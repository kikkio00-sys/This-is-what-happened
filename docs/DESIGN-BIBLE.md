# This Is What Happened — Design Bible

**Status:** Proposal for Design Authority review

**Phase:** Design Bible / Visual Approval Gate

**Implementation status:** Documentation only; no direction or visual choice in this document is approved for implementation.

Every choice below is a **proposal awaiting explicit project-owner visual approval**. This document establishes a review vocabulary, not permission to alter the site. Candidate designs must still be rendered at representative mobile and desktop sizes, reviewed with visual evidence, and approved under the Project Constitution’s Visual Approval Gate before implementation or acceptance.

## Design Philosophy and Emotional Tone

The archive should feel like four compatible experiences held in balance:

- **A museum exhibit:** composed, contextual, trustworthy, and respectful of original objects.
- **An heirloom scrapbook:** tactile, personal, imperfect in human ways, and made from things a family kept.
- **A premium coffee-table book:** image-led, spacious, beautifully paced, and rewarding to linger over.
- **A family welcome:** warm rather than institutional, plainspoken rather than academic, and never precious at the expense of comprehension.

The proposed emotional sequence is **welcome → recognition → curiosity → connection → confidence**. Visitors should first feel invited, then recognize a person, place, or object, become curious about its story, understand its family connections, and trust how the archive knows what it says.

Technology must recede. Under the **Invisible Software Rule**, the interface should look like an edited family archive rather than a database, dashboard, content-management system, or software demonstration. Under the **Grandparent Test**, a first-time visitor should comfortably answer: “Where am I?”, “Whose story is this?”, and “Where can I go next?” without coaching.

## Visitor-First and Mobile-First Principles

1. Begin with people, stories, photographs, and familiar family language—not tools or archive structure.
2. Design the phone experience first as the complete experience, not a reduced desktop site.
3. Give each screen one clear subject and one obvious next action.
4. Keep reading order linear and meaningful; enhancements must not be required to understand content.
5. Prefer visible labels over unexplained icons, hover behavior, gestures, or hidden menus.
6. Preserve orientation with a page title, a plain-language return path, and consistent navigation.
7. Make tap targets forgiving and text comfortable for older eyes; never require precision.
8. Reveal evidence beside the claim it supports while keeping the main story calm and readable.
9. Treat slow connections, missing images, incomplete records, and long names as normal conditions.
10. Do not expose implementation concepts. The archive’s internal model must translate into ordinary family language.

## Proposed Color Palette

All colors and pairings are **proposals awaiting approval** and must receive contrast testing in rendered contexts.

| Role | Proposed color | Hex | Intended use |
|---|---|---:|---|
| Archive Paper | warm ivory | `#F6F0E4` | Primary page ground |
| Cotton White | soft white | `#FFFDF8` | Reading surfaces and photograph mats |
| Walnut Ink | deep brown-black | `#2B2521` | Primary text and strong rules |
| Sepia Ink | muted brown | `#68584B` | Secondary text and captions |
| Oxblood | restrained burgundy | `#7A342F` | Primary actions, active states, key accents |
| Oxblood Dark | dark burgundy | `#54231F` | Hover/focus reinforcement on light grounds |
| Heritage Blue | subdued blue | `#3F6272` | Links, places, and informational accents |
| Sage Cloth | quiet green | `#77806A` | Collection markers and supporting accents |
| Brass | aged gold | `#A77B3F` | Fine decorative details only, never body text |
| Faded Rose | dusty blush | `#C99D93` | Sparing family or relationship accents |
| Rule | parchment gray | `#D8CDBD` | Dividers, borders, and document edges |
| Evidence Wash | pale blue-gray | `#E8EEF0` | Source and evidence callouts |
| Caution Wash | pale ochre | `#F3E5C5` | Uncertain or conflicting information |

Color must never carry meaning alone. Walnut Ink on Archive Paper is the default long-reading combination. Cotton White provides contained reading contrast without stark digital white. Accent colors should occupy a small minority of each page; family material remains the visual focus.

## Typography Hierarchy

Typography is proposed as an editorial pairing, subject to font licensing, performance, glyph, and accessibility review:

