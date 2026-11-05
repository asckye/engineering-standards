#!/usr/bin/env python3
"""Check the standards repository.

Checks internal links, rule ids, reason lines, section 24, version strings, the
checklists copied into templates, line endings, and that no MUST was lowered
since the last tag of the same major version (rule G-07).

Usage: python build-tools/check_standards.py [--root PATH]
Exit code 0 when clean, 1 when a problem is found.
"""
import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

RELEASED_PARTS = ["general", "desktop", "hmi", "web", "mobile"]
DRAFT_PARTS = ["mcp", "vision", "dashboard"]
# Files that describe past states, so they may name rules that no longer exist.
HISTORY_FILES = {"CHANGELOG.md", "general/appendix/changelog.md", "mcp/handbook-mapping.md"}
# Looks like a rule id but is not one: the elliptic curve name.
NOT_RULE_IDS = {"P-256"}
# Checklists kept in the standard and copied into a template.
TEMPLATE_COPIES = [
    ("general/26-checklists.md", "checklist-release", "templates/release-checklist.md", "发布核对"),
    ("general/26-checklists.md", "checklist-real", "templates/release-checklist.md", "实机验证"),
    ("hmi/README.md", "pb-checklist", "templates/release-checklist.md", "上位机：硬件在环 [M+]"),
    ("desktop/README.md", "pd-checklist", "templates/release-checklist.md", "桌面"),
    ("web/README.md", "pe-checklist", "templates/release-checklist.md", "Web"),
    ("mobile/README.md", "pf-checklist", "templates/release-checklist.md", "移动"),
    ("vision/README.md", "vis-checklist", "templates/release-checklist.md", "视觉"),
    ("dashboard/README.md", "dsh-checklist", "templates/release-checklist.md", "大屏"),
    ("general/23-definition-of-done.md", "dod-task", "templates/definition-of-done.md", "任务完成"),
    ("general/23-definition-of-done.md", "dod-merge", "templates/definition-of-done.md", "合并完成"),
    ("general/23-definition-of-done.md", "dod-release", "templates/definition-of-done.md", "发布完成"),
    ("general/23-definition-of-done.md", "dod-delivery", "templates/definition-of-done.md", "交付完成 [M+]"),
]

RULE_RE = re.compile(r"^\s*- \*\*(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\*\* `([A-Z][A-Z0-9]*-\d+)`")
ID_RE = re.compile(r"\b([A-Z][A-Z0-9]*-\d+)\b")
RANGE_RE = re.compile(r"\b([A-Z][A-Z0-9]*)-(\d+)[–-](?:\1-)?(\d+)\b")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^```.*?^```", re.M | re.S)
ANCHOR_RE = re.compile(r'<a id="([^"]+)"')
HEADING_RE = re.compile(r"^#+ (.+)$", re.M)
VERSION_RE = re.compile(r"（当前 (\d+\.\d+)，(\d{4}-\d{2}-\d{2})）")


@dataclass(frozen=True)
class Rule:
    rule_id: str
    level: str
    path: str
    line: int
    has_reason: bool


def read(root, rel):
    return (root / rel).read_text(encoding="utf-8")


def markdown_files(root):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*.md") if ".git" not in p.parts)


def parse_rules(text, rel="", line_offset=0):
    lines = text.split("\n")
    rules = []
    for i, line in enumerate(lines):
        m = RULE_RE.match(line)
        if m:
            has_reason = i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- 理由")
            rules.append(Rule(m.group(2), m.group(1), rel, i + 1 + line_offset, has_reason))
    return rules


def all_rules(root):
    rules = []
    for rel in markdown_files(root):
        rules.extend(parse_rules(read(root, rel), rel))
    return rules


def expand_ranges(text):
    """Return every rule id a text names, reading SEC-03–10 and P-12–P-14 as ranges."""
    found = set(ID_RE.findall(text))
    for prefix, start, end in RANGE_RE.findall(text):
        for n in range(int(start), int(end) + 1):
            found.add(f"{prefix}-{n:0{len(start)}d}")
    return found


