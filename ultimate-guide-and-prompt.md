# How to Save the Reference CSS/HTML + The Ultimate Prompt

## Step 1: Save the Reference Site's CSS (30 seconds)

Open https://www.effectivealtruism.org/ in Chrome. Then:

1. Right-click → **View Page Source** (or Ctrl+U)
2. Ctrl+A to select all, Ctrl+C to copy
3. Paste into a file: `/docs/reference/homepage.html`
4. Repeat for any other pages you want (/take-action, /faqs, /articles/introduction-to-effective-altruism)

To grab the CSS specifically:

1. Open DevTools (F12) → **Sources** tab
2. Look in the left sidebar under the domain → `_next/static/css/`
3. Click each `.css` file, then Ctrl+A → Ctrl+C
4. Paste into `/docs/reference/main.css` (combine them into one file)

**Even faster method** — paste this in the Console (F12 → Console):

```javascript
// Extracts all inline + linked CSS into one blob and copies it
(async () => {
  let allCSS = '';

  // Inline styles
  document.querySelectorAll('style').forEach((s, i) => {
    allCSS += `/* === INLINE STYLE BLOCK ${i + 1} === */\n${s.textContent}\n\n`;
  });

  // External stylesheets
  for (const link of document.querySelectorAll('link[rel="stylesheet"]')) {
    try {
      const res = await fetch(link.href);
      const text = await res.text();
      allCSS += `/* === ${link.href} === */\n${text}\n\n`;
    } catch (e) {
      allCSS += `/* === FAILED: ${link.href} === */\n\n`;
    }
  }

  // Also grab CSS from CSSOM (covers dynamically injected styles)
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        allCSS += rule.cssText + '\n';
      }
    } catch (e) {} // cross-origin sheets will throw
  }

  try {
    await navigator.clipboard.writeText(allCSS);
    console.log('%c✅ All CSS copied to clipboard! (' + (allCSS.length / 1024).toFixed(0) + ' KB)', 'color: green; font-size: 16px;');
  } catch (e) {
    console.log('%c⚠️ Clipboard blocked. Output below:', 'color: orange; font-size: 14px;');
  }
  console.log(allCSS);
})();
```

Save the output as `/docs/reference/extracted.css` in your project.


## Step 2: Your Project File Structure

After doing all the above, your `/docs/` folder should look like:

```
/docs/
  style-guide.md              ← (the merged design tokens file)
  visual-reference.md          ← (the screenshot descriptions file)
  reference/
    homepage.html              ← (view-source of the homepage)
    extracted.css              ← (all CSS from the console script)
```


## Step 3: The Ultimate CLAUDE.md Section

Add this to your project's `CLAUDE.md`:

```markdown
## Design System — MANDATORY

Before writing or modifying ANY CSS, styled component, or UI markup:

1. Read `/docs/style-guide.md` for exact design token values (colors, fonts, spacing, radii, shadows)
2. Read `/docs/visual-reference.md` for layout patterns, component structures, and section-by-section descriptions
3. Reference `/docs/reference/extracted.css` and `/docs/reference/homepage.html` for the actual source CSS and markup

### Hard Rules
- Background is ALWAYS #f4efe9, never white
- Headings: Inter, weight 600, with NEGATIVE letter-spacing (-2px for h1 down to -0.2px for h6)
- Body text: Times New Roman, 16px, weight 400
- Buttons: #000000 bg, #ffffff text, 0px border-radius (square), no shadows
- No box shadows (except the rare subtle one noted in the style guide)
- No gradients anywhere
- No rounded buttons
- Cards: no border, no shadow, no background — they sit flat on #f4efe9
- Spacing: use the scale from style-guide.md (based on 8px unit)
- Max content width: 1240px–1280px, centered
- 3-column grids with ~24px gap for card layouts
- Accordions: thin black separator lines, "+" icon on right, no bg change
- Links: #0000ee or #0c859a (teal, in article contexts)
- Footer: #212121 dark background
- The overall feel is editorial/journal — like a sophisticated newspaper, not a tech startup
```


## Step 4: The Ultimate Prompt

Paste this single prompt into Claude Code (terminal). It handles everything — fetching the reference site, reading your docs, auditing, and fixing:

---

```
STEP 0 — FETCH THE REFERENCE SITE:
Create the folder /docs/reference/ if it doesn't exist. Then run:
  curl -sL https://www.effectivealtruism.org/ -o docs/reference/homepage.html
  curl -sL https://www.effectivealtruism.org/take-action -o docs/reference/take-action.html
  curl -sL https://www.effectivealtruism.org/faqs -o docs/reference/faqs.html
Inspect each saved HTML file for any <link rel="stylesheet"> tags or CSS file paths (likely under _next/static/css/). Fetch each CSS URL you find and save them all into docs/reference/extracted.css. If no external stylesheets are found, extract all <style> blocks from the HTML files into extracted.css instead.

STEP 1 — READ ALL REFERENCE MATERIALS (do this before changing anything):
1. /docs/style-guide.md — exact design token values
2. /docs/visual-reference.md — layout patterns and component descriptions from screenshots
3. /docs/reference/extracted.css — the actual CSS from the live site
4. /docs/reference/homepage.html — the actual HTML structure

STEP 2 — AUDIT AND FIX every component and page in the current codebase:

2a. FIX TOKENS: Replace any color not in the style guide. Replace any font not in the style guide. Replace any border-radius on buttons that isn't 0px. Remove any box-shadow that isn't the one documented subtle shadow. Change any white (#fff/#ffffff) background to #f4efe9 where it should be the page background.

2b. FIX TYPOGRAPHY: Headings must use Inter with the exact sizes, weights, and negative letter-spacing from the style guide table. Body text must use Times New Roman 16px. Check every heading level.

2c. FIX LAYOUT: Cards should be flat (no border, no shadow, no bg) in 3-column grids. Sections should have 48-90px vertical padding. Content max-width should be 1240-1280px. Match the layout patterns described in visual-reference.md.

2d. FIX COMPONENTS: Buttons must be square (0px radius), black bg, white text. Accordions must use thin black lines as separators with a "+" icon. The footer must be #212121. The newsletter CTA must match the reference.

2e. MATCH THE VIBE: Compare your work against visual-reference.md. The site should feel like an editorial journal — warm, flat, typographically driven, lots of whitespace, serif body + sans-serif headings. If something looks "techy" or "startup-y", it's wrong.

STEP 3 — REPORT: List every change you made — file, property, old value, new value.
```

---

That's everything. This prompt makes Claude Code:
- Fetch the reference HTML and CSS itself (no manual browser work needed)
- Read all your reference docs (style guide, visual descriptions, fetched source)
- Systematically audit the codebase against them
- Fix deviations category by category
- Report what it changed so you can verify