- **Display and story headings:** a warm, sturdy old-style serif such as Source Serif 4. It should suggest a well-made book without imitation handwriting or decorative nostalgia.
- **Body copy:** the same serif for long narrative reading, with generous leading and a comfortable measure.
- **Navigation, labels, captions, dates, and controls:** a highly legible humanist sans serif such as Source Sans 3.
- **Transcriptions and archival identifiers:** the sans serif, not a typewriter novelty face; original handwriting appears only in authentic document imagery.

Proposed mobile scale:

| Level | Size / line height | Use |
|---|---|---|
| Display | `2.25rem / 1.08` | Person or homepage title |
| H1 | `2rem / 1.12` | Primary page heading |
| H2 | `1.5rem / 1.2` | Major story section |
| H3 | `1.1875rem / 1.3` | Subsection or card heading |
| Lead | `1.1875rem / 1.55` | Opening summary |
| Body | `1.0625rem / 1.65` | Narrative text |
| UI | `1rem / 1.4` | Navigation and buttons |
| Caption | `0.9375rem / 1.45` | Image and source context |

Desktop display headings may grow fluidly up to approximately `4.5rem`, but body text should remain near `1.125rem` and 60–72 characters per line. Use true italics sparingly for titles or gentle emphasis. Avoid all-caps sentences; small labels may use modest letterspacing and title case.

## Spacing and Layout System

Use a proposed **4 px base unit** with a practical spacing sequence of `4, 8, 12, 16, 24, 32, 48, 64, 96` px. Repeated relationships should be predictable:

- 8–12 px between a label and its title.
- 16 px within compact controls or metadata groups.
- 24 px within cards on mobile.
- 32–48 px between related content groups.
- 64–96 px between major story chapters.

Mobile pages use 20 px side gutters, expanding to 24 px on larger phones. The primary narrative column should be no wider than 720 px. Desktop layouts may sit within a 1280 px maximum canvas with 48–80 px gutters and a 12-column grid, while story text retains its narrower measure. Full-bleed imagery must be intentional and must return the eye to an aligned reading edge.

Whitespace should communicate editing and care, not emptiness. Borders, shadows, torn edges, tape, and paper layers must not all compete at once.

## Navigation Patterns

- A calm site header proposes three primary destinations: **People**, **Places**, and **Collections**, plus a clearly labeled **Search** action if search is available.
- On phones, show the archive name, one obvious **Menu** control, and the current page context. The opened menu should be a straightforward vertical list, not icon-only navigation.
- Use a plain return path such as **All people** or **Back to the Downing family**, rather than technical breadcrumbs. When deeper hierarchy is useful, breadcrumbs remain short and readable.
- Within a long person page, a compact **On this page** list appears near the introduction. It should use ordinary section names and standard anchor behavior.
- Previous/next links should name their destinations: **Next story: Early years**, not merely “Next.”
- Browser Back must remain dependable. No navigation should unexpectedly replace history or trap focus.
- Persistent navigation is optional, not assumed. If proposed later, it must not obscure content or create a software-toolbar feeling.

## Cards and Content Containers

Cards are editorial entry points, not dashboard widgets. Proposed card types are limited to:

- **Person card:** portrait, full name, lifespan when known, and one human line of context.
- **Story card:** strong image or document detail, story title, short invitation, and subject names.
- **Place card:** place photograph/map detail, plain place name, and its family connection.
- **Collection card:** representative image, collection title, and a concise description of what is inside.
- **Evidence note:** a visually quieter container tied to a nearby fact or passage.

Use warm paper surfaces, restrained 1 px rules, modest corner radii (proposed 4–8 px), and either no shadow or a very soft physical lift. Entire clickable cards must have a visible focus state and a textual link cue. Avoid nested cards, dense metadata, status chips, counts as the dominant feature, or equal-weight grids that erase narrative priority.

## Buttons and Links

- Primary buttons propose Oxblood fill with Cotton White text; secondary buttons use a transparent ground, Walnut Ink text, and a clear border.
- Buttons use verbs and objects: **Read William’s story**, **View the family map**, **See the original record**.
- Inline links use Heritage Blue, remain underlined, and have distinct hover and focus treatment.
- Minimum target size is 44 × 44 px, with 48 px preferred for principal mobile actions.
- Focus indicators must be clearly visible and not depend on browser color alone; a proposed 3 px contrasting outline with offset is preferred.
- Disabled actions should be rare. If an action is unavailable, explain in human language rather than presenting a mysterious inactive control.
- No text disguised as a button and no button disguised as ordinary text.