def heading_slug(heading):
    plain = ANCHOR_RE.sub("", heading)
    plain = re.sub(r"</a>", "", plain)
    return re.sub(r"[^\w\- ]", "", plain.lower()).strip().replace(" ", "-")


def check_links(root):
    files = markdown_files(root)
    anchors = {}
    for rel in files:
        text = read(root, rel)
        anchors[rel] = set(ANCHOR_RE.findall(text)) | {heading_slug(h) for h in HEADING_RE.findall(text)}
    problems = []
    for rel in files:
        text = FENCE_RE.sub("", read(root, rel))
        for m in LINK_RE.finditer(text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, fragment = url.partition("#")
            target = (root / rel).parent / path if path else root / rel
            if not target.exists():
                problems.append(f"{rel}: link target does not exist: {url}")
                continue
            if fragment and target.suffix == ".md":
                key = target.resolve().relative_to(root.resolve()).as_posix()
                if fragment not in anchors.get(key, set()):
                    problems.append(f"{rel}: anchor does not exist: {url}")
    return problems


def check_rules(rules):
    problems = []
    seen = {}
    for rule in rules:
        where = f"{rule.path}:{rule.line}"
        if rule.rule_id in seen:
            problems.append(f"{where}: {rule.rule_id} is also defined at {seen[rule.rule_id]}")
        seen[rule.rule_id] = where
        is_must = rule.level.startswith("MUST")
        if is_must and not rule.has_reason:
            problems.append(f"{where}: {rule.rule_id} is {rule.level} and has no reason line (G-12)")
        if not is_must and rule.has_reason:
            problems.append(f"{where}: {rule.rule_id} is {rule.level} and has a reason line")
    return problems


def check_references(root, rules):
    defined = {rule.rule_id for rule in rules}
    prefixes = {rule_id.split("-")[0] for rule_id in defined}
    problems = []
    for rel in markdown_files(root):
        if rel in HISTORY_FILES:
            continue
        for rule_id in sorted(set(ID_RE.findall(read(root, rel)))):
            if rule_id in NOT_RULE_IDS or rule_id in defined:
                continue
            if rule_id.split("-")[0] in prefixes:
                problems.append(f"{rel}: names {rule_id}, which is not defined")
    return problems


def check_enforcement(root, rules):
    """Rule ENF-01: every MUST outside the drafts has a way of being checked in section 24."""
    listed = expand_ranges(read(root, "general/24-enforcement.md"))
    problems = []
    for rule in rules:
        part = rule.path.split("/")[0]
        if part in RELEASED_PARTS and rule.level.startswith("MUST") and rule.rule_id not in listed:
            problems.append(f"{rule.path}:{rule.line}: {rule.rule_id} is {rule.level} and not listed in section 24")
    return problems


def current_version(root):
    m = VERSION_RE.search(read(root, "general/00-purpose.md"))
    return (m.group(1), m.group(2)) if m else (None, None)


def check_versions(root):
    version, date = current_version(root)
    if version is None:
        return ["general/00-purpose.md: G-07 does not state the current version"]
    expected = [
        ("general/README.md", f"版本 {version} · {date}"),
        ("general/README.md", f"工程开发规范 {version} · {date}"),
        ("general/appendix/changelog.md", f"| {version} | {date} |"),
        ("CHANGELOG.md", f"## [{version}] - {date}"),
    ]
    expected += [(f"{part}/README.md", f"状态：{version}。") for part in RELEASED_PARTS if part != "general"]
    problems = [f"{rel}: does not say {text}" for rel, text in expected if text not in read(root, rel)]
    table = read(root, "README.md")
    for label, part in [("所有项目", "general"), ("上位机", "hmi"), ("桌面应用", "desktop"), ("Web", "web"), ("移动 App", "mobile")]:
        if not re.search(rf"^\| {label} \|.*\| {re.escape(version)} \|$", table, re.M):
            problems.append(f"README.md: the row for {label} ({part}) does not say {version}")
    for part in DRAFT_PARTS:
        m = re.search(r"状态：\*\*草稿 (\d+\.\d+)\*\*", read(root, f"{part}/README.md"))
        if not m:
            problems.append(f"{part}/README.md: has no draft status line")
        elif not re.search(rf"\[{part}/\]\({part}/README\.md\).*\| 草稿 {re.escape(m.group(1))} \|$", table, re.M):
            problems.append(f"README.md: the row for {part}/ does not say 草稿 {m.group(1)}")
    return problems


def section_items(text, start):
    """Return the checklist items under the heading that contains start."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("#") and start in line:
            items = set()
            for following in lines[i + 1 :]:
                if following.startswith("#"):
                    break
                if following.startswith("- [ ]"):
                    items.add(normalize_item(following))
            return items
    return None


def normalize_item(line):
    line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
    return line.replace("`", "").strip()


def check_template_copies(root):
    problems = []
    for source, anchor, template, heading in TEMPLATE_COPIES:
        original = section_items(read(root, source), f'id="{anchor}"')
        copy = section_items(read(root, template), f"## {heading}")
        if original is None:
            problems.append(f"{source}: section {anchor} not found")
            continue
        if copy is None:
            problems.append(f"{template}: section {heading} not found")
            continue
        for item in sorted(original - copy):
            problems.append(f"{template}: section {heading} lacks: {item}")
        for item in sorted(copy - original):
            problems.append(f"{source}: section {anchor} lacks: {item}")
    return problems


def check_line_endings(root):
    problems = []
    for path in sorted(root.rglob("*")):
        if ".git" in path.parts or not path.is_file() or path.suffix not in {".md", ".py", ".yml"}:
            continue
        data = path.read_bytes()
        rel = path.relative_to(root).as_posix()
        if b"\r\n" in data:
            problems.append(f"{rel}: has CRLF line endings")
        if data.startswith(b"\xef\xbb\xbf"):
            problems.append(f"{rel}: starts with a BOM")
    return problems


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8")


def check_against_tag(root, rules):
    """Rule G-07: lowering or removing a MUST outside the drafts needs a new major version."""
    tags = git(root, "tag", "--list", "v*", "--sort=-v:refname")
    if tags.returncode != 0 or not tags.stdout.strip():
        print("note: no version tag found, so MUST rules were not compared with a release")
        return []
    tag = tags.stdout.split()[0]
    version, _ = current_version(root)
    if version is None or tag.lstrip("v").split(".")[0] != version.split(".")[0]:
        print(f"note: {tag} has a different major version from {version}, so MUST rules were not compared")
        return []
    listing = git(root, "ls-tree", "-r", "--name-only", tag)
    old_rules = {}
    for rel in listing.stdout.split("\n"):
        if rel.endswith(".md") and rel.split("/")[0] in RELEASED_PARTS:
            shown = git(root, "show", f"{tag}:{rel}")
            old_rules.update({r.rule_id: r.level for r in parse_rules(shown.stdout)})
    now = {rule.rule_id: rule.level for rule in rules}
    problems = []
    for rule_id, level in sorted(old_rules.items()):
        if not level.startswith("MUST"):
            continue
        if rule_id not in now:
            problems.append(f"{rule_id}: was {level} in {tag} and is gone; that needs a new major version (G-07)")
        elif not now[rule_id].startswith("MUST"):
            problems.append(f"{rule_id}: was {level} in {tag} and is {now[rule_id]}; that needs a new major version (G-07)")
    return problems


def run_checks(root):
    rules = all_rules(root)
    problems = []
    problems += check_links(root)
    problems += check_rules(rules)
    problems += check_references(root, rules)
    problems += check_enforcement(root, rules)
    problems += check_versions(root)
    problems += check_template_copies(root)
    problems += check_line_endings(root)
    problems += check_against_tag(root, rules)
    return rules, problems


def main():
    parser = argparse.ArgumentParser(description="Check the standards repository.")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="repository root")
    args = parser.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    rules, problems = run_checks(Path(args.root))
    for problem in problems:
        print(problem)
    must = sum(rule.level.startswith("MUST") for rule in rules)
    print(f"{len(rules)} rules, {must} MUST, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
