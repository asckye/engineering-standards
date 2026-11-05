# Changelog

All notable changes to this repository are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Version numbers follow rule G-07.

## [Unreleased]

### Added

- The standard is now a set of Agent Skills and a Claude Code plugin. There is one skill per part, each with a `SKILL.md` that holds a task table saying which file to read, and the rules stay in that skill's `references/`.
- A minimum list in the `SKILL.md` of each project type, with the MUST rules that prevent the worst failures for that kind of project. It is an entry point and changes no level.
- `evals/`: test cases for the skills, in the layout `claude plugin eval` reads.
- `build-tools/check_standards.py` checks internal links, rule ids, reason lines, section 24, version strings, the checklists copied into templates, the skills and plugin manifests, and line endings, and that no MUST was lowered since the last tag of the same major version. It has tests and runs in CI on every push to `main`. Scripts are under the MIT licence.

### Changed

- Files moved: `general/` to `skills/general-engineering-standard/references/`, `templates/` to its `assets/`, and each project-type folder to `skills/<skill>/references/`. A part's `README.md` is now `rules.md`, or `overview.md` for MCP and `contents.md` for the general part. `mcp/templates/` moved to that skill's `assets/`, and `general/00a-minimum.md` is now the general `SKILL.md`. Rule ids, rule text and levels did not change.
- Small tools have their own shape in the golden path and the new-project playbook: one source file, one test file and a README. For an S-tier tool only the maintainer uses and does not publish, section 0.2 gives two conditional exceptions: `DOC-06` when there are no other users, and `P-14` when there are no logs, child processes, plugins or communication layers. This narrows two MUST rules for those tools only, so under G-07 it needs a new major version.

## [2.1] - 2026-11-05

`general/`, `hmi/`, `desktop/`, `web/` and `mobile/` are 2.1; `mcp/`, `vision/` and `dashboard/` are drafts at 0.2. In the 2.1 parts, every MUST rule in 2.0 is still a MUST with the same id. In the drafts, whose levels may still change, `mcp/` lowers four MUST rules, listed under Changed. This is a minor version under rule G-07 because rules were added or raised. Three changes narrow what a 2.0 MUST covered and are listed under Changed: tier S, the real-target and pre-release test layers and `TST-05`, and site records and `SEC-22`. Each resolves a conflict or an unclear scope in the 2.0 text, so we do not treat them as lowering a MUST.

For a project following 2.0, this release adds 56 MUST rules and raises 21 rules to MUST in the 2.1 parts. Rules on delivery, operations, support and retirement mostly apply from tier M and only to projects with a recipient or software that keeps running.

### Added

- Three sections in `general/` that carry the lifecycle past release: 27 on acceptance and delivery (`ACC`), 28 on operations (`OPS`) and 29 on support periods and retirement (`EOL`, and `SUP` for user support). Section 18.1 now continues to delivery, running and retirement. Section 28 says which rules apply depending on who runs the software, and that AI agents hold no write access to production or site equipment.
- `hmi/` B.13 on factory and site acceptance (`IND-43` to `IND-47`), with a pointer from `vision/`.
- Section 7 gains a data inventory with legal basis, retention and deletion, minimal collection and data classification (`DAT-08` to `DAT-11`), definitions of personal data and customer data, and a table of what applies depending on who holds the data.
- Section 6.12 covers cryptography (`SEC-35` to `SEC-42`), 6.13 multi-factor sign-in and least-privilege release tokens (`SEC-43`), and 6.14 an assessment against the EU Cyber Resilience Act with compliance where it applies (`SEC-44`). Branch protection is `GIT-08`.
- Sections 19.5 to 19.7 cover data sent to external models, products that call a model, and the tools and memory agents use (`AI-18` to `AI-27`). An MCP service returning project content to a client the user configured is outside `AI-18` and `AI-21`.
- Section 3 gains concurrency rules (`CODE-15` to `CODE-20`), with `TST-12` for testing them and a line in each language annex.
- Requirements and planning: non-functional requirements (`REQ-03`) and estimates and committed dates (`PLN-01`).
- Tests: upgrade tests with data from the previous release (`TST-13`), performance baselines (`TST-14`), fuzzing of parsers (`TST-15`), a decision not to set a global coverage target (`TST-16`) and automated accessibility checks (`UI-38`). Section 12.1 and 15.1 gain a pre-release layer.
- Dependencies: an upgrade rhythm and support end dates (`DEP-12`), a waiting period for new releases (`DEP-13`) and CI components pinned to references that cannot be rewritten (`DEP-14`).
- Release: staged rollout including configuration and models (`BLD-11`), a stated recovery route when an upgrade cannot be undone (`BLD-12`) and hardened release builds (`BLD-13`).
- Section 0.7 defines one level criterion for the whole standard, by the consequence of breaking a rule, and `G-12` applies it to new rules and level changes.
- `ERR-22` and `UI-39` split the serious part out of `ERR-12` and `UI-21` as MUST rules. `MOB-17` and `MOB-18` take what stays SHOULD from `MOB-11` and `MOB-12`.
- `general/appendix/standards-mapping.md` maps the standard against NIST SSDF and the Cyber Resilience Act, says where coverage is partial or missing, and gives steps to decide whether the Act applies.
- Playbooks for delivery, incidents and retirement, checklists 26.3 and 26.4, definition of done 23.4, templates `runbook.md` and `acceptance-record.md`, a non-functional field in the requirement template, a support policy line in the README and release note templates, new glossary terms and references rows.