## Photography Treatment

Photographs are family records first and design material second.

- Preserve original aspect ratio and avoid cropping faces, handwriting, dates, borders, or contextual details.
- Use a respectful Cotton White mat or a quiet full-width presentation. One strong image is preferable to a decorative collage of many small images.
- Supply a concise caption identifying people, approximate date, place, and contributor/source when known. Clearly label uncertainty.
- Do not colorize, “restore,” generate, or materially alter an image without explicit disclosure and approval. Never imply an altered image is the original.
- Minor display adjustments may be proposed only when the original remains preserved and accessible.
- Missing photographs receive dignified text, not generic silhouettes that could be mistaken for a person.
- Galleries should be keyboard operable, swipe-independent, and accompanied by visible controls and position context.

## Historical-Document Treatment

Documents should feel like carefully mounted exhibit objects, not background texture.

- Show the complete object first whenever possible, followed by optional detail views.
- Provide a readable transcription adjacent to or immediately after the image on mobile; desktop may pair image and transcription while preserving logical reading order.
- Identify document type, date, creator/issuing body, repository or custodian, and archive reference when known.
- Separate verbatim transcription from editorial notes. Mark illegible text, supplied words, and uncertain readings consistently.
- Do not manufacture stains, torn paper, handwriting, seals, or “aged” effects.
- Zoom is an enhancement; essential information must remain available without precision gestures.

## Family-Map Presentation

“Family map” proposes a relationship-focused orientation experience, not a technical genealogy chart.

- Begin with recognizable portraits and names around a clearly stated family or generation.
- Express relationships in words—**daughter of**, **married to**, **their children**—in addition to lines or position.
- On mobile, use a guided vertical sequence of family groups with visible **View their story** links; do not require horizontal panning.
- On desktop, a broader connected arrangement may use gentle relationship lines, but every person must remain reachable by keyboard and understandable without interpreting line color.
- Offer a simple **Start with…** choice or highlighted family group rather than presenting the whole lineage at once.
- Distinguish known, uncertain, adoptive, step, and other family relationships accurately and respectfully, using words chosen with the family and never visual hierarchy that implies lesser belonging.

## Timeline Presentation

A timeline supports a life story; it does not replace it.

- Use a vertical chronological spine on mobile, with year/date, human event title, short context, and optional image.
- Organize dense lives into named eras such as **Early years**, **Family and work**, and **Later life**, avoiding a wall of dates.
- On desktop, retain a readable vertical narrative or a two-column date-and-story rhythm. Do not default to a horizontally draggable strip.
- Clearly distinguish exact dates, approximate dates, ranges, recollections, and disputed dates in words.
- Connect personal events to wider history only when relevant and sourced; family experience remains primary.
- Provide stable anchors for major eras if the timeline is long.

## Collections and Places

Collections are curated rooms, not file folders. Each collection opens with an editorial introduction: what it contains, why it matters, who assembled it, and any known gaps. A representative object leads; filters or counts remain secondary and use visitor language.

Places explain why geography matters to this family. A place page proposes a clear place name, a present/historical location note, a lead image or simple map, associated people, and stories or records connected to it. Maps must be supplements, with equivalent text lists and no requirement to pinch, drag, or understand pins. Historical and current place names should coexist when both are relevant.

## Evidence and Citation Presentation

Evidence should build trust without turning the archive into database software.

- Place a restrained source marker after the supported sentence or paragraph; selecting it moves to a plainly written source note.
- Group full source notes under **Sources and family records**, ordered to match the story rather than by internal identifier.
- Label knowledge as **Documented**, **Family recollection**, **Likely**, **Date uncertain**, or **Accounts differ**, with a one-sentence explanation when needed.
- When accounts conflict, present both respectfully, state their sources, and do not force false certainty.
- A source note proposes: human-readable title, creator, date, repository/custodian, relevant page or item, contributor, and access details as applicable.
- Keep archive identifiers available but visually subordinate. Never expose raw filenames, database keys, JSON, ingest status, or editorial workflow to visitors.
- Corrections invite care: **Do you know more about this? Share a correction or memory.** The language must not imply that an unreviewed submission immediately becomes fact.

## Motion and Interaction

Motion is quiet, optional, and functional.

