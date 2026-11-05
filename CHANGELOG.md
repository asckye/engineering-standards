# Changelog

All notable changes to this repository are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Version numbers follow the handbook's own policy (rule G-07).

## [Unreleased]

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

Changes made when the handbook moved from one HTML file to this repository. They are part of this first published 1.1, not a separate release, and no rule id, level or tier changed:

- The desktop token reference in the UI chapter now points at the tokens listed in that chapter.
- A few examples became generic, and the wording about where the change record lives follows the new file layout.
