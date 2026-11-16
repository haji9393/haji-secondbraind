---
name: "Phong cách slide deck Insider"
description: "Hệ thống hình ảnh slide deck của Insider: layout, motif, icon, connector và quy ước placeholder khi dựng file .pptx."
group: Marketing
---

# Insider Deck Style

## Khi nào dùng

Insider's slide-deck visual system - layouts, motifs, icon treatments, connector styles, and placeholder conventions observed from Insider template slides. Use whenever building a .pptx for Insider or in an Insider-branded context. Pair with insider-brand-guidelines for colors and typography.

## Overview

A deck-specific style guide extracted from Insider template slides. It complements `insider-brand-guidelines` (colors, typography; that skill is NOT installed in this Javis brain) by documenting the layouts, motifs, and components that make a slide look and feel like Insider.

**Keywords**: Insider, deck, slides, presentation, style, layout, motif, template, pptx, Insider One

## Foundation

Colors and typography come from `insider-brand-guidelines`. That skill is not installed in this Javis brain, so treat the summary below as the source of truth and ask the user for any value it does not cover:

- **Background**: Nova `#EFEBE4` (cream) - nearly every slide
- **Primary text**: Eclipse `#261A28` or Dark Matter `#18181B`
- **Primary accent**: Solar `#F4482B` - use sparingly but with conviction (dots, circles, emphasis words, decorative motifs)
- **Soft accent**: Cosmic `#F0CABF` - translucent shapes, overlays
- **Typography**: **Barlow** (Preferred for Vietnamese support) or Poppins (International). Barlow handles Vietnamese diacritics with better alignment and legibility.

Insider decks feel airy and editorial, yet data-rich. The style relies on:

1. **Structured Content Density.** For Business Reviews (QBRs), slides should be comprehensive, including specific campaign IDs, exact metrics (volume, CR%, revenue), and regional insights.
2. **Massive whitespace.** Even with high density, slides must breathe. Balance text-heavy columns with clear margins and Solar accents.
2. **Thin lines, small dots.** Connectors are 0.75–1pt black lines ending in 6–8pt filled dots. Dividers are single hairlines.
3. **Solar as a point accent.** Orange appears as dots, filled circles, emphasis words, dotted trails, and the organic "blob" motif - not as large filled blocks of color.
4. **Playful organic shape on the left.** A curvy Solar "blob" bleeding in from the edge is a brand-defining hero element, especially on agenda/section/cover slides.

## Layout Grid

- Canvas: 13.333" × 7.5" (`LAYOUT_WIDE`)
- Outer margin: 0.6" minimum on all sides
- Column gutters: 0.3"–0.5"
- Title block: top 1.2"–1.8" of slide, left-aligned
- Placeholder logo: bottom-right at ~(11.5, 7.0), small uppercase

## Core Motifs

### 1. Solar Circle Icon Marker