- Prefer immediate state changes. If transitions aid orientation, keep them around 150–250 ms using simple opacity or small positional changes.
- Honor `prefers-reduced-motion` by removing nonessential animation and smooth scrolling.
- Never use parallax, scroll-jacking, autoplaying slideshows, animated counters, ambient movement, or surprise audio/video.
- Do not hide essential content behind hover. Hover may reinforce a control that is already visible.
- Expand/collapse controls must state what they reveal, expose their state to assistive technology, and preserve focus.
- Loading and error states use calm, plain language and keep recovery obvious.

## Accessibility

Proposed designs target WCAG 2.2 AA at minimum and treat accessibility as part of visual approval.

- Use semantic headings, landmarks, lists, buttons, links, figures, captions, and tables.
- Maintain at least 4.5:1 contrast for normal text and 3:1 for large text and essential interface graphics; verify actual rendered combinations.
- Support keyboard-only navigation with logical order, visible focus, skip navigation, and no traps.
- Provide useful alternative text based on the image’s role; avoid duplicating adjacent captions. Decorative imagery should be ignored by assistive technology.
- Do not place meaningful text only inside images. Provide full transcriptions for historical documents.
- Allow text to resize to 200% and pages to reflow at 320 CSS px without two-dimensional scrolling except truly essential content, for which an equivalent view is required.
- Use plain language, descriptive link text, large targets, generous line spacing, and persistent labels.
- Respect reduced-motion, high-contrast, forced-colors, and user font/zoom preferences where supported.
- Captions and transcripts are required for time-based media. Never autoplay sound.

## Mobile Behavior

- Content follows a single meaningful column with 20–24 px gutters.
- The opening viewport communicates archive identity, page subject, and an inviting next step without requiring a hero image to load.
- Navigation uses a labeled menu and familiar close control; the page title remains clear after navigation opens.
- Cards stack with image, title, context, then action. Important information is not reordered visually away from document order.
- Photographs may extend toward the viewport edge, while text returns to the reading gutter.
- Document image and transcription stack; family maps become guided groups; timelines stay vertical; place maps have immediate text equivalents.
- Long names wrap naturally. Controls never rely on side-by-side space that disappears in translation or zoom.
- Avoid sticky elements that consume limited height. No essential action sits beneath a device safe area.

## Desktop Adaptations

Desktop adds breathing room and comparison, not complexity.

- Use the wider canvas for editorial pairings: portrait with introduction, document with transcription, place image with context.
- Keep the primary story at a readable measure and use side columns only for genuinely related material such as a caption, date, or section navigation.
- Allow selective asymmetry reminiscent of a designed book spread while preserving clear reading order.
- Family connections may broaden spatially; collections may use two- or three-column compositions with one clear lead item.
- Hover treatment is supplementary. All actions remain visible and usable by keyboard and touch-capable desktop devices.
- Do not fill space with extra controls, metadata, or decorative objects merely because room exists.

## Print Rules

Printed pages should become durable family reading copies.

- Use a white background, near-black text, and remove navigation, menus, decorative backgrounds, shadows, motion, and interactive-only controls.
- Preserve the archive title, page title, story text, captions, evidence labels, full source notes, and a modest canonical page address where available.
- Print photographs and documents at useful scale without splitting them from captions when practical; never crop originals for print decoration.
- Avoid orphaned headings and prevent short cards or evidence notes from breaking across pages where possible.
- Expand essential collapsed content and print link destinations when useful, without cluttering ordinary prose links.
- Use print-appropriate margins and page-break rules; do not emulate aged paper through ink-heavy backgrounds.
- Clearly mark approximate, uncertain, or conflicting information in text so meaning survives grayscale printing.

## Prohibited Visual Patterns

The following are proposed as prohibited because they conflict with the Constitution:

- Dashboard layouts, admin panels, database tables as the primary visitor experience, analytics-style charts, and exposed system metadata.
- Generic “family tree” clip art, faux heraldry, wax seals, quills, typewriters, or themed nostalgia without authentic relevance.
- Artificial paper damage, fake tape everywhere, heavy sepia filters, forced film grain, and decorative handwriting fonts for ordinary text.
- Carousels, autoplay, parallax, scroll-jacking, infinite scroll, surprise modals, newsletter pop-ups, and gamified engagement.
- Icon-only primary navigation, mystery-meat controls, hover-only disclosure, hidden gestures, and horizontal mobile timelines or trees.
- Tiny type, low-contrast beige-on-beige text, text over busy photographs, excessive all caps, and justified body text with uneven gaps.
- Dense card walls, nested cards, badge collections, pill overload, status colors without words, and counts that overwhelm stories.
- Cropped faces, colorized or generated “historical” images presented as authentic, and decorative use of sensitive records.
- Visual hierarchy that ranks relatives’ worth or treats incomplete records as errors.
- Any perceptible implementation that has not passed representative mobile/desktop review and explicit Design Authority approval.

