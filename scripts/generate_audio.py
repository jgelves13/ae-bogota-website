"""
Regenerate audio/essay-es.mp3 from about-ea.html using ElevenLabs Multilingual v2.

Voice: Leo (es-CO, Colombian native, male, narrative-tuned).
The English audio (audio/essay-en.mp3) is the official EA.org Buzzsprout
recording — do NOT regenerate it from this script.

Multilingual v2 has a per-request limit, so the essay is split into chunks at
paragraph boundaries (max ~4500 chars). Each request uses previous_text /
next_text to keep prosody smooth across chunk boundaries. The resulting MP3
fragments are concatenated as binary streams (works for ElevenLabs MP3 output).

Run:
    py scripts/generate_audio.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup


REPO_ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = REPO_ROOT / "about-ea.html"
AUDIO_DIR = REPO_ROOT / "audio"
ENV_PATH = REPO_ROOT / ".env"

API_BASE = "https://api.elevenlabs.io/v1"
MODEL_ID = "eleven_multilingual_v2"
VOICE_ID_LEO = "Ux2YbCNfurnKHnzlBHGX"  # Leo - Colombian Spanish narrative voice
MAX_CHARS_PER_CHUNK = 4500


def load_api_key() -> str:
    if not ENV_PATH.exists():
        sys.exit(f"Missing .env at {ENV_PATH}")
    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("ELEVENLABS_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("ELEVENLABS_API_KEY not found in .env")


def extract_essay_text(html: str, lang: str = "es") -> str:
    """Extract clean narration text from the essay div for the given language."""
    soup = BeautifulSoup(html, "html.parser")

    candidates = soup.find_all("div", attrs={"data-lang": lang})
    essay_div = None
    for div in candidates:
        if div.find("p", recursive=False) or div.find("h2", recursive=False):
            essay_div = div
            break
    if essay_div is None:
        raise RuntimeError(f"Could not find essay div for lang={lang}")

    # Strip footnote popups (long source citations) and ref numbers.
    for popup in essay_div.find_all("span", class_="fn-popup"):
        popup.decompose()
    for ref in essay_div.find_all("span", class_="fn-ref"):
        ref.decompose()
    # Drop images.
    for img in essay_div.find_all("img"):
        img.decompose()
    # Drop the CC attribution paragraph.
    for p in essay_div.find_all("p"):
        style = p.get("style", "") or ""
        if "border-top" in style:
            p.decompose()
    # Drop the inline newsletter aside (CTA, not essay content).
    for aside in essay_div.find_all("aside"):
        aside.decompose()

    blocks: list[str] = []
    for el in essay_div.find_all(["h2", "h3", "p", "li"]):
        text = el.get_text(" ", strip=True)
        if text:
            blocks.append(text)

    full = "\n\n".join(blocks)
    full = re.sub(r"[ \t]+", " ", full)
    full = re.sub(r"\n{3,}", "\n\n", full)
    return full.strip()


def chunk_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> list[str]:
    """Split text into chunks of <= max_chars at paragraph boundaries."""
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    current = ""
    for p in paragraphs:
        candidate = (current + "\n\n" + p) if current else p
        if len(candidate) > max_chars and current:
            chunks.append(current)
            current = p
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def synthesize_chunk(
    api_key: str,
    text: str,
    voice_id: str,
    previous_text: str | None,
    next_text: str | None,
) -> bytes:
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }
    if previous_text:
        payload["previous_text"] = previous_text[-1000:]  # last ~1000 chars for context
    if next_text:
        payload["next_text"] = next_text[:1000]

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{API_BASE}/text-to-speech/{voice_id}",
        data=body,
        method="POST",
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        body_txt = e.read().decode("utf-8", errors="replace")
        sys.exit(f"HTTP {e.code} from ElevenLabs: {body_txt}")


def main() -> None:
    api_key = load_api_key()
    html = HTML_PATH.read_text(encoding="utf-8")
    text = extract_essay_text(html, "es")
    print(f"[ES] essay text: {len(text):,} chars")

    chunks = chunk_text(text)
    print(f"[ES] split into {len(chunks)} chunks (max {MAX_CHARS_PER_CHUNK} chars each)")
    for i, c in enumerate(chunks, 1):
        print(f"     chunk {i}: {len(c):,} chars")

    total_chars = sum(len(c) for c in chunks)
    print(f"[ES] total characters to bill: {total_chars:,}")

    # Generate each chunk with prosody continuity context.
    audio_parts: list[bytes] = []
    for i, chunk in enumerate(chunks):
        prev = chunks[i - 1] if i > 0 else None
        nxt = chunks[i + 1] if i < len(chunks) - 1 else None
        print(f"\n[{i + 1}/{len(chunks)}] generating ({len(chunk):,} chars)...")
        audio = synthesize_chunk(api_key, chunk, VOICE_ID_LEO, prev, nxt)
        print(f"        ok ({len(audio):,} bytes)")
        audio_parts.append(audio)

    # Concatenate as binary (works for ElevenLabs MP3 stream output).
    combined = b"".join(audio_parts)

    # Save via tempfile to avoid Google Drive 0KB sync bug.
    tmp = Path(tempfile.gettempdir()) / "essay-es.mp3"
    tmp.write_bytes(combined)

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    out = AUDIO_DIR / "essay-es.mp3"
    shutil.copy2(tmp, out)
    tmp.unlink(missing_ok=True)

    print(f"\nWrote {out} ({len(combined):,} bytes total)")


if __name__ == "__main__":
    main()
