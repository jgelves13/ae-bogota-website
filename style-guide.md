# Style Guide — Effective Altruism (effectivealtruism.org)

> Extracted from homepage + /take-action + /articles/introduction-to-effective-altruism
> Date: 2026-04-07

## Colors

### Backgrounds
- Primary: `#f4efe9` (warm off-white — used everywhere)
- Dark: `#212121` (dark sections, footer)
- Black: `#000000` (buttons, accents)
- White: `#ffffff` (cards, overlays)
- Muted: `#757575` (secondary surfaces)
- Feature: `#c9d7d8` (teal-tinted accent bg)
- Near-white: `#fafafa` (subtle alternate bg)

### Text
- Primary: `#000000`
- Inverted: `#ffffff` (on dark backgrounds)
- Secondary: `#757575`
- Muted: `#808080`
- Light: `#fafafa` (on dark backgrounds)
- Link: `#0000ee`
- Link accent: `#0c859a` (teal, used in article contexts)
- Dark: `#212121`

### Borders
- Primary: `#000000`
- Light: `#fafafa`
- White: `#ffffff`

## Typography

### Font Families
- **Headings**: "Inter" (from Google Fonts)
- **Body**: "Times New Roman" (system serif)
- **Alternate serif**: "Charis SIL" (used in some body contexts)
- **Fallback sans**: "Arial"

### Font Source
- https://fonts.googleapis.com/

### Headings (all Inter, weight 600)
| Level | Size | Line-height | Letter-spacing |
|-------|------|-------------|----------------|
| h1    | 54px | 56.7px      | -2px           |
| h2    | 30px | 39px        | -1.2px         |
| h3    | 22px | 26.4px      | -0.28px        |
| h4    | 20px | 24px        | -0.28px        |
| h5    | 18px | 23.4px      | -0.2px         |
| h6    | 16px | 22.4px (weight 500) | -0.2px  |

### Body Text
- Font: "Times New Roman"
- Size: 16px
- Weight: 400
- Line-height: normal
- Color: `#000000`

## Spacing Scale (px)
1, 2, 4, 6, 8, 12, 14, 16, 18, 20, 24, 32, 40, 48, 60, 76, 80, 90

Base unit appears to be **8px**, with smaller values (2, 4) for tight gaps and larger values (48, 60, 76, 80, 90) for section padding.

## Borders & Shadows

### Border Radii
- Small: `6px`
- Medium: `12px`
- Circle: `50%`
- Buttons: `0px` (square corners)

### Box Shadows
- Subtle (rare): `rgba(0, 0, 0, 0.14) 0px 1px 5px 0px` (found on article page elements)
- The site is overwhelmingly flat — shadows are the exception, not the rule.

## Layout

### Max Widths
- Main container: `1280px`
- Content container: `1240px`
- Narrow content: `752.4px`
- Card/component: `576px`
- Small component: `min(520px, 100%)`

## Transitions
- General: `all` (various durations)
- Opacity: `opacity 0.2s ease-in-out`
- Opacity slow: `opacity 0.4s`
- Transform: `transform 0.15s ease-in-out` / `transform 0.2s ease-in-out`
- Max-width: `max-width 0.2s ease-in-out`

## Buttons

### Primary Button
- Background: `#000000`
- Text: `#ffffff`
- Font size: 13.3px
- Weight: 400
- Padding: `12px 24px`
- Border: `0.8px solid rgb(0, 0, 0)`
- Border radius: `0px` (sharp square corners)
- Text transform: none

### Nav/Inline Button
- Background: `#000000`
- Text: `#ffffff`
- Font size: 15px
- Weight: 550
- Padding: `0px`
- Border radius: `0px`

## Design Personality

Key traits that define the EA site aesthetic:
- **Flat**: Almost no box shadows. A very subtle one (`0px 1px 5px`) appears rarely on article pages, but the default is zero elevation.
- **Editorial serif + clean sans**: Body in Times New Roman, headings in Inter — gives a newspaper/journal feel.
- **Tight letter-spacing on headings**: Negative letter-spacing (-0.28px to -2px) makes headings feel dense and authoritative.
- **Warm neutral palette**: The `#f4efe9` background is the signature — not white, not beige, but a warm paper tone.
- **Square buttons**: 0px border radius on all buttons. No rounding. Very deliberate.
- **Restrained color use**: Almost everything is black, white, and the warm off-white. Color is rare and intentional.
- **Generous section spacing**: Large values (48–90px) between sections create breathing room.

---

## CLAUDE.md Instructions

Add this to your project's `CLAUDE.md`:

```
## Design System
- Before writing ANY CSS or styled component, read /docs/style-guide.md
- Use ONLY the colors, fonts, spacing, and radii defined there
- Match the reference site's flat, editorial aesthetic exactly
- No box shadows. No rounded buttons. No gradients.
- Headings: Inter with negative letter-spacing. Body: Times New Roman.
- Primary background is always #f4efe9, not white.
```