## Prohibited Visitor-Facing Language

Visitor copy must not expose systems or make family members feel like records to process. Avoid:

- **Technical/system language:** “database,” “record ID,” “entity,” “node,” “schema,” “dataset,” “asset,” “ingest,” “sync,” “query,” “API,” “CMS,” “backend,” “frontend,” “404,” “null,” or “invalid payload.”
- **Administrative language:** “manage profile,” “edit entity,” “submit ticket,” “moderation queue,” “workflow status,” or “user permissions.”
- **Cold commands:** “execute search,” “return to index,” “view record,” “drill down,” “load more data,” or “click here.”
- **False certainty:** “proven” when evidence is partial, “unknown” when “not yet documented” is more accurate, or silently definitive relationship/date language where accounts differ.
- **Possessive or reductive labels:** “the deceased,” “subjects,” “data points,” “maiden name” as the only identity framing, or language that reduces people to lineage function.
- **Blaming errors:** “You entered invalid information,” “user error,” or “failed request.” Prefer a calm explanation and recovery, such as **We couldn’t open that page. Return to People.**
- **Promotional language:** “engage,” “unlock,” “discover amazing content,” “trending,” “exclusive,” or urgency tactics.

Prefer **People**, **Stories**, **Family map**, **Places**, **Collections**, **Sources and family records**, **What we know**, **What family remembers**, **Accounts differ**, and **Help us learn more**. Exact language remains a proposal awaiting approval and content review.

# Homepage Visual Direction

The following are three distinct, unselected proposals. **None is the approved homepage direction.** Each awaits rendered mobile and desktop studies, Visual Approval Gate review, and explicit project-owner approval. In particular, the **Heirloom Journal** proposal does not approve, adopt, validate, alter, or merge PR #11 or any prior journal design.

## Direction A — Family Map as the Invitation

### Mobile structure

1. Compact archive masthead and labeled menu.
2. Welcome statement: **Every family has a way in. Start with someone you know.**
3. A vertical series of 3–5 family groups anchored by portraits and relationship words.
4. A clear **See the whole family map** action.
5. One featured story, then concise entrances to Places and Collections.
6. Stewardship/source reassurance and footer navigation.

The “map” is a guided vertical path, never a tiny desktop tree squeezed onto a phone.

### Desktop structure

A generous opening canvas pairs a short welcome with a composed constellation of family portraits. Restrained lines and explicit relationship labels connect a limited number of entry points. Below, an editorial row features a story, place, and collection, followed by orientation text. The complete lineage is not placed above the fold.

### Opening experience

A visitor recognizes a face or name immediately and understands that the archive is organized through relationships. One person is visually emphasized only as a suggested starting point, not as the family’s most important member.

### Navigation

Primary navigation remains People, Places, Collections, and Search. Portrait/name links move directly to stories. A labeled **How everyone connects** action opens the fuller family map. Return links name the family group.

### Imagery

Portraits are the principal imagery, presented with consistent mats but preserved aspect ratios. Missing portraits use names and short relationship context, never invented silhouettes. A small number of authentic documents or place images appear below the relational opening.

### Typography

The serif display voice gives the family name and invitation a book-like presence. Sans-serif relationship phrases create clarity around the more expressive portrait composition.

### Interaction

On mobile, visitors scroll and select ordinary links. On desktop, focus or hover may gently emphasize a person and their immediate relationships, but the relationship text is always present and all connections remain comprehensible without interaction or color.

### Strengths

- Offers an immediate answer to “How am I connected?”
- Makes people the primary navigation and can prompt recognition across generations.
- Establishes the archive’s distinctive family purpose without relying on software language.
- Creates natural routes into individual stories.

### Risks

- Relationship complexity could overwhelm first-time visitors.
- A spatial layout can become inaccessible, cramped, or falsely hierarchical.
- Portrait availability may unevenly represent branches of the family.
- Maintaining accurate relationships demands especially careful evidence and privacy review.

