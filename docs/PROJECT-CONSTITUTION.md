# This Is What Happened — Project Constitution

## Purpose

**This Is What Happened** is a living family archive: a welcoming place where relatives and future generations can encounter the people, places, work, photographs, voices, and everyday memories that shaped their family.

The experience should feel like opening a well-kept family journal, not operating a database. Technology supports the visit quietly and never becomes the subject of it.

## Vision

A visitor should be able to arrive with no instructions, choose a family or a kind of memory, and begin exploring. Each path should encourage curiosity, preserve context, and make connections across generations without overstating what is known.

The archive grows through careful contributions. New discoveries should deepen existing stories and remain connected to their people, places, sources, and family lines.

## Guiding principles

1. **People and stories come first.** Organize the experience around what visitors want to do—meet relatives, follow journeys, see photographs, hear memories, and share discoveries—not around screens, files, or internal systems.
2. **Mobile is the foundation.** Design first for a small touch screen, readable type, comfortable controls, safe-area spacing, and a clear single-column flow. Larger layouts progressively enhance that foundation.
3. **The machinery stays backstage.** Public language must never expose software terminology, developer notes, implementation details, build messages, debug states, or placeholder copy. When something is unknown, describe the historical uncertainty honestly and humanly.
4. **Preserve what works.** Extend and reorganize working experiences rather than replacing them without cause. Changes should protect photographs, biographies, stories, maps, search, narration, and contribution tools.
5. **Evidence and memory are distinct.** Clearly distinguish documented facts, family memories, interpretations, research leads, and conflicting accounts. An attractive presentation must never turn uncertainty into fact.
6. **Unknown is not empty.** Missing names, dates, and context are invitations to learn more. Present them as open family questions, never as unfinished product work.
7. **One connected archive.** A contribution belongs everywhere it is meaningful. People, places, photographs, stories, livelihoods, and sources should reinforce one another rather than becoming isolated pages.
8. **Welcoming by default.** Use plain, warm language; accessible structure; keyboard and touch support; sufficient contrast; reduced-motion respect; and meaningful labels.
9. **Privacy deserves care.** Treat living people, personal memories, and family materials respectfully. Share only what the family intends to preserve publicly.
10. **Growth should remain maintainable.** Keep family records separate from presentation where practical, reuse experience patterns, and favor small understandable changes that future stewards can continue.

## Visitor experience model

The archive is organized around these visitor intentions:

- **Meet the families** — enter through a family line and follow connected lives.
- **Follow their journeys** — explore the places and movements that shaped those lives.
- **Look through photographs** — browse visual memories and their connections.
- **See how they lived** — learn about work, craft, school, home, and daily life.
- **Hear their stories** — read or listen to remembered moments.
- **Search the collection** — find a known person, place, record, or keepsake.
- **Share a discovery** — preserve new knowledge with its source and uncertainty intact.

These intentions are the durable architecture. Individual views and technologies may change beneath them.

## Content standard

Every public-facing addition should answer three questions:

1. What will a family visitor understand or feel here?
2. Is the wording honest about what is documented, remembered, or still unknown?
3. Does the experience remain clear and useful on a phone without revealing its implementation?

If any answer is unclear, the work is not ready to become part of the public archive.

## Project Workflow

Every significant public-facing feature must complete each of the following stages, in order, before it may be merged into the main branch:

1. **Vision & Requirements** — Define the visitor need, intended outcome, scope, constraints, source material, and acceptance criteria.
2. **Architecture Review** — Confirm how the work fits the visitor experience model, existing content structure, accessibility requirements, mobile-first foundation, and connected archive without unnecessarily removing working functionality.
3. **Visual Design Proposal** — Present the proposed appearance and interaction behavior at representative mobile and desktop sizes before beginning significant public-facing implementation.
4. **Visual Approval Gate** — Obtain explicit approval of the visual design proposal. **No public-facing implementation may begin before this approval is given.** Revisions return to the proposal stage until approved.
5. **Implementation (Codex)** — Build only the approved scope, preserve existing functionality, follow this constitution, and keep implementation details out of the visitor experience.
6. **Code Review** — Review the change for correctness, maintainability, accessibility, responsiveness, regressions, evidence handling, privacy, and consistency with the approved proposal.
7. **Museum Review** — Review the working experience as a public exhibit, with attention to historical care, family-centered language, visual coherence, usability, and the experience of visitors on both mobile and desktop devices.
8. **Merge** — Merge into the main branch only after code review and museum review are complete and all required changes have been addressed.
9. **Release Notes** — Record what visitors can now experience, what existing behavior was preserved, any known limitations, and any follow-up work that remains outside the release.

Skipping, combining, or reordering these stages requires an explicit project-owner decision. Approval of a concept, architecture, or written requirement does not count as visual approval.
