# Changelog

All notable changes to this repository are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Version numbers follow rule G-07.

## [Unreleased]

### Added

- Three sections in `general/` that carry the lifecycle past release: 27 on acceptance and delivery (`ACC`), 28 on operations (`OPS`) and 29 on support periods and retirement (`EOL`). Section 18.1 now continues to delivery, running and retirement. Section 28 says which rules apply depending on who runs the software, and that AI agents hold no write access to production or site equipment.
- `hmi/` B.13 on factory and site acceptance (`IND-43` to `IND-47`), with a pointer from `vision/`.
- New MUST rules: 6 in `ACC`, 15 in `OPS` (`OPS-14` is tier L only), 6 in `EOL`, and `IND-44` to `IND-46` (`IND-45` applies at every tier). The others are for tier M and above, and public releases with no recipient are outside section 27.
- Playbooks for delivery, incidents and retirement, checklists 26.3 and 26.4, definition of done 23.4, templates `runbook.md` and `acceptance-record.md`, and a support policy line in the README and release note templates and in the release checklists.
- Glossary terms for runbook, incident, alert, deployment rollback, FAT, SAT, RTO, RPO and retirement, and a references row for operations and delivery.
- Section 24 of `general/` lists how the new MUST rules are checked.
- Section 7 gains a data inventory with legal basis, retention and deletion, minimal collection and data classification (`DAT-08` to `DAT-11`), a definition of personal data and customer data, and a table of what applies depending on who holds the data. Section 6.12 covers cryptography (`SEC-35` to `SEC-42`). Sections 19.5 to 19.7 cover data sent to external models, products that call a model, and the tools and memory agents use (`AI-18` to `AI-27`). Section 3 gains concurrency rules (`CODE-15` to `CODE-20`), with `TST-12` for testing them and a line in each language annex.
- These add 18 MUST rules: `DAT-08`, `DAT-10`, `SEC-35` to `SEC-39`, `SEC-41`, `AI-18`, `AI-21` to `AI-24`, `AI-26` and `CODE-15` to `CODE-18`. `DAT-08`, `DAT-10`, `SEC-41`, `AI-26` and `CODE-18` are for tier M and above; the others have no tier mark. An MCP service returning project content to a client the user configured is outside `AI-18` and `AI-21`, as section 19.5 and `mcp/README.md` say.
- Playbooks, the review checklists, T.3, T.8, checklist 26.3, the acceptance record, section 24, glossary terms for personal data, customer data and anonymization, and references rows for cryptography and AI security follow these rules.

### Changed

- Minimum list item 13 now also covers sending credentials and customer data to external models.
- `MIG-05` and `DSK-07` now require the updater to check the publisher's signature as well as the hash, with the signing key kept off the update server. A hash fetched from the same channel does not stop an attacker who controls that channel.
- `SEC-16` and `PRO-19` say constant-time comparison instead of fixed-length comparison, which was the wrong term.
- Section 13.1 now counts a running service or production line stopped by the software as S1, and S1 response starts with recovery.
- `mcp/` is now draft 0.2 and is designed as a standard that projects follow. A rule's level depends on what goes wrong when the rule is broken, as `mcp/README.md` now defines. A project that cannot comply registers a deviation. Levels may still change while the part is a draft.
- Raised to MUST: `PRO-02`, `TL-05`, `TL-06`, `TL-08`, `TL-18`, `TL-26`, `TL-34`, `WS-05`, `WS-06`, `WS-12`, `WS-15`, `WS-25`, `WS-35`, `WS-37`, `WS-39`, `WS-41`, `WS-43`, `ENG-06`, `ENG-09`, `ENG-10`, `ENG-22` and `VER-05`.
- Lowered: `VER-01` to SHOULD and `WS-40` to MAY. The next-step wording of `TL-31` moved to the new SHOULD rule `TL-43`.
- New rules: `WS-44` and `ENG-26` (MUST), `PRO-24`, `TL-40`, `TL-41`, `TL-42` and `TL-43` (SHOULD).
- `WS-15` and `WS-16` now limit the approval off-switch and throwaway projects to ordinary writes. Destructive, code-running, system and online-device operations, shared data and paths outside the root always need approval.
- `PRO-12` says what a re-issued write returns, `PRO-13` says nothing more is sent after a cancel, and `WS-17` defines `partial` and `unknown` for batches.
- Rules no longer offer alternatives or wording for services already published. How to adopt with published names or an older MCP revision is now in one place in `mcp/README.md`.
- `mcp/README.md` lists the rules that are explicit exceptions to `general/` and `desktop/`.
- `TL-14` requires an object schema root without `oneOf`, `anyOf` or `allOf`, and `TL-15` keeps mutually exclusive parameters in the description with validation on the server.
- `handbook-mapping.md` corrected against the 1.1 text, including level changes it did not state.
- The status column in `README.md` now shows only the version, and the sentence about where the rules came from is gone.
- `vision/` and `dashboard/` are now draft 0.2 and use the same approach: each file defines how levels are chosen, and a rule is MUST when breaking it directly has one of those consequences and no other MUST already prevents it. They were all SHOULD before. `vision/` has 32 MUST of 42 rules and `dashboard/` has 20 MUST of 28.
- Rules in `vision/` that bundled an end with a means are split, and the means stay SHOULD: `VIS-32` and `VIS-37` to `VIS-42`, plus `DSH-26` in `dashboard/`.
- New MUST rules in `vision/`: `VIS-35` (recipe matches the product, camera parameters read back), `VIS-36` (bypass needs permission, audit and a time limit) and `VIS-43` (production PC setup). `VIS-33` and `VIS-34` now require an OK-image policy and an alarm when the NG rate or score distribution moves. `VIS-24` stays SHOULD.
- `VIS-11` no longer lets replayed results reach the PLC or the formal records, `VIS-20` covers a result that never arrives at the PLC, `VIS-27` stops judging after a count mismatch, `VIS-23` forbids retesting until a part passes, and `VIS-28` asks for a confidence bound on the escape rate.
- `vision/README.md` states explicit exceptions to `P-04`, `SEC-03`, `ERR-08` and `IND-17` for writes at line speed, and a tier line.
- New MUST rules in `dashboard/`: `DSH-24` (metric definitions), `DSH-25` (alarms during carousel), `DSH-27` (long-lived front ends reload) and `DSH-28` (mock data). `DSH-04` is now MUST. `DSH-08` takes the data time from the source, not from a cache, and keeps judging staleness during a disconnect. `DSH-15` no longer means leaving a machine unpatched, `DSH-19` covers credential renewal, and `DSH-10` requires one-way flow through an isolation zone only when the display is outside the production network.
- `dashboard/README.md` lets a showroom screen treat `DSH-11`, `DSH-23`, `DSH-24` and `DSH-25` as SHOULD, and states exceptions for credentials and desktop heartbeats.
- The release checklists of `vision/` and `dashboard/`, and `templates/release-checklist.md`, gained items for the new runtime rules.
- Section 24 of `general/` says the runtime MUST rules of `vision/` and `dashboard/` are checked through their release checklists and the rest in review.
- The roadmap in `README.md` now says each draft is tried on a new project before 1.0.