### How it satisfies the Constitution

It proposes people before features, plain relationship language, accessible mobile groups, and visible story destinations. It supports the Grandparent Test through recognition and named actions, and the Invisible Software Rule by presenting family connections rather than graph controls. It satisfies the Evidence Standards only if uncertain relationships are explicitly labeled. It remains subject to the Visual Approval Gate.

## Direction B — Heirloom Journal

### Mobile structure

1. Quiet masthead and menu.
2. One full-width archival photograph with caption.
3. A short editorial welcome and **Begin with this story** action.
4. A paced sequence of story excerpts alternating photographs, documents, and text.
5. Small, clear entrances to People, Places, and Collections.
6. Source/stewardship note and footer.

### Desktop structure

The page reads as a series of premium book spreads: a strong photograph paired with a welcome, a document detail paired with a story excerpt, and a restrained grid of further chapters. A narrow central rhythm holds the page together; asymmetry is used sparingly, never at the expense of reading order.

### Opening experience

The visitor feels they have opened a carefully kept family volume at a meaningful page. The opening is intimate and editorial: one image, one short passage, and one obvious invitation rather than a complete directory.

### Navigation

The persistent site vocabulary remains familiar, while the content path uses **Begin the story**, **Meet the family**, and **Continue reading**. An **Explore another way** group leads to People, Places, and Collections without hiding those routes.

### Imagery

Large authentic photographs, album pages, letters, and document details provide pacing. Captions and object context remain attached. Scrapbook qualities come from genuine objects and measured layering, not fake paper effects, stock ephemera, or decorative clutter.

### Typography

Expressive but highly legible serif headlines and generous body copy create the journal rhythm. A clear sans serif distinguishes captions, navigation, dates, and evidence notes. No simulated handwriting is proposed.

### Interaction

Primarily vertical reading with standard links. Optional details may reveal a transcription or photograph context through accessible disclosure controls. There is no page-turn gimmick, dragging, autoplay, or scroll-controlled animation.

### Strengths

- Best expresses warmth, memory, and premium coffee-table-book pacing.
- Allows stories and original artifacts to lead together.
- Can welcome visitors without requiring prior understanding of the family structure.
- Scales naturally into seasonal or editorially curated openings.

### Risks

- Editorial curation may obscure a straightforward route to a particular person.
- Decorative enthusiasm could drift into faux nostalgia or visual clutter.
- A long opening could bury navigation or make the homepage feel like one person’s page.
- This name could be mistaken for approval of earlier journal work; it explicitly is not.

### How it satisfies the Constitution

It places stories before systems and uses authentic family material to keep software invisible. Clear navigation and a single reading path support the Grandparent Test. Evidence remains attached to artifacts, and accessibility prevents the “book” metaphor from becoming a page-turn interface. This is a fresh conceptual proposal only; PR #11’s journal design is not treated as approved, and any future interpretation requires explicit Visual Approval Gate approval.

## Direction C — Family Portrait Gallery

### Mobile structure

1. Archive title, plain welcome, and menu.
2. One featured portrait and short invitation.
3. A two-column portrait gallery that becomes one column at narrow/zoomed widths.
4. Each portrait includes the person’s full name and one relationship/story cue.
5. **Can’t find someone? View all people** followed by Places and Collections.
6. Featured family photograph, stewardship note, and footer.

### Desktop structure

A museum-wall composition presents one large featured portrait beside a varied but orderly gallery of smaller portraits. Names are always visible. Below, a calm editorial band offers a family photograph, a place, and a collection so the homepage does not imply that portraits are the archive’s only material.

### Opening experience

Visitors enter a room of faces. Recognition and curiosity happen before explanation; a brief statement makes clear that each portrait opens a life story and that every documented family member belongs in the archive.

### Navigation

People is the strongest route, with equally visible Places and Collections in the header. Gallery entries are direct named links. Alphabetical and family-group options may appear after **View all people**, not as a control-heavy homepage toolbar.

### Imagery

Portraits receive quiet, gallery-like mats with their original framing respected. Different photograph ages and qualities are allowed to show. People without photographs receive typographic name panels with an honest invitation to learn their story, preventing photographic survival from determining importance.

### Typography

The archive title and featured story use the serif display face. Names and relationship cues use a direct sans serif for scanability. Labels resemble museum captions in restraint, not in institutional jargon.