### Changed

**`general/`, `desktop/`, `hmi/`, `web/` and `mobile/`**

- Raised to MUST: `G-05`, `ERR-13`, `ERR-16`, `ARC-05`, `ARC-14`, `SEC-06`, `SEC-08`, `SEC-09`, `SEC-13`, `SEC-15`, `SEC-24`, `TST-09`, `IND-16`, `IND-20`, `IND-30`, `IND-34`, `IND-40`, `WEB-03`, `WEB-23`, `MOB-11` and `MOB-12`.
- Some were narrowed so they can be followed at that level: `ARC-05` covers a project's own protocols where versions can differ, and asks for identity and a nonce only where impersonation matters; `ARC-14` leaves out heartbeats and listed line-speed writes; `ERR-16` covers writes; `SEC-09` covers the user's existing files and makes a new empty directory the default; `SEC-13` covers commands a model, an outside request or project data can trigger; `SEC-15` requires the firewall sources in the documents, set by a person; `SEC-24` covers text going to a model or an approval screen; `IND-16` covers operator writes; `IND-40` is tier M and above; `WEB-03` requires full WCAG 2.2 AA for public products or where law requires it; `MOB-11` keeps only notification content.
- Tier S: sections 0.2 and 0.3 disagreed. 0.2 and `G-01` said S takes only the minimum list, golden path and playbooks, and 0.3 said untiered rules bind every tier. This release follows 0.2, so untiered rules, including MUST rules, are default practice at S and no longer bind there. A project that writes to real devices, real engineering projects or production data, stores or sends out other people's personal data, or serves others is not tier S and starts at M. We treat this as resolving a contradiction, not as lowering a MUST.
- Section 12.1 says the real-target and pre-release layers are not limited by the one-second rule in `TST-05`, and `OPS-02` says site records kept by the operator are not documents under `SEC-22`.
- `SEC-01`, `SEC-12`, `SEC-14`, `SEC-19`, `SEC-29`, `SEC-30`, `CFG-04`, `PKG-01` and section 0.1 are written in a platform-neutral way, and the language annexes hold the specific tools. `SEC-14` now covers Unix domain sockets. On .NET Framework, which has no `ArgumentList`, L1 allows one central escaping function for `Arguments` under `SEC-12`.
- The nightly check is now called the full check. A project with no nightly job runs it before a release on the commit being released, and it still blocks the release.
- `BLD-07` adds building from a clean checkout of the commit being released, which the tag points to, and `PKG-07` adds debug entry points.
- `MIG-05` and `DSK-07` require the updater to check the publisher's signature as well as the hash, with the signing key kept off the update server. A hash fetched from the same channel does not stop an attacker who controls that channel.
- Section 13.1 counts a running service or production line stopped by the software as S1, and S1 response starts with recovery. `ACC-01` says changes to accepted criteria also need the recipient's agreement. Minimum list item 13 also covers sending credentials and customer data to external models. `DEP-01` and `REV-07` check package names and publishers.
- `G-07` says raising a level is a minor version and that levels in a draft may still change. The conflict notes in `hmi/README.md` are no longer marked as suggestions, and the status column in `README.md` shows only the version.

**`mcp/`, now draft 0.2**

