# Project Constitution

## Status and authority

This constitution is the permanent governing document for **This Is What Happened**. It defines why the project exists, whom it serves, how its records are treated, and the workflow required for every significant change. Product, design, editorial, and engineering decisions must conform to it. When speed or convenience conflicts with this constitution, the constitution takes priority.

The project owner is the final decision-maker. Any exception to this constitution must be explicit, documented, and limited to the decision for which it was granted.

## Project purpose and long-term vision

This Is What Happened exists to preserve and share the stories of real people so that families, friends, and future generations can encounter lives as they were experienced—not merely as names, dates, or files. It is a living family museum: intimate, durable, understandable, and worthy of the people whose memories it holds.

The long-term vision is a trustworthy, multigenerational home for photographs, voices, documents, relationships, and recollections. It should remain approachable as its collection grows, survive changes in technology, and make each visitor feel welcomed into a human story rather than presented with a software product. Longevity, dignity, clarity, and emotional truth matter more than novelty, feature count, or technical display.

## Visitor-first and mobile-first principles

The project is **visitor-first**. Decisions begin with what helps a visitor understand where they are, whose story they are seeing, and how to continue without instruction. Navigation must be calm and obvious; language must be plain; accessibility, readability, performance, and emotional context are core requirements. Internal architecture and contributor convenience must never be exposed as burdens for visitors.

The project is **mobile-first**. The smallest supported screen and touch interaction are the starting point for information hierarchy, design, implementation, and review—not a reduced version addressed after desktop work. Essential content and actions must work without hover, precision pointing, wide layouts, or high bandwidth. Larger screens may enrich the experience but may not define it.

## Stories and people before software

People are not content units, and their lives are not demonstrations for technology. Stories, relationships, context, and dignity come before components, frameworks, automation, visual effects, or engineering cleverness. The software must serve the collection quietly.

Every feature must answer a human need: whose story becomes clearer, what relationship becomes understandable, what memory becomes safer, or what visitor becomes better able to participate? If that answer is weak, the feature should not be built. The project must not manufacture engagement, gamify remembrance, flatten a person into metadata, or privilege what is easiest to encode over what is meaningful to preserve.

## Evidence versus memory

The project respects both documentary evidence and remembered experience, but it does not confuse them.

- **Evidence** includes sourceable records such as photographs, letters, certificates, clippings, recordings, and other documents. Provenance should be retained whenever known. Transcription, cropping, restoration, and other alteration must not silently change meaning.
- **Memory** includes personal recollection, family tradition, interpretation, and stories passed between people. Memory may be partial, subjective, conflicting, or uncertain and remains valuable when honestly presented as memory.
- A claim must not be presented as verified fact merely because it is repeated or confidently remembered. Uncertainty, disagreement, estimated dates, unknown authorship, and missing context must be stated plainly.
- The interface must not create false authority. Labels, captions, structure, or generated summaries must preserve the distinction between a documented fact, an editorial inference, and a contributor's recollection.
- Corrections should preserve an accountable history when practical. New evidence may refine the record without erasing the fact that a different memory existed.

Trust is more important than neatness. When the record is incomplete, the project says so.

## The Invisible Software Rule

Software should be felt as care, not noticed as machinery. This is the **Invisible Software Rule**: technology must recede so that the visitor encounters people, stories, and artifacts first.

Interfaces must avoid unnecessary controls, product jargon, dashboards, novelty interactions, conspicuous automation, and decoration that competes with the collection. Motion, transitions, media treatment, and navigation are justified only when they improve comprehension, orientation, accessibility, or emotional continuity. A visitor should not need to understand the data model or admire the implementation in order to understand a life.

Invisible does not mean careless or simplistic. It requires robust accessibility, resilient performance, clear recovery from errors, respectful privacy, and maintainable systems behind a quiet experience.

## The Visual Approval Gate

Visual direction is a project-owner decision, not an implementation side effect. **No significant public-facing implementation may begin before explicit visual approval from the project owner.** Approval must be based on a concrete visual proposal at appropriate mobile and larger-screen sizes, with enough fidelity to judge hierarchy, typography, spacing, imagery, navigation, states, and overall emotional character.

Written descriptions, wireframes, code experiments, or developer preference do not substitute for approval unless the project owner explicitly says they do. Approval of one screen, component, or direction does not imply approval of materially different work. If implementation reveals a substantial visual departure, work returns to the Visual Design Proposal and Visual Approval Gate before continuing.

## Permanent project workflow

Every significant project change follows these nine stages in order. **Stages cannot be skipped, combined, or reordered without an explicit project-owner decision.** Reviews must produce a clear outcome, and unresolved issues return the work to the appropriate earlier stage.

### 1. Vision & Requirements

Define the human purpose of the change, the visitors and stories it serves, its scope, constraints, accessibility and mobile needs, evidence or editorial implications, and clear acceptance criteria. Identify what is deliberately out of scope. No solution should be selected before the need is understood.

### 2. Architecture Review

Assess how the proposal fits the existing information architecture, content model, navigation, privacy expectations, accessibility obligations, performance goals, and technical foundation. Prefer durable, comprehensible structures and the smallest system that meets the approved requirements. Record consequential tradeoffs before visual design or implementation.

### 3. Visual Design Proposal

Prepare a concrete proposal showing the intended visitor experience. Include representative content, mobile-first layouts, relevant larger-screen layouts, important interaction states, and sufficient visual detail for an informed decision. The proposal must demonstrate the visitor-first principles, the priority of stories and people, and the Invisible Software Rule.

### 4. Visual Approval Gate

Present the visual proposal to the project owner and obtain explicit approval, requested revisions, or rejection. Approval must be unambiguous and recorded. No significant public-facing implementation may begin until approval is granted. Material changes after approval must return to this gate.

### 5. Implementation

Build only the approved scope and visual direction. Preserve content integrity, provenance, accessibility, responsive behavior, performance, privacy, and maintainability. Do not introduce speculative features or redesign approved behavior through code. Validate on mobile first and then across the supported experience.

### 6. Code Review

Review correctness, security, accessibility, performance, maintainability, test coverage, content safety, and fidelity to the approved requirements and visual proposal. Code review is not authorization to change product or visual direction. Findings must be resolved or explicitly accepted before proceeding.

### 7. Museum Review

Review the completed experience as a steward and visitor rather than only as a developer. Confirm that people remain central, stories retain context and dignity, evidence and memory are represented honestly, artifacts are treated responsibly, navigation feels natural, and the software remains invisible. Verify the experience with representative content and on a real mobile-sized viewport.

### 8. Merge

Merge only after all prior stages have clear approval and required checks pass. The merged change must match the reviewed scope, contain no unrelated work, and leave the primary branch in a releasable state. Merge is a controlled record of an approved decision, not merely the end of coding.

### 9. Release Notes

Document what changed, why it changed, whom it serves, and any known limitations, migrations, editorial considerations, or follow-up work. Use visitor-centered language and distinguish public changes from internal maintenance. Release notes complete the workflow and preserve decision context for future stewards.

## Stewardship

This constitution should evolve rarely and deliberately. Proposed amendments must explain the need, preserve the project's human purpose, and receive explicit project-owner approval through the same disciplined workflow. The existence of new technology, pressure to ship, or an attractive design trend is not by itself a reason to weaken these commitments.
