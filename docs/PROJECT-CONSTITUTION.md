# Project Constitution

**Version 1.0**

## Article I — Mission

This Is What Happened exists to preserve and share the stories, photographs, records, and relationships of our family in a form that is welcoming, trustworthy, and built to last. The project shall help family members recognize the people who came before them, understand how lives connect, and contribute what they know without requiring technical expertise.

## Article II — Vision

The project shall become a living family archive: intimate enough to feel like opening a cherished album, clear enough for any relative to explore, and durable enough to pass from one generation to the next. It shall favor meaningful memory over novelty and patient stewardship over rapid expansion.

## Article III — Core Principles

1. **People before features.** Every decision shall serve the family members whose lives are represented and the relatives who visit the archive.
2. **Stories before systems.** Technology shall support the record, never become the subject of the experience.
3. **Clarity before cleverness.** Familiar words, obvious actions, and calm layouts shall take precedence over fashionable interaction patterns.
4. **Care before speed.** Accuracy, dignity, privacy, and review shall take precedence over shipping quickly.
5. **Preservation before reinvention.** Existing material and working behavior shall be protected unless an approved change clearly improves them.
6. **Accessibility by default.** The archive shall be readable, navigable, and useful across ages, abilities, devices, and levels of technical confidence.

## Article IV — Visitor Experience

A visitor shall be able to understand where they are, whose story they are viewing, and what they can do next without instruction. The experience shall feel warm, quiet, legible, and human. Navigation shall use plain language and consistent placement. Reading and viewing family material shall remain the primary activity; controls, decoration, and administrative tools shall not compete with it.

The archive shall work on phones and larger screens, support keyboard use, maintain readable contrast and type, and avoid unnecessary motion, interruption, or cognitive load. No visitor shall be required to understand the project’s software architecture in order to use it.

## Article V — Invisible Software Rule

Software shall remain invisible whenever possible. A successful feature feels like a natural part of the family archive rather than a demonstration of technology. Visitors shall not be exposed to implementation terms, developer controls, raw data, avoidable error messages, or workflow complexity.

When technology must announce itself—for consent, safety, recovery, or an essential instruction—it shall do so briefly, plainly, and respectfully. Technical sophistication is valuable only when it produces a simpler and more dependable human experience.

## Article VI — Grandparent Test

Every visitor-facing change must pass the Grandparent Test: could a grandparent, arriving without coaching, understand what the page is for, read it comfortably, find a person or story, move forward and back, and recover from a mistake without fear?

If the answer is uncertain, the change is not ready. The remedy shall be to simplify the experience, improve its language, strengthen its visual cues, or test it with an appropriate nontechnical visitor—not to add more instructions around a confusing design.

## Article VII — Evidence Standards

The archive shall distinguish verified fact, family recollection, reasonable inference, and unknown information. Names, dates, relationships, quotations, and historical claims shall be supported by the best available evidence and shall retain source information when known. Conflicting accounts shall be preserved and described rather than silently resolved.

Unverified material shall be labeled honestly. Placeholders shall not be presented as facts. Corrections shall be welcomed, reviewed, and recorded with care. The project shall never invent biographical detail to fill a gap, and it shall not use generated material in a way that could be mistaken for an authentic family record.

## Article VIII — Visual Approval Gate

No perceptible visual change is complete on code review alone. Before acceptance, it must be rendered in the actual site and reviewed at representative mobile and desktop sizes. The reviewer shall inspect hierarchy, typography, spacing, imagery, contrast, navigation, overflow, empty states, and the surrounding pages that could be affected.

Approval requires visual evidence, normally screenshots, and explicit confirmation from the project’s Design Authority. Automated checks may support this gate but shall not replace human visual judgment. A change that is technically correct but visually unapproved shall not be merged.

## Article IX — Development Workflow

All work shall begin from the current `main` branch and proceed on a focused branch. Each change shall have a clear purpose, the smallest practical scope, and no unrelated cleanup. Existing behavior shall be understood before it is modified.

Before a pull request is opened, applicable automated checks shall pass, changed experiences shall be exercised directly, and visual changes shall satisfy the Visual Approval Gate. Pull requests shall explain the reason for the change, identify the files and behavior affected, report the checks performed, and disclose limitations or follow-up work. Review and approval shall occur before merge; urgent work is not exempt from documentation or later verification.

## Article X — Design Authority

The project owner is the final Design Authority for the archive. The Design Authority determines the approved visual direction, voice, visitor priorities, and whether a change satisfies the Mission, Visitor Experience, Invisible Software Rule, and Grandparent Test.

Contributors may propose alternatives and shall explain tradeoffs, but they shall not substitute personal preference, framework convention, or implementation convenience for an approved design decision. When direction is ambiguous, preserve the current experience and seek approval before making a perceptible change.

## Article XI — Repository Standards

The repository is the durable record of the project. `main` shall remain stable and releasable. Changes shall be traceable through focused commits and reviewed pull requests. Files shall use clear names and established organization; duplicated implementations, abandoned artifacts, secrets, generated clutter, and unrelated formatting churn shall not be introduced.

Documentation shall describe the system as it exists. Content and assets shall be stored in maintainable, portable formats whenever practical. Dependencies and automation shall be added only when their long-term value exceeds their maintenance cost. Backward compatibility, preservation of family material, and simple recovery shall guide repository decisions.

## Article XII — Stewardship

Stewards hold family material in trust. They shall protect original records, attribution, privacy, dignity, and the ability of future maintainers to understand the archive. Sensitive information shall be collected sparingly and published only with appropriate permission and judgment. Living people shall receive particular care.

Stewardship includes backups, exportability, correction paths, accessible documentation, and orderly transfer of responsibility. No vendor, tool, account, or individual contributor shall become an avoidable single point of failure. Decisions shall be evaluated not only for today’s convenience but for their effect on the archive years from now.

## Article XIII — Amendments

This Constitution may be amended when experience shows that its guidance is incomplete or no longer serves the Mission. An amendment shall be proposed in a dedicated pull request, state the problem and intended effect, identify the articles changed, and receive explicit approval from the project owner.

Amendments shall not be hidden inside feature work. Once approved, the version and ratification record shall be updated, and project practices shall be brought into alignment. Until an amendment is ratified, this Version 1.0 remains controlling.

## Ratification

This Project Constitution, Version 1.0, is ratified as the governing standard for This Is What Happened. All design, content, development, review, and stewardship decisions shall be measured against it.

**Ratified:** July 25, 2026