### Interaction

Selecting a portrait opens the person’s story. Hover/focus may reveal or emphasize an already-present story cue on desktop; mobile never depends on it. No masonry reflow surprises, face zoom effects, filters above the fold, or animated gallery walls.

### Strengths

- Passes the recognition test quickly and makes the archive feel human.
- Offers direct, obvious links with minimal explanation.
- Creates a museum exhibit feeling from authentic family material.
- Accommodates a growing archive through a clear route to the full People index.

### Risks

- Uneven portrait availability can privilege well-photographed relatives or eras.
- A wall of faces can feel repetitive, overwhelming, or memorial rather than living.
- Cropping pressure can compromise original images.
- Relationship context is less immediately visible than in the Family Map direction.

### How it satisfies the Constitution

It leads with people, recognizable faces, visible names, and simple actions. The absence of gallery tricks supports the Invisible Software Rule; large labeled targets support the Grandparent Test. Honest no-photo states, inclusive prominence, and captions support evidence and stewardship. Representative mobile/desktop gallery studies and explicit Design Authority approval remain mandatory.

## Direction Review Questions

The Design Authority’s review should compare—not yet select—the directions using these questions:

1. Which opening helps a first-time relative understand the archive fastest?
2. Which provides the warmest invitation without obscuring People, Places, or Collections?
3. Which treats branches, generations, living people, and missing photographs most fairly?
4. Which can remain simple with substantially more stories and records?
5. Which best balances museum exhibit, heirloom scrapbook, and coffee-table book qualities?
6. Which most clearly passes the Grandparent Test in rendered phone and desktop studies?
7. What must change before any direction is approved for implementation?

# William Alfred Downing Visual Concept

**Status:** Unimplemented concept and proposal awaiting explicit project-owner visual approval. This section does not authorize an ancestor-page build, select a homepage direction, establish facts about William Alfred Downing, or permit placeholder biography. Content may enter a future page only after evidence and privacy review.

## Mobile Page Structure

The proposed mobile reading order is:

1. Archive masthead and a plain return link such as **All people** or the approved family-group name.
2. William Alfred Downing’s full name, verified lifespan or carefully qualified dates, and one evidence-based identifying line.
3. Portrait/hero figure with complete caption and source.
4. Short, sourced opening narrative answering who he was and why his story matters.
5. **On this page:** Story, Photographs, Life timeline, Family records, People, and Places—only including sections that have substantive content.
6. Story chapters in chronological or thematic sequence.
7. Photographs placed near the life passages they illuminate.
8. Vertical life timeline.
9. Historical documents with transcriptions and evidence notes.
10. Related people and related places.
11. Full **Sources and family records**.
12. Named previous/next routes and site footer.

The single-column order is the canonical content order. No essential relationship, source, or navigation depends on a side panel.

## Desktop Page Structure

The proposed desktop opening resembles a composed book spread: portrait on one side; name, dates, identifying line, and opening narrative on the other. After the opening, the story occupies a restrained central column. Photographs and brief evidence notes may sit in adjacent columns when they directly support the nearby passage.

Major chapters use generous separation. A quiet **On this page** rail may remain beside the narrative only if it does not resemble application navigation, obscure content, or create keyboard confusion. Documents may pair with transcriptions. Related people and places form an editorial closing spread rather than a dashboard of relations.

## Portrait or Hero Treatment

If an authenticated portrait exists and permission allows its use, show it without dramatic crop, colorization, artificial restoration, or decorative effects. Preserve edges and contextual marks when meaningful. A quiet Cotton White mat, generous surrounding space, full caption, approximate date, identified people, contributor/custodian, and uncertainty language are proposed.

If no verified portrait exists, lead with the name and an authentic associated object, place, or document only when its relationship to William is evidenced. Never substitute a generic man, generated likeness, silhouette, or unlabeled group crop. The absence of a portrait should feel like an honest archival gap, not an interface error.

## Story Hierarchy

The future narrative proposes three layers:

- **Opening:** a short, readable account of who William was, grounded only in supported facts.
- **Life chapters:** a small number of meaningful headings based on the evidence actually available—not a predetermined template that invents completeness.
- **Context and evidence:** family recollections, historical context, uncertainty, and citations placed near the relevant passage.

