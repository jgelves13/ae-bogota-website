# EA Bogota — Visual Reference (effectivealtruism.org)

Detailed layout and component descriptions extracted from the three reference pages on effectivealtruism.org. Use alongside `style-guide.md` for design tokens.

---

## Global Elements (shared across all pages)

### Navigation Bar

- **Position**: Fixed top, full-width, sits on the warm sand background (`#F4EFE9`)
- **Height**: ~76px (main content starts with `margin-top: 76px`)
- **Layout**: Single row, logo left, links right
- **Logo**: "Effective Altruism" wordmark + small lightbulb icon, left-aligned, links to `/`
- **Nav links** (left to right): Learn (dropdown), Take action, Courses, Opportunities board, Conferences (external icon), EA Funds (external icon)
  - "Learn" has a **dropdown panel** containing: Intro essay, FAQs, Videos/books/podcasts, Online intro course, Community stories, EA Newsletter, EA Handbook (external), EA Forum (external)
  - External links show a small arrow/external-link icon after the text
- **Typography**: Inter, ~14px, weight 400, black text
- **Behavior**: No background color change on scroll; clean, flat appearance; no box-shadow

### Newsletter Slide-in (popup)

- **Trigger**: Appears after short scroll on every page
- **Position**: Top of `<main>`, overlaid content
- **Content**: Dismiss button (X), h4 heading "Get more ideas on how to make a difference", description paragraph, email input + "Subscribe" button, "60k+ subscribers" social proof line
- **Style**: Same warm sand background, black text, black square button

### Footer

- **Background**: `#000000` (pure black), full-width
- **Padding**: 80px all sides
- **Text**: `#FFFFFF` (white), Times New Roman, 16px
- **Layout**: Two major rows
  - **Row 1 — left column**: h3 heading "Start making a difference with your donations and career" + email input + Subscribe button + "Join 60k subscribers..." text with "View past editions" link. Legal paragraph below (Centre for Effective Altruism, Effective Ventures, charity registration numbers)
  - **Row 1 — right columns**: Two link columns side by side:
    - Column 1 ("Effective Altruism"): Stories, Learn, Take action, Courses, Conferences, Opportunities board, EA Funds, EA Forum, FAQ
    - Column 2 ("About this website"): Made by CEA, Contact, Privacy Policy, Cookie notice
  - **Row 2**: "© 2026 Effective Ventures" left, social icons right (LinkedIn, Instagram, X, YouTube) as small white icons
- **Typography**: Footer headings in Inter 600, links in serif, ~14px
- **Separators**: None; columns distinguished by whitespace alone

### Horizontal Rule / Section Divider

- Simple `<hr>` / `<separator>`, thin 1px black line, full content width
- Used between major page sections (especially on Take Action and FAQs pages)

---

## Page 1: Homepage (`/`)

### Hero Section

- **Background**: Full-width photographic image (aerial nature shot — earth tones, water, trees), dark overlay for text legibility
- **Layout**: Centered text on image
- **h1**: "Turning good intentions into greater impact"
  - Inter, 72px, weight 600, letter-spacing -3px, line-height 1.04, white text
  - Margin-bottom: 24px
- **Subtitle** (h6): "Meet people applying effective altruism to do more good with their time, money, and resources."
  - Smaller, lighter weight, white text
- **CTAs**: Two buttons side by side — "Watch stories" and "Take action"
  - Black background, white text, square (0px border-radius), 1px border
  - Padding: 12px 24px
  - Inter, 16px, weight 400

### "What is effective altruism?" Section

- **Spacing**: ~90px top padding from hero
- **h2**: "What is effective altruism?" — Inter, 44px, weight 600, letter-spacing -1.2px, line-height 1.2, black text
- **Horizontal rule** below heading
- **Layout**: Two-column grid below the heading
  - **Column 1**: h3 "A philosophy" + serif paragraph describing the approach + inline link
  - **Column 2**: h3 "A movement" + serif paragraph
- **h3**: Inter, 28px, weight 600, letter-spacing -0.28px
- **Body text**: Times New Roman, 16px, weight 400, black

### "As Featured In" Logo Bar