A small filled Solar circle (~0.55" diameter) containing a white monoline icon (most common: arrow-up-right / "launch"). Used as the bullet for column headers, steps, or feature callouts.

```
┌─────────────┐
│    ●  ↗     │  (Solar fill, white icon)
└─────────────┘
```

```js
// pptxgenjs pattern
slide.addShape(pres.ShapeType.oval, {
  x: 1.0, y: 2.0, w: 0.55, h: 0.55,
  fill: { color: "F4482B" }, line: { color: "F4482B", width: 0 },
});
// White arrow-up-right placed over the circle via Unicode or an SVG path/image.
slide.addText("↗", {
  x: 1.0, y: 2.0, w: 0.55, h: 0.55,
  fontSize: 22, bold: true, color: "FFFFFF",
  align: "center", valign: "middle", fontFace: "Barlow",
});
```

### 2. Line-and-Dot Callout

A thin horizontal black line ending in a small filled dot, pointing from a target (circle, shape, or chart element) to an adjacent label. The label is two lines: bold term on top, supporting sentence below in regular weight.

Use 0.75–1pt line, 6–8pt filled dot in Eclipse/Dark Matter.

```js
slide.addShape(pres.ShapeType.line, {
  x: 7.0, y: 2.0, w: 1.3, h: 0,
  line: { color: "261A28", width: 1 },
});
slide.addShape(pres.ShapeType.oval, {
  x: 6.92, y: 1.92, w: 0.15, h: 0.15,
  fill: { color: "261A28" }, line: { color: "261A28", width: 0 },
});
slide.addText([
  { text: "Integration\n", options: { bold: true, fontSize: 18, color: "261A28" } },
  { text: "Easy integration with Tag Managers and shopping cars",
    options: { fontSize: 13, color: "261A28" } },
], { x: 8.4, y: 1.7, w: 3.5, h: 1.0, fontFace: "barlow" });
```

### 3. Target / Bullseye Marker

A Solar dot wrapped in two concentric Solar outline rings to mark the "current" or highlighted step on a timeline. Inner dot ~0.2", ring 1 ~0.45", ring 2 ~0.7".

```js
const cx = 6.5, cy = 4.0;
[0.7, 0.45].forEach(d => {
  slide.addShape(pres.ShapeType.oval, {
    x: cx - d/2, y: cy - d/2, w: d, h: d,
    fill: { type: "none" },
    line: { color: "F4482B", width: 1.5 },
  });
});
slide.addShape(pres.ShapeType.oval, {
  x: cx - 0.1, y: cy - 0.1, w: 0.2, h: 0.2,
  fill: { color: "F4482B" }, line: { color: "F4482B", width: 0 },
});
```

### 4. Dotted Solar Trail

A horizontal dotted line in Solar connecting a row of Solar step-dots. This is the backbone of the Insider timeline layout.

```js
slide.addShape(pres.ShapeType.line, {
  x: 1.0, y: 4.0, w: 11.3, h: 0,
  line: { color: "F4482B", width: 2, dashType: "dash" },
});
// Then place 7 evenly-spaced Solar dots on top.
```

### 5. White Rounded Pill Callout

An elevated white pill containing label text, connected to its target by a dashed vertical line. Radius ~0.1", soft drop shadow.

```js
slide.addShape(pres.ShapeType.roundRect, {
  x: 5.5, y: 2.2, w: 3.0, h: 0.6, rectRadius: 0.1,
  fill: { color: "FFFFFF" }, line: { color: "FFFFFF", width: 0 },
  shadow: { type: "outer", color: "000000", opacity: 0.12,
            blur: 12, offset: 2, angle: 90 },
});
slide.addText("Approve & launch campaign", {
  x: 5.5, y: 2.2, w: 3.0, h: 0.6,
  fontSize: 13, fontFace: "barlow", color: "261A28",
  align: "center", valign: "middle",
});
```

### 6. Curved Bracket Connector

A swooping bracket below the timeline that gathers the row of steps into a central trunk leading to the Insider One (or partner) logo. Visually it reads as "all these steps power this brand." Usually built from two curved-connector shapes meeting at a center point.

### 7. Organic Solar Blob

A large curvy, liquid Solar shape that bleeds off the left edge of the slide, most often on **agenda / section / cover** slides. Organic, not geometric - think lava lamp, not circle. Covers roughly the lower-left quadrant, leaving the top-left open for the page title.

Implementation options:
- Pre-export the blob as a PNG with transparent background and add via `slide.addImage`. (Recommended - organic shapes are hard to get right with pptxgenjs freeform paths.)
- Approximate with 2–3 overlapping ovals of varying sizes blended together in Solar.

### 8. Translucent Overlapping Circles

Venn / intersection visuals use 3 circles with `~30% alpha` Solar / Cosmic fills so overlaps create darker color mixes naturally.

```js
const circle = (x, y, d, alpha) => slide.addShape(pres.ShapeType.oval, {
  x, y, w: d, h: d,
  fill: { color: "F4482B", transparency: alpha },  // transparency = 100 - alpha%
  line: { color: "F4482B", width: 0 },
});
circle(6.5, 1.4, 3.2, 60); // top - lighter
circle(5.0, 3.5, 3.2, 25); // lower-left - darker (the "hero" circle)
circle(7.5, 3.5, 3.2, 55); // lower-right - lighter
```

### 9. Mixed-Color Emphasis Titles

Titles alternate Solar orange and Eclipse dark on key words to guide the reader's eye: `"Take Control of Your Campaigns & Execute with Ease"` → "Take Control" (Solar), "of Your Campaigns &" (Eclipse), "Execute" (Solar), "with Ease" (Eclipse).

```js
slide.addText([
  { text: "Take Control ",            options: { color: "F4482B" } },
  { text: "of Your Campaigns & ",     options: { color: "261A28" } },
  { text: "Execute ",                 options: { color: "F4482B" } },
  { text: "with Ease",                options: { color: "261A28" } },
], { x: 0.7, y: 0.6, w: 12, h: 0.9,
     fontSize: 34, fontFace: "barlow", bold: false });
```

### 10. Thin Column Dividers

Vertical 0.5pt lines in Lunar `#D0C2C7` separating columns; optionally a thin horizontal rule under column headers. Never use boxed/filled cards on content slides - the grid is implied, not drawn.

## Placeholder Convention

Insider templates use angle-bracket placeholders in the bottom-right corner for third-party logos:

- `<INSERT CUSTOMER LOGO>` - when the deck is pitched to a specific customer
- `<INSERT PARTNER LOGO>` - when co-branded with a partner

Styling: ~10pt, Poppins bold, Eclipse color, letter-spacing +1, positioned at (11.3, 7.05), 1.7" wide.

```js
slide.addText("<INSERT CUSTOMER LOGO>", {
  x: 11.2, y: 7.05, w: 1.9, h: 0.3,
  fontSize: 10, fontFace: "barlow", bold: true, color: "261A28",
  charSpacing: 1.5, align: "right",
});
```

## Standard Slide Recipes

### Recipe A - Agenda / Section Divider

- Left: organic Solar blob bleeding off the edge
- Left top: section title ("Agenda", "Part 2", etc.) - very large (~72pt), Eclipse
- Right: list of items, each with a thin divider line; left-aligned label + right-aligned page reference ("Your heading goes here" ... "Slide 16")
- Section headers in list are bold Eclipse, same font size as sub-items (~18–20pt) but heavier

### Recipe B - Concept Diagram (Venn / Radial)

- Title top-left, bold, ~36pt Eclipse
- Centered composition on right 60% of slide: 3 translucent Solar/Cosmic circles with an obvious dominant circle
- Line-and-dot callouts to external labels (bold term + supporting sentence)
- Placeholder logo bottom-right

### Recipe C - Horizontal Timeline

- Title full-width top, mixed-color emphasis
- Dotted Solar trail with 5–7 Solar dots
- One dot marked with the target/bullseye rings
- Labels below each dot (short, Eclipse, regular weight)
- Optional dashed vertical connector from highlighted dot up to a white pill callout
- Curved bracket below timeline feeding to Insider One logo
- Placeholder logo bottom-right

### Recipe D - 4-Column Feature Grid

- Title top-left, bold ~36pt Eclipse
- 4 columns separated by thin Lunar vertical lines
- Each column starts with a Solar circle + white icon
- Column header (bold, ~20pt Eclipse, 2 lines max)
- Optional bullet list below with Solar-dot bullets (or leave columns empty as editable placeholders)
- Placeholder logo bottom-right

### Recipe E - Icon Row

- Title optional
- 4 columns, each with a large black monochrome icon (~0.8–1.0") centered under a bold header
- Thin horizontal rule between header row and icons
- Minimal text - icons carry the meaning

## Dos and Don'ts

**Do**
- Keep ~60% of every slide empty
- Limit Solar to dots, circles, emphasis words, and the one blob per section
- Use Poppins (or approximate) for everything and vary weight + size rather than swapping fonts
- Left-align titles and body; only center text inside small UI elements (pills, circle icons)
- Let thin lines and small dots carry the structure instead of boxes

**Don't**
- Fill entire slides with Solar or Eclipse - the cream background is the hero
- Use drop-shadows or gradients on content (only on the pill callout, subtly)
- Box every content group in a card - Insider relies on whitespace and lines
- Use more than one organic blob per slide
- Underline titles or add horizontal accent bars beneath them - Insider never does this
- Mix accent colors from outside the Insider palette on deck slides

## Working with pptxgenjs

Set defaults up front to keep code consistent with the system:

```js
const INSIDER = {
  nova:      "EFEBE4",
  eclipse:   "261A28",
  darkMatter:"18181B",
  solar:     "F4482B",
  cosmic:    "F0CABF",
  lunar:     "D0C2C7",
  stardust:  "CFEBDD",
};
const FONT_HEAD = "Barlow"; 
const FONT_BODY = "Barlow"; // Use Barlow for robust Vietnamese character support

function styledSlide(pres) {
  const s = pres.addSlide();
  s.background = { color: INSIDER.nova };
  return s;
}

function placeholderLogo(slide, text = "<INSERT CUSTOMER LOGO>") {
  slide.addText(text, {
    x: 11.2, y: 7.05, w: 1.9, h: 0.3,
    fontSize: 10, fontFace: FONT_HEAD, bold: true,
    color: INSIDER.eclipse, charSpacing: 1.5, align: "right",
  });
}
```

## QA Checklist

Before shipping an Insider-branded deck:

- Background is Nova, not pure white
- At most one "loud" visual element per slide
- Solar appears but does not dominate
- No unboxed content is floating - align to the left edge or center on the content axis
- Every slide has the bottom-right placeholder (or real logo)
- Titles are left-aligned, bold-free titles use weight ≥ 400, bold titles use weight ≥ 600
- Mixed-color titles only when there's a reason (emphasis makes the line scannable)
- No accent underlines, no emoji decoration, no stock-photo drop-ins
