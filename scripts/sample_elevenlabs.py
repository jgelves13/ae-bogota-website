"""
Generate short voice samples with ElevenLabs to pick the best LATAM Spanish voice
for the about-ea.html essay narration.

Strategy:
  1. Fetch all voices available in the workspace.
  2. Pick LATAM/Spanish-tagged voices first; fall back to popular premade voices
     known to work well for Spanish narration with English code-switching.
  3. Generate a ~340-char sample with each candidate using Multilingual v2.
  4. Save to audio/samples/ for human review.

Run:
    py scripts/sample_elevenlabs.py
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

import urllib.request
import urllib.error


REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = REPO_ROOT / ".env"
SAMPLES_DIR = REPO_ROOT / "audio" / "samples"

API_BASE = "https://api.elevenlabs.io/v1"
MODEL_ID = "eleven_multilingual_v2"

# Sample text: includes English names so we hear how each voice handles
# code-switching (GiveWell, Open Philanthropy, 80,000 Hours).
SAMPLE_TEXT = (
    "El altruismo eficaz es un proyecto que busca encontrar las mejores "
    "formas de ayudar a los demás, y ponerlas en práctica. Organizaciones "
    "como GiveWell, Open Philanthropy y 80,000 Hours han ayudado a salvar "
    "miles de vidas y a orientar a personas hacia carreras de alto impacto. "
    "Esta es una muestra de voz para el ensayo de Altruismo Eficaz Bogotá."
)

# Premade fallback voices (always present in every ElevenLabs account).
# These are known to handle Spanish reasonably well via Multilingual v2.
PREMADE_FALLBACKS: list[tuple[str, str]] = [
    ("Sarah",     "EXAVITQu4vr4xnSDxMaL"),  # F, neutral, soft
    ("Charlotte", "XB0fDUnXU5powFXDhCwa"),  # F, warm, popular for ES
    ("Bill",      "pqHfZKP75CvOlQylNhV4"),  # M, friendly, conversational
    ("Antoni",    "ErXwobaYiN019PkySvjV"),  # M, well-rounded, warm
]


def load_api_key() -> str:
    if not ENV_PATH.exists():
        sys.exit(f"Missing .env at {ENV_PATH}")
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("ELEVENLABS_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("ELEVENLABS_API_KEY not found in .env")


def http_get(url: str, api_key: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"xi-api-key": api_key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_post_audio(url: str, api_key: str, payload: dict, out_path: Path) -> None:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )
    tmp_dir = Path(tempfile.gettempdir())
    tmp_out = tmp_dir / out_path.name
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            tmp_out.write_bytes(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"HTTP {e.code} from {url}: {body}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(tmp_out, out_path)
    tmp_out.unlink(missing_ok=True)


def pick_candidates(voices: list[dict]) -> list[tuple[str, str, str]]:
    """Pick up to 4 candidate voices.

    Returns list of (voice_name, voice_id, source_label).
    Priority:
      1. Voices labeled with Spanish / LATAM.
      2. Multilingual-tagged voices.
      3. Premade fallbacks.
    """
    chosen: list[tuple[str, str, str]] = []
    seen_ids: set[str] = set()

    def add(name: str, vid: str, label: str) -> None:
        if vid in seen_ids or len(chosen) >= 4:
            return
        chosen.append((name, vid, label))
        seen_ids.add(vid)

    # Pass 1: any voice with Spanish-related labels in its metadata.
    for v in voices:
        labels = v.get("labels") or {}
        all_text = " ".join(str(x).lower() for x in labels.values())
        descr = (v.get("description") or "").lower()
        name = v.get("name", "?")
        vid = v.get("voice_id")
        if not vid:
            continue
        if any(k in all_text for k in ("spanish", "español", "latam", "latin", "mexic", "colomb")) \
                or any(k in descr for k in ("spanish", "español", "latam", "latin")):
            add(name, vid, "library:spanish")

    # Pass 2: any voice tagged multilingual.
    for v in voices:
        labels = v.get("labels") or {}
        all_text = " ".join(str(x).lower() for x in labels.values())
        descr = (v.get("description") or "").lower()
        if "multilingual" in all_text or "multilingual" in descr:
            add(v.get("name", "?"), v["voice_id"], "library:multilingual")

    # Pass 3: premade fallbacks.
    for name, vid in PREMADE_FALLBACKS:
        add(name, vid, "premade")

    return chosen


def main() -> None:
    api_key = load_api_key()
    print(f"Fetching voices from {API_BASE}/voices ...")
    data = http_get(f"{API_BASE}/voices", api_key)
    voices = data.get("voices", [])
    print(f"Found {len(voices)} voices in workspace.")

    candidates = pick_candidates(voices)
    print(f"\nGenerating {len(candidates)} samples ({len(SAMPLE_TEXT)} chars each):")
    for name, vid, label in candidates:
        print(f"  - {name:20s}  [{label}]  {vid}")

    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
    payload_base = {
        "text": SAMPLE_TEXT,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }

    for name, vid, label in candidates:
        safe_name = name.replace(" ", "_").replace("/", "_")
        out_path = SAMPLES_DIR / f"sample_{safe_name}.mp3"
        url = f"{API_BASE}/text-to-speech/{vid}"
        print(f"\n  generating {name} -> {out_path.name}")
        http_post_audio(url, api_key, payload_base, out_path)
        print(f"  ok ({out_path.stat().st_size:,} bytes)")

    print(f"\nDone. Listen to samples in: {SAMPLES_DIR}")
    total_chars = len(SAMPLE_TEXT) * len(candidates)
    print(f"Used ~{total_chars:,} characters of your monthly allowance.")


if __name__ == "__main__":
    main()
