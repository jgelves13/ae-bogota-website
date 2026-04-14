"""
Download all 25 images from EA.org /take-action page and save them locally.
URLs were captured live via Playwright in a prior session.
"""

import os
import shutil
import tempfile
import urllib.request

OUT_DIR = r"G:\Mon Drive\EA Bogotá\website\img\take-action"

# (slug, contentful_asset_id, hash, filename) — captured from EA.org
IMAGES = [
    # Section 1 — Contribuye con tu tiempo
    ("find-volunteering",        "6Pez5KoLXGpBOnRJsVvuRK", "e662ca5fb0624d69625619b2ea1d6fe8", "aimee.jpg"),
    ("career-guide",             "6K0Ufqg10tklnmqKqPorlL", "5045aacf9d99c48001b357882a7c0e85", "career-guide__1_.jpg"),
    ("career-advising",          "1Z2zxMLyWYuAWKhFMOSvU7", "4aebf416b668638530809f6f45f95bf4", "katiejessica_1__1_.jpg"),
    ("high-impact-job",          "6PEIJad3ISK8pnp9ZJ1xmX", "8d3cd1d99eaa8f836690b8bf446da2e6", "find-a-high-impact-job.jpg"),
    ("talent-database",          "1wiNbKr1IomzGJr1cuXgnO", "cc39a6e21eee0ef8199a361a5782335e", "talent-database__1_.jpg"),

    # Section 2 — Dona efectivamente
    ("best-charities-2025",      "6tGvllGVbk8khlhitwdn1Z", "98e44a1baa4e69f6dcfa2f0c3e36286e", "b887cd8cd6d66d56b45e460a7c5824eb__1_.webp"),
    ("global-health-charities",  "4KBw4GfD7GmuTQAAW1SI3s", "8832e25561a37668912394073de4144d", "malaria-consortium.jpeg"),
    ("animal-welfare",           "5CbeUNW4RRXFMi3CQKTWhX", "c8c234670dc6a3fb265073e56e077a7c", "b-cole-tZDQqzD3EqI-unsplash__1_.jpg"),
    ("pledge-to-donate",         "5NApVgxHmg6MZ9IaJwkN4v", "b8e8b99ce43d8dd549ac863d90b4abdf", "pledge.jpg"),
    ("ea-funds",                 "3fyDhZkfnYpoC6lQHMAHV8", "8032c513f5bff3635a36a9897ecac71d", "image.jpg"),
    ("ea-forum-giving",          "3WfFDX3aHg1hAH3yd7j6ij", "3668a9f08384edc9b3696b922718db30", "career-guidance__1_.jpeg"),

    # Section 3 — Conecta con otros
    ("ea-forum",                 "AfclzWlVO8iuh9ToHuB7P", "0057664065163f4ed24d167ec8dda5c8", "effective-altruism-forum.png"),
    ("local-group",              "44LcGfHAHmo2XrwP0CYcC9", "3763b9f5fc3169b1e79ba31f66b42a74", "image-2.jpg"),
    ("conference",               "6a7JzB5ro2s2ZTLop52ToC", "7101465be74991825dae58118ecadbbd", "image_34.jpg"),
    ("local-event",              "6nUGjd8aVPJ2bXenM1nEER", "0fdec19b7656aceb28f185d9af0d7210", "7R506715__1_.jpeg"),
    ("magnify-mentoring",        "2xA6t1Zir3tuJCH89C3i0Z", "7c621ccf099b694658edcc11289036e4", "conference-chat.jpg"),

    # Section 4 — Empieza algo nuevo
    ("charity-entrepreneurship", "184YSJ67E8uDzEPaG88ClE", "d9d92e62f7fd3516b8637bb2ab856d97", "charity-entrepreneurship.jpg"),
    ("start-ea-group",           "52TWOz6dXGxFhFkpbtBO6R", "311347efeac98564a8e7d26cef6f2ab8", "MJB_8876__1_.jpeg"),
    # Note: section 4 "Seek funding" reuses the EA Funds image (same asset)

    # Section 5 — Aprende más
    ("intro-to-ea",              "6j6BwYr6VCYqDa65noFZGl", "564eed3d76045e8c46f45ea1ace1004e", "intro-to-ea.jpg"),
    ("intro-course",             "1ggJRLlHkzlCcq0BQQfl0v", "ba216a489caeb03ae5620e2cd8d87d98", "intro-course.jpg"),
    ("find-cause",               "7L813uLpOM1xLHGBjMQQq3", "a214fdaf0766a89e3d12893fb59d6c64", "4427_Hauwa_Ibrahim__Caregiver__Hamza__Infant__Abubakar_Yahaya__Child__2__1_.jpg"),
    ("ea-handbook",              "1PtN5BVeOO1tswE5DZoL1S", "c780216c09568dfffff4a6eb755948a6", "nasa-yZygONrUBe8-unsplash.jpg"),
    ("books-podcasts",           "1FjZTcRVHQtK7OIpbKXrW3", "b34f67cc9e4d6dbc21a81af878c90866", "peter-singer-ted.jpg"),
    ("best-of-forum",            "qLc1stEDjmT4r8OOaWHaZ",  "c4e34c444ba292af955468b32cf6fae0", "image-2.jpg"),
]


def build_url(asset_id: str, hash_: str, filename: str) -> str:
    """Build the direct Contentful CDN URL (no Next.js wrapper needed)."""
    return f"https://images.ctfassets.net/ohf186sfn6di/{asset_id}/{hash_}/{filename}?fit=fill&w=1600"


def download(slug: str, asset_id: str, hash_: str, filename: str) -> str:
    url = build_url(asset_id, hash_, filename)
    # Determine extension from source filename
    ext = os.path.splitext(filename)[1].lower()
    if not ext:
        ext = ".jpg"
    out_name = f"{slug}{ext}"
    final_path = os.path.join(OUT_DIR, out_name)

    # Workaround for Google Drive sync issues: write to temp first, then copy.
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
    tmp.close()
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AE-Bogota-bot/1.0)"},
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(tmp.name, "wb") as f:
                shutil.copyfileobj(resp, f)
        size = os.path.getsize(tmp.name)
        if size < 500:
            raise RuntimeError(f"Suspicious file size {size} for {url}")
        os.makedirs(OUT_DIR, exist_ok=True)
        shutil.copy2(tmp.name, final_path)
        return f"OK   {out_name}  ({size:,} bytes)"
    except Exception as e:
        return f"FAIL {out_name}: {e}"
    finally:
        try:
            os.remove(tmp.name)
        except OSError:
            pass


def main() -> None:
    print(f"Downloading {len(IMAGES)} images to {OUT_DIR}\n")
    for slug, asset_id, hash_, filename in IMAGES:
        print(download(slug, asset_id, hash_, filename))
    print("\nDone.")


if __name__ == "__main__":
    main()