- The standard is designed so that projects follow it. A project that cannot comply registers a deviation. How to adopt with published names or an older MCP revision is in one place in `mcp/README.md`.
- Raised to MUST: `PRO-02`, `TL-05`, `TL-06`, `TL-08`, `TL-18`, `TL-26`, `TL-34`, `WS-05`, `WS-06`, `WS-15`, `WS-25`, `WS-37`, `WS-39`, `WS-41`, `WS-43`, `ENG-06`, `ENG-09`, `ENG-10` and `VER-05`. New MUST rules: `WS-44` and `ENG-26`.
- Lowered: `VER-01`, `TL-29`, `TL-31` and `WS-02` to SHOULD, and `WS-40` to MAY. The next-step wording of `TL-31` moved to `TL-43`. New SHOULD rules: `PRO-24`, `TL-40`, `TL-41` and `TL-42`.
- `WS-15` and `WS-16` limit the approval off-switch and throwaway projects to ordinary writes. Destructive, code-running, system and online-device operations, shared data and paths outside the root always need approval.
- `PRO-12` says what a re-issued write returns, `PRO-13` says nothing more is sent after a cancel, and `WS-17` defines `partial` and `unknown` for batches. `TL-14` requires an object schema root without `oneOf`, `anyOf` or `allOf`.
- `PRO-18` no longer rejects a request that has no `Origin`; such a request depends on `PRO-19`. `TL-21` requires the same error object and `execution` path across a service, not one result shape. `WS-26` refuses a write only when the start record cannot be written, and `WS-43` covers the end record.
- `mcp/README.md` lists the rules that are explicit exceptions to `general/` and `desktop/`, and says a service that can write to real projects is at least tier M.

**`vision/` and `dashboard/`, now draft 0.2**

- They were all SHOULD. Each now lists its own consequences under section 0.7 of `general/`. `vision/` has 32 MUST of 42 rules and `dashboard/` has 20 MUST of 28.
- Rules that bundled an end with a means are split, and the means stay SHOULD: `VIS-32`, `VIS-37` to `VIS-42` and `VIS-24`, plus `DSH-26`.
- New MUST rules in `vision/`: `VIS-35` (recipe matches the product, camera parameters read back), `VIS-36` (bypass needs permission, audit and a time limit) and `VIS-43` (production PC setup). `VIS-33` and `VIS-34` require an OK-image policy and an alarm when the NG rate or score distribution moves. `VIS-11` keeps replayed results away from the PLC and formal records, `VIS-20` covers a result that never arrives at the PLC, `VIS-27` stops judging after a count mismatch, `VIS-23` forbids retesting until a part passes, and `VIS-28` asks for a confidence bound on the escape rate. `VIS-21` relies on the handshake with the PLC or robot controller instead of read-back. `VIS-08` says a regression image set in controlled storage is not a fixture under `DAT-07` and `SEC-22`. `vision/README.md` states explicit exceptions to `P-04`, `SEC-03`, `ERR-08`, `IND-17` and `ARC-14` for judgement, measurement and positioning results written at line speed, and a tier line.
- New MUST rules in `dashboard/`: `DSH-24` (metric definitions), `DSH-25` (alarms during carousel), `DSH-27` (long-lived front ends reload) and `DSH-28` (mock data). `DSH-04` is MUST. `DSH-08` takes the data time from the source and keeps judging staleness during a disconnect, `DSH-15` no longer means leaving a machine unpatched, `DSH-19` covers credential renewal, and `DSH-10` requires one-way flow through an isolation zone only when the display is outside the production network. A showroom screen may treat `DSH-11`, `DSH-23`, `DSH-24` and `DSH-25` as SHOULD.

### Fixed

- `SEC-16` and `PRO-19` say constant-time comparison instead of fixed-length comparison, which was the wrong term.
- `mcp/handbook-mapping.md` corrected against the 1.1 text, including level changes it did not state.

### Removed

- The labels in `mcp/` that recorded how far existing projects implemented each rule, and the sentence in `README.md` about where the rules came from. `[规范]` stays, because it marks rules that come from the MCP specification.

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

[Unreleased]: https://github.com/asckye/engineering-standards/compare/v2.1...HEAD
[2.1]: https://github.com/asckye/engineering-standards/compare/v2.0...v2.1
[2.0]: https://github.com/asckye/engineering-standards/releases/tag/v2.0