### Removed

- The labels in `mcp/` that recorded how far existing projects implemented each rule. `[规范]` stays, because it marks rules that come from the MCP specification.

## [2.0] - 2026-11-05

First version meant for publication. `general/`, `hmi/`, `desktop/`, `web/` and `mobile/` are 2.0; `mcp/`, `vision/` and `dashboard/` are drafts at 0.1. The major version changes because domains A and C were replaced and the scope of some MUST rules narrowed.

### Added

- Draft 0.1 of a dedicated MCP standard under `mcp/` for services that connect to engineering software and can write to real projects. It targets MCP 2026-07-28, marks the evidence behind each rule, and maps every rule from the earlier domains A and C.
- Draft 0.1 of `vision/` for machine vision software and `dashboard/` for large data displays. All their rules are suggestions that no project has validated yet.
- `desktop/local-software.md` for software that runs on a user's or site machine.

### Changed

- The repository is now one `general/` folder for all projects plus one folder per project type: `mcp/`, `hmi/`, `vision/`, `dashboard/`, `desktop/`, `web/` and `mobile/`. Rules that moved keep their ids; the former `MCP-` and `VND-` rules have new ids in `mcp/`.
- Windows, packaging, diagnostics and the desktop UI values moved from the general part to `desktop/`, along with the local pipe and HTTP rules, DAT-02, DAT-03, DAT-05, DAT-06, SEC-26, CFG-04 and MIG-05. They assumed software on the user's machine and conflicted with web projects.
- WIN-12, WIN-14, PKG-07 and PKG-08 moved the other way, into `general/`, because every project needs them.
- Project-type rules now take precedence over the general part when the two conflict, but they do not loosen a MUST elsewhere unless they say so.
- Section 0.1 now says that the confirm-before-write and unknown-outcome rules apply to writes started by automation or AI and to writes to target software and devices, not to a user saving in their own interface.
- SEC-19 now covers server-side secret stores as well as the Windows user store, and CFG-03 limits local network listening to software on a user's machine.
- References now point at MCP 2026-07-28.
- FAST-04 now applies when AI agents are used, so a team without them does not break a MUST.
- Section 0.1 says an equivalent on another platform is not an exception and needs no ADR. Section 0.3 explains why rule numbers have gaps.

### Removed

- The text of domains A and C, replaced by `mcp/`. `mcp/handbook-mapping.md` lists where each rule went and what changed.

## [1.1] - 2026-11-02

The date is that of the handbook text. The repository files were added on 2026-11-04.

### Added

- Handbook 1.1 as Markdown under `handbook/`, one file per top-level section.
- Fill-in templates under `templates/`: task spec, architecture decision record, review checklist, definition of done, release checklist and project adoption file.
- `README.md` and `LICENSE` (CC BY 4.0).

### Changed

Compared with handbook 1.0:

- Slimmed the rules: MUST rules went from 456 to 150 and each now carries a one-line reason; the rest became SHOULD, or were merged or removed (491 rules to 396 in total).
- The UI chapter now gives general defaults (row height 36 or 44 per product, undo and approval rules, no access keys on approval buttons); a project records its own trade-offs in its ADRs.
- The merge gate target is about 15–20 minutes; a project may set a stricter one.
- The enforcement table is rewritten around the MUST rules.

Changes made when the handbook moved from one HTML file to this repository. They are part of 1.1 as first added to this repository, not a separate release, and no rule id, level or tier changed:

- The desktop token reference in the UI chapter now points at the tokens listed in that chapter.
- A few examples became generic, and the wording about where the change record lives follows the new file layout.
- Section 0.1 now says that some rules are written for Windows and .NET, and that other platforms use an equivalent.
- Subsections 6.4, 9.7, 19.3 and 20.3 had no text and now point at the rules that cover them.
- Template T.1, the minimum list and section 25 now use one term for a profile, as the glossary does.
- SBOM is marked M+ in the playbooks and, with provenance, in section 26.1 and the release checklist template, as rule DEP-11 and section 23.3 already said.
- The directory tree in section 2.6 now includes `docs/plan` and `docs/postmortems`, which rules DOC-11 and BUG-06 name.
- Section 6.11 now points at rule DSK-08 for signing, because section 14.1 has no signing rule.
