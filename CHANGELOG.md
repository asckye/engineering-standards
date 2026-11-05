# Changelog

All notable changes to this repository are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Version numbers follow the handbook's own policy (rule G-07).

## [Unreleased]

## [2.0] - 2026-11-05

First version meant for publication. `general/`, `hmi/`, `desktop/`, `web/` and `mobile/` are 2.0; `mcp/`, `vision/` and `dashboard/` are drafts at 0.1. The major version changes because rules moved, and domains A and C were replaced.

### Added

- Draft 0.1 of a dedicated MCP standard under `mcp/` for services that connect to engineering software and can write to real projects. It targets MCP 2026-07-28, marks the evidence behind each rule, and maps every rule from the earlier domains A and C.
- Draft 0.1 of `vision/` for machine vision software and `dashboard/` for large data displays. All their rules are suggestions that no project has validated yet.
- `desktop/local-software.md` for software that runs on a user's or site machine.

### Changed

- The repository is now one `general/` folder for all projects plus one folder per project type: `mcp/`, `hmi/`, `vision/`, `dashboard/`, `desktop/`, `web/` and `mobile/`. Rule ids do not change.
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