- **Layout**: "As featured in" label left-aligned, then a horizontal row of 6 grayscale media logos: TED, New York Times, The Guardian, Forbes, The Economist, BBC
- **Style**: Logos are neutral/grayscale, each is a link to the source article
- **Spacing**: Compact, minimal vertical padding (~24px above and below)

### Newsletter + Books CTA Section

- **Layout**: Three-column grid left, content block right
  - Left: 2 rows x 3 columns of book cover images (The Precipice, Doing Good Better, Animal Liberation Now, The Life You Can Save, 80000 Hours, Famine Affluence and Morality)
  - Right: h3 "More ideas on how to make a difference — and a free book" + description paragraph + email input + Subscribe button + "60k+ subscribers" line + "Read past editions" link
- **Book images**: No border, no shadow, directly on sand background

### "Effective Altruism in Action" Section — Story Carousel

- **Header**: h2 "Effective altruism in action" + italic serif subtitle describing the section
- **Carousel**: Horizontally-scrolling card carousel with left/right arrow navigation buttons
- **Story cards**: Each card is a link to `/stories/{name}`, containing:
  - **Thumbnail image**: Large portrait photo with overlay badge ("Watch" or "Read" + play/read icon)
  - **Quote** (h6): A pull-quote from the person, in quotes, serif italic style
  - **Divider**: Thin horizontal rule
  - **Name**: Bold text (person's name)
  - **Role description**: Short description like "Software engineer turned charity incubator COO"
- **Card style**: No border, no shadow, no background — flat on sand. Text sits directly below image
- **Navigation arrows**: Circular or icon buttons at left and right edges of the carousel

### "What the Community Has Achieved" Section

- **h2**: "What the community has achieved" + subtitle paragraph
- **Component**: Accordion / expandable list (5 items):
  1. Global health and economic development
  2. Animal welfare
  3. Existential risk and the long-term future
  4. Research and charity evaluation
  5. Grantmaking, fundraising, and donor advising
- **Accordion style**: Each item shows an h6 heading + "+" toggle on the right. Items are separated by horizontal rules. Click expands to reveal content below. No background color change, no border, no shadow — purely typographic

### "Four Ideas You Probably Already Agree With" Section

- **h2**: "Four ideas you probably already agree with"
- **Subtitle**: Serif paragraph "That could mean you're already on board with effective altruism"
- **Horizontal rule** below subtitle
- **Layout**: 4 items in a 2x2 grid (or stacked on mobile)
  - Each item: h4 numbered title ("1. It's important to help others") + serif body paragraph
  - Some paragraphs contain inline links
- **h4**: Inter, ~20px, weight 600, letter-spacing -0.28px
- **CTA link below**: "Read more in the intro" with arrow icon, black text, links to intro essay

### "Research and Ideas" Section

- **h2**: "Research and ideas" + subtitle
- **Layout**: 2-row x 3-column card grid (6 cards total)
- **Research cards**: Each card is a link, containing:
  - **Thumbnail image**: Rectangular, no border-radius, no shadow
  - **Title** (h5): Inter, ~18px, weight 600
  - **Source** text: Smaller, muted, serif — e.g., "Will MacAskill at TED"
- **Cards link to**: External resources (TED, 80000 Hours, GiveWell, EA Forum)
- **One card** includes an embedded video play button overlay
- **CTA button below**: "View more resources" — black background, white text, square

### Blockquote / Testimonial Band

- **Layout**: Full content-width, centered text block
- **Quote text**: Large serif italic, ~20px, in quotation marks. Key phrase in `<strong>` bold
- **Attribution**: Below quote, smaller text — "Dr. Rachel Glennerster, Associate Professor at the University of Chicago"
- **Style**: No background, no border — just generous whitespace above and below

### "Find Ways to Help" Section

- **h2**: "Find ways to help" + subtitle paragraph
- **Layout**: 2-row x 3-column card grid (6 action cards)
- **Action cards**: Each card is a link containing:
  - **Thumbnail image**: Rectangular, no border, no shadow
  - **Title** (h5): Inter, ~18px, weight 600
  - **Description**: Serif paragraph, ~16px
- **Cards**: Take a free online course, Read the intro essay, Donate to effective charities, Get career guidance, Join a group, Attend a conference
- **CTA button below**: "More ways to take action" — black background, white text, square

### Pre-Footer Newsletter Band

- **Background**: Same sand `#F4EFE9`
- **Layout**: Centered text + email input + "Sign up" button on one line + "View past editions" link below
- **Text**: "Join 60k subscribers and sign up for the EA Newsletter, a monthly email with the **latest ideas and opportunities**"

---

## Page 2: Take Action (`/take-action`)

### Page Header

- **h1**: "Take action" — Inter, 72px (same as homepage hero h1 but on sand background, black text)
- **No hero image** — just the heading on the sand background with generous whitespace above (~90px from nav)

### Anchor Navigation (TOC)

- **Position**: Directly below the h1
- **Layout**: Vertical list of 5 anchor links (numbered):
  1. Contribute your time
  2. Give to outstanding charities
  3. Connect with others
  4. Start something new
  5. Learn more
- **Style**: Plain black text links, serif, each with a numbered prefix. Clean and minimal — no background, no bullets, no icons

### Section Pattern (repeated 5 times)

Each numbered section follows an identical pattern:

#### Section Header
- **h2**: "1. Contribute your time" (numbered, Inter, 44px, weight 600, -1.2px letter-spacing)
- **Subtitle**: Serif paragraph, 16px, describing the section

#### Resource Card Grid
- **Layout**: 2-column grid (some sections have 3 rows = 6 cards, some fewer)
- **Card structure**: Each card is a link containing:
  - **Thumbnail image**: Rectangular, fills card width, no border-radius, no shadow
  - **Title** (h5): Inter, ~18px, weight 600, black — action-oriented ("Find volunteering, internships, and part-time roles")
  - **Description**: Serif paragraph, 16px, black — explanatory sentence
- **Card style**: No border, no shadow, no background — flat on sand
- **Grid gap**: ~24px between cards

#### Section Divider
- Thin horizontal `<hr>` between each numbered section

### Section Details

**1. Contribute your time** (5 cards):
- Find volunteering/internships, Read career guide, Get 1:1 career advising, Find a high-impact job, Join a talent database

**Between sections 1 and 2**: Newsletter inline CTA band (same as homepage pre-footer)

**2. Give to outstanding charities** (6 cards):
- Best charities 2025, Recommended charities in global health, Top animal welfare charities, Take a pledge to donate, Donate to EA Funds, Discuss effective giving on EA Forum

**3. Connect with others** (5 cards):
- EA Forum, Local group, Attend a conference, Local/online event, Find a mentor at Magnify Mentoring

**4. Start something new** (3 cards):
- Start a high-impact charity, Start an EA group, Seek funding for a high-impact project

**5. Learn more** (6 cards):
- Read the intro, Online intro course, Find a cause, EA Handbook, Books/podcasts/videos, Read best of EA Forum

---

## Page 3: FAQs (`/faqs`)

### Page Header

- **h1**: "Frequently asked questions and common objections" — Inter, 72px (estimated same as other pages), black text on sand background
- **Horizontal rule** below h1
- **Generous whitespace**: ~90px top, ~48px below hr

### FAQ Accordion Section

- **h2**: "FAQ" — Inter, 44px, weight 600
- **Layout**: Vertical list of 12 expandable items
- **Accordion item structure**:
  - **Question** (h6): Inter, ~16px, weight 500, black text, left-aligned
  - **Toggle icon**: "+" character, right-aligned on same row
  - **Separator**: Thin horizontal line between each item
  - **Expanded state**: Content appears below the question as serif body text
- **Items are full content-width** (~1280px max, centered)
- **No indentation**, no icons, no numbering — purely typographic
- **Questions include**:
  - What is effective altruism?
  - How does EA compare different types of 'good'?
  - What if I don't think EA's practical suggestions are effective?
  - Are you saying what I'm doing right now isn't the most effective thing?
  - Does EA only recommend things proven to work?
  - I already pay my taxes. Why should I do more?
  - What if I don't have enough money to donate?
  - Isn't effective altruism obvious?
  - What things are people in the community working on?
  - What difference has the community made so far?
  - Why should I join the community?
  - How do I get involved?

### Section Divider

- Horizontal `<hr>` between FAQ and Objections sections
- Generous whitespace (~64px) above and below

### Objections Accordion Section

- **Header**: h2 "Objections to effective altruism" + serif paragraph explaining that these objections capture important points
- **Layout**: Same accordion pattern, 12 items:
  - Is EA only about making money and donating to charity?
  - Is EA the same as utilitarianism?
  - Does EA neglect systemic change?
  - Would following EA advice lead to resource misallocation?
  - Is EA calculating and impersonal?
  - Is EA too demanding?
  - Doesn't charity start at home?
  - Does charity and aid really work?
  - Does donating just subsidize billionaires?
  - How are the people you're trying to help involved in decision-making?
  - Does EA neglect effective interventions when impact can't be measured?
  - Is the EA community too homogeneous?

### "Question Not Answered" CTA

- **h3**: "Do you have a question not answered here?" — centered, Inter, ~28px, weight 600
- **Button**: "Contact us" with arrow icon — black bg, white text, square (0px radius), centered below heading

### Section Divider

- Another `<hr>` before "What's next?"

### "What's Next?" Section

- **h2**: "What's next?" — centered, Inter, 44px
- **Subtitle**: Centered serif paragraph
- **Layout**: 2-column first row + 1 card below (3 total), or flexible grid
- **Cards**: Same pattern as Take Action resource cards:
  - Read the introduction to effective altruism
  - Books, podcasts, videos and articles
  - Find the best charities
- **CTA button below**: "More ways to take action" — centered, black bg, white text, square

---

## Component Pattern Library (summary)

### 1. Resource Card

Used on: Homepage ("Find ways to help", "Research and ideas"), Take Action (all sections), FAQs ("What's next?")

```
┌─────────────────────────┐
│  [Thumbnail image]      │  ← No border-radius, no shadow
│                         │
├─────────────────────────┤
│  Title (h5, Inter 600)  │  ← 18px, -0.2px letter-spacing
│  Description (serif)    │  ← 16px, Times New Roman
└─────────────────────────┘
     No border, no shadow, no bg
```

### 2. Story Card (Carousel)

Used on: Homepage ("Effective altruism in action")

```
┌─────────────────────────┐
│  [Portrait photo]       │
│     ┌──────┐            │
│     │Watch │            │  ← Badge overlay
│     └──────┘            │
├─────────────────────────┤
│  "Pull quote..." (h6)  │  ← Serif italic, in quotes
│  ─────────────          │  ← Thin <hr>
│  Name (bold)            │
│  Role description       │
└─────────────────────────┘
     No border, no shadow, no bg
```

### 3. Accordion Item

Used on: Homepage ("What the community has achieved"), FAQs (both sections)

```
──────────────────────────────
  Question text (h6)      +   ← Inter 500, "+" right-aligned
──────────────────────────────
  [Expanded content]          ← Serif body text, hidden by default
──────────────────────────────
```

### 4. Action Button

Used on: Hero CTAs, section CTAs, footer

```
┌──────────────────────┐
│  Button text         │  ← Inter 400, 16px, white on black
└──────────────────────┘
  No border-radius (square)
  padding: 12px 24px
  border: 1px solid
  No box-shadow
```

### 5. Newsletter CTA Band

Used on: Homepage (pre-footer), Take Action (between sections 1-2), Footer

```
  Centered text: "Join 60k subscribers..." with bold emphasis
  [Email input] [Sign up button]
  "View past editions" link
```

---

## Overall Aesthetic Summary

- **Editorial / journal feel**: Warm sand background, serif body text, tight sans-serif headings — like a well-designed long-form publication
- **Flat design**: Zero box-shadows, zero gradients, zero rounded corners anywhere
- **Typography-driven hierarchy**: Size, weight, and spacing create all visual structure — no color coding, no iconography in headings
- **Generous whitespace**: 48-90px between sections, cards breathe with 24px gap
- **Restrained color palette**: Sand (#F4EFE9) + black + white + teal (#0C859A) accent only for links
- **Content-first**: No decorative elements, no illustrations — photography and typography carry the entire visual weight
- **Grid patterns**: 2-column and 3-column grids for cards, max-width 1280px centered
- **Interactive elements are minimal**: Accordions use +/- only, carousels use simple arrow buttons, hover states are subtle