Headings should use human subjects such as **Early years in [place]** or **The family remembers**, not database categories such as “Vital events.” Verified facts, recollections, inferences, and unknowns must remain visibly distinct.

## Photographs

Photographs should appear at the moment they deepen the story rather than in a detached media dump. Each figure proposes the full image first, a plain caption, named people where known, date/place qualification, and source or contributor. A small gallery may collect additional views after the narrative, with keyboard controls and visible position labels.

Group photographs should identify William’s position using caption language or a separate, clearly disclosed reference aid; do not permanently mark the original. Unknown people remain honestly labeled **Not yet identified** with an invitation to share knowledge.

## Life Timeline

A concise vertical timeline proposes dated milestones that help orient the longer story. Each entry includes a date or honest qualifier, a human event title, one or two contextual sentences, and a source marker. Events may be grouped into evidence-led eras. Personal milestones should not be overwhelmed by generic world history.

On desktop, dates may occupy a narrow left column and narratives a right column while maintaining linear reading order. No draggable horizontal timeline, animated travel path, or unsourced gap-filling is proposed.

## Evidence and Sources

Source markers should appear beside supported claims and lead to corresponding notes under **Sources and family records**. The notes use human-readable titles before repository codes. Proposed evidence labels include **Documented**, **Family recollection**, **Likely**, **Date uncertain**, and **Accounts differ**.

A brief **What we know** note may explain an important conflict or limitation without interrupting the story. Conflicting evidence remains visible and attributed. Raw internal filenames, record keys, confidence scores, editorial status, and empty fields never appear to visitors.

## Historical Documents

Relevant records—such as certificates, registers, letters, clippings, or military/work records—may appear only when authenticated, appropriate to publish, and connected to the nearby narrative. Each document presentation proposes:

1. Complete-object image.
2. Object title and contextual caption.
3. Accessible transcription.
4. Editorial note only where needed to interpret handwriting or context.
5. Repository/custodian, reference, date, and contributor information.

The display must distinguish original text from archive commentary and must never fabricate missing portions or decorative document effects.

## Related People

A small closing group proposes 3–6 people whose relationships are supported and whose stories offer a natural continuation. Each entry includes portrait if available, full name, relationship in words, and a specific action such as **Read Mary’s story**. Selection should explain William’s life, not rank relatives or maximize clicks.

A separate **See how the family connects** route may lead to the approved family-map experience. Uncertain or complex relationships receive explicit, respectful wording; living relatives require privacy care.

## Related Places

Related places should be limited to locations that materially shaped William’s documented story. Each entry proposes the historical/current place name, its connection to him, one authentic image or map detail when available, and **Explore [place]**. If geography is useful, pair a simple map with an equivalent text list. Avoid decorative pins, speculative routes, and precise sensitive locations.

## Page Navigation

- A plain return link appears before the title.
- An **On this page** list offers stable anchors to substantive sections.
- Long sections may end with **Back to page sections**, not a floating utility widget.
- Related links name the person, place, or story they open.
- The closing offers a clear return to People and one or two evidence-based next stories.
- Navigation placement and vocabulary remain consistent with the eventual approved homepage system.
- No tabs, hidden side drawers, app-style command bar, or ancestor-tree pan/zoom is proposed.

## Intended Emotional Experience

The visitor should first meet William as a person, not a row of facts. The portrait or authentic object creates presence; the opening narrative creates recognition; photographs and places create texture; the timeline creates orientation; and visible evidence creates earned trust. By the close, a relative should feel both closer to his life and confident about what is documented, remembered, uncertain, or still missing.

The proposed page should feel dignified without becoming solemn, intimate without inventing familiarity, and authoritative without becoming institutional. It should invite the next family conversation: **This is what we know. This is what the family remembers. What can you add?** Its software should be nearly unnoticeable, and its path should remain simple enough to pass the Grandparent Test.

## Approval Boundary and Next Step

No concept in this Design Bible is final. The next permitted design step, after document review, is to prepare static visual studies or rendered prototypes for the project owner’s review at representative mobile and desktop sizes. Those studies must demonstrate hierarchy, typography, spacing, imagery, contrast, navigation, overflow, empty states, accessibility, and neighboring-page implications. Implementation—including a homepage or William Alfred Downing ancestor page—must not begin until the Design Authority explicitly approves a visual direction under the Constitution’s Visual Approval Gate.
