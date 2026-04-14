"""
Insert EA.org take-action images into get-involved.html action cards.

For each <a class="action-card"> in the file, identified by its href:
  - Insert an .action-card-img-wrap with the mapped image
  - Wrap existing children (h4, p, span) in .action-card-body
"""

import re
from pathlib import Path

HTML_PATH = Path(r"G:\Mon Drive\EA Bogotá\website\get-involved.html")

# href -> image filename in img/take-action/
# Order matches the visual order on the page (sections 1..5)
MAPPING = {
    # Section 1 — Contribuye con tu tiempo
    "opportunities.html":                                               "find-volunteering.jpg",
    "https://80000hours.org/career-guide/":                             "career-guide.jpg",
    "https://probablygood.org/advising/":                               "career-advising.jpg",
    "https://jobs.80000hours.org/":                                     "high-impact-job.jpg",
    "team.html#join":                                                   "talent-database.jpg",
    "https://www.effectivealtruism.org/get-involved/newsletter":        "best-of-forum.jpg",

    # Section 2 — Dona efectivamente
    "https://www.givingwhatwecan.org/best-charities-to-donate-to-2025": "best-charities-2025.webp",
    "https://www.givewell.org/":                                        "global-health-charities.jpeg",
    "https://farmkind.giving/":                                         "animal-welfare.jpg",
    "https://www.givingwhatwecan.org/pledge":                           "pledge-to-donate.jpg",
    "https://funds.effectivealtruism.org/":                             "ea-funds.jpg",  # also S4 C3
    "resources.html#giving":                                            "ea-forum-giving.jpeg",

    # Section 3 — Conecta con otros
    "https://forum.effectivealtruism.org/":                             "ea-forum.png",
    "https://www.effectivealtruism.org/groups":                         "local-group.jpg",
    "https://www.effectivealtruism.org/ea-global":                      "conference.jpg",
    "events.html":                                                      "local-event.jpeg",
    "https://www.magnifymentoring.org/":                                "magnify-mentoring.jpg",
    "team.html":                                                        "start-ea-group.jpeg",  # also S4 C2

    # Section 4 — Empieza algo nuevo
    "https://www.charityentrepreneurship.com/":                         "charity-entrepreneurship.jpg",
    "https://tally.so/r/NpJlYN":                                        "start-ea-group.jpeg",
    # NOTE: S4 C3 "Busca financiación" reuses funds.effectivealtruism.org -> already mapped above

    # Section 5 — Aprende más
    "about-ea.html":                                                    "intro-to-ea.jpg",
    "https://www.effectivealtruism.org/virtual-programs/introductory-program": "intro-course.jpg",
    "https://forum.effectivealtruism.org/handbook":                     "ea-handbook.jpg",
    "resources.html#reading":                                           "books-podcasts.jpg",
    "resources.html#careers":                                           "career-guide.jpg",  # reuse
    "https://probablygood.org/cause-areas/":                            "find-cause.jpg",
}


def transform(html: str) -> str:
    """Walk every <a class="action-card"...>...</a> block and rewrite it."""
    # Match the full anchor block — non-greedy across newlines
    card_re = re.compile(
        r'(<a\s+href="(?P<href>[^"]+)"[^>]*class="action-card"[^>]*>)'
        r'(?P<inner>.*?)'
        r'(</a>)',
        re.DOTALL,
    )

    def replace(m: re.Match) -> str:
        opening = m.group(1)
        href = m.group("href")
        inner = m.group("inner")
        closing = m.group(4)

        if href not in MAPPING:
            print(f"  WARN no image mapped for {href}")
            return m.group(0)

        img_file = MAPPING[href]
        img_block = (
            '\n          <div class="action-card-img-wrap">'
            f'<img class="action-card-img" src="img/take-action/{img_file}" alt="" loading="lazy">'
            '</div>'
        )
        # Re-wrap inner content (currently h4 + p + span) in .action-card-body.
        # Strip leading/trailing whitespace inside the anchor for cleaner output, then re-indent.
        body_block = (
            '\n          <div class="action-card-body">'
            f'{inner.rstrip()}\n          </div>\n        '
        )
        return f"{opening}{img_block}{body_block}{closing}"

    new_html, n = card_re.subn(replace, html)
    print(f"\nReplaced {n} action-card blocks.")
    return new_html


def main() -> None:
    src = HTML_PATH.read_text(encoding="utf-8")
    out = transform(src)
    HTML_PATH.write_text(out, encoding="utf-8")
    print(f"Wrote {HTML_PATH}")


if __name__ == "__main__":
    main()
