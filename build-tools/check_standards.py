#!/usr/bin/env python3
"""Check the standards repository.

Checks internal links, rule ids, reason lines, section 24, version strings, the
checklists copied into templates, the skills and plugin manifests, line endings,
and that no MUST was lowered since the last tag of the same major version (rule G-07).

Usage: python build-tools/check_standards.py [--root PATH]
Exit code 0 when clean, 1 when a problem is found.
"""
import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

GENERAL = "skills/general-engineering-standard"
# Skill folder: its row in the root README, and the file with its status line.
RELEASED_PARTS = {
    "general-engineering-standard": ("所有项目", "references/contents.md"),
    "hmi-standard": ("上位机", "references/rules.md"),
    "desktop-app-standard": ("桌面应用", "references/rules.md"),
    "web-app-standard": ("Web", "references/rules.md"),
    "mobile-app-standard": ("移动 App", "references/rules.md"),
}
DRAFT_PARTS = {
    "mcp-server-standard": ("MCP 服务", "references/overview.md"),
    "machine-vision-standard": ("视觉", "references/rules.md"),
    "dashboard-standard": ("大屏", "references/rules.md"),
}
# Files that describe past states, so they may name rules that no longer exist.
HISTORY_FILES = {"CHANGELOG.md", f"{GENERAL}/references/appendix/changelog.md", "skills/mcp-server-standard/references/handbook-mapping.md"}
# Looks like a rule id but is not one: the elliptic curve name.
NOT_RULE_IDS = {"P-256"}
# Checklists kept in the standard and copied into a template.
RELEASE_TEMPLATE = f"{GENERAL}/assets/release-checklist.md"
DONE_TEMPLATE = f"{GENERAL}/assets/definition-of-done.md"
TEMPLATE_COPIES = [
    (f"{GENERAL}/references/26-checklists.md", "checklist-release", RELEASE_TEMPLATE, "发布核对"),
    (f"{GENERAL}/references/26-checklists.md", "checklist-real", RELEASE_TEMPLATE, "实机验证"),
    ("skills/hmi-standard/references/rules.md", "pb-checklist", RELEASE_TEMPLATE, "上位机：硬件在环 [M+]"),
    ("skills/desktop-app-standard/references/rules.md", "pd-checklist", RELEASE_TEMPLATE, "桌面"),
    ("skills/web-app-standard/references/rules.md", "pe-checklist", RELEASE_TEMPLATE, "Web"),
    ("skills/mobile-app-standard/references/rules.md", "pf-checklist", RELEASE_TEMPLATE, "移动"),
    ("skills/machine-vision-standard/references/rules.md", "vis-checklist", RELEASE_TEMPLATE, "视觉"),
    ("skills/dashboard-standard/references/rules.md", "dsh-checklist", RELEASE_TEMPLATE, "大屏"),
    (f"{GENERAL}/references/23-definition-of-done.md", "dod-task", DONE_TEMPLATE, "任务完成"),
    (f"{GENERAL}/references/23-definition-of-done.md", "dod-merge", DONE_TEMPLATE, "合并完成"),
    (f"{GENERAL}/references/23-definition-of-done.md", "dod-release", DONE_TEMPLATE, "发布完成"),
    (f"{GENERAL}/references/23-definition-of-done.md", "dod-delivery", DONE_TEMPLATE, "交付完成 [M+]"),
]

RULE_RE = re.compile(r"^\s*- \*\*(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\*\* `([A-Z][A-Z0-9]*-\d+)`(?: \[(M\+|L)\])?")
ID_RE = re.compile(r"\b([A-Z][A-Z0-9]*-\d+)\b")
RANGE_RE = re.compile(r"\b([A-Z][A-Z0-9]*)-(\d+)[–-](?:\1-)?(\d+)\b")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^```.*?^```", re.M | re.S)
ANCHOR_RE = re.compile(r'<a id="([^"]+)"')
HEADING_RE = re.compile(r"^#+ (.+)$", re.M)
VERSION_RE = re.compile(r"（当前 (\d+\.\d+)，(\d{4}-\d{2}-\d{2})）")
SKILL_KEYS = {"name", "description", "license", "compatibility", "metadata"}
TIER_RANK = {"": 0, "M+": 1, "L": 2}
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Rule:
    rule_id: str
    level: str
    path: str
    line: int
    has_reason: bool
    tier: str = ""


def read(root, rel):
    return (root / rel).read_text(encoding="utf-8")


def part_of(rel):
    """Return the skill a repository path belongs to, or its top folder outside skills/."""
    parts = rel.split("/")
    return parts[1] if parts[0] == "skills" and len(parts) > 2 else parts[0]


def markdown_files(root):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*.md") if ".git" not in p.parts)


def parse_rules(text, rel="", line_offset=0):
    lines = text.split("\n")
    rules = []
    for i, line in enumerate(lines):
        m = RULE_RE.match(line)
        if m:
            has_reason = i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- 理由")
            rules.append(Rule(m.group(2), m.group(1), rel, i + 1 + line_offset, has_reason, m.group(3) or ""))
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
    listed = expand_ranges(read(root, f"{GENERAL}/references/24-enforcement.md"))
    problems = []
    for rule in rules:
        if part_of(rule.path) in RELEASED_PARTS and rule.level.startswith("MUST") and rule.rule_id not in listed:
            problems.append(f"{rule.path}:{rule.line}: {rule.rule_id} is {rule.level} and not listed in section 24")
    return problems


def current_version(root):
    m = VERSION_RE.search(read(root, f"{GENERAL}/references/00-purpose.md"))
    return (m.group(1), m.group(2)) if m else (None, None)


def check_versions(root):
    version, date = current_version(root)
    if version is None:
        return [f"{GENERAL}/references/00-purpose.md: G-07 does not state the current version"]
    expected = [
        (f"{GENERAL}/references/contents.md", f"版本 {version} · {date}"),
        (f"{GENERAL}/references/contents.md", f"工程开发规范 {version} · {date}"),
        (f"{GENERAL}/references/appendix/changelog.md", f"| {version} | {date} |"),
        ("CHANGELOG.md", f"## [{version}] - {date}"),
    ]
    expected += [
        (f"skills/{skill}/{status_file}", f"状态：{version}。")
        for skill, (_, status_file) in RELEASED_PARTS.items()
        if skill != "general-engineering-standard"
    ]
    problems = [f"{rel}: does not say {text}" for rel, text in expected if text not in read(root, rel)]
    table = read(root, "README.md")
    for label, _ in RELEASED_PARTS.values():
        if not re.search(rf"^\| {label} \|.*\| {re.escape(version)} \|$", table, re.M):
            problems.append(f"README.md: the row for {label} does not say {version}")
    for skill, (label, status_file) in DRAFT_PARTS.items():
        rel = f"skills/{skill}/{status_file}"
        m = re.search(r"状态：\*\*草稿 (\d+\.\d+)\*\*", read(root, rel))
        if not m:
            problems.append(f"{rel}: has no draft status line")
        elif not re.search(rf"^\| {label} \|.*\| 草稿 {re.escape(m.group(1))} \|$", table, re.M):
            problems.append(f"README.md: the row for {label} does not say 草稿 {m.group(1)}")
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


def check_minimum_lists(root, rules):
    """Each project type's SKILL.md has a minimum list, and it cites only existing MUST rules."""
    levels = {rule.rule_id: rule.level for rule in rules}
    problems = []
    for skill in [*RELEASED_PARTS, *DRAFT_PARTS]:
        rel = f"skills/{skill}/SKILL.md"
        lines = read(root, rel).split("\n")
        start = next((i for i, line in enumerate(lines) if line.startswith("## ") and "最小" in line), None)
        if start is None:
            problems.append(f"{rel}: has no minimum list")
            continue
        items = []
        for line in lines[start + 1 :]:
            if line.startswith("#"):
                break
            if re.match(r"\d+\. ", line):
                items.append(line)
        if skill == "general-engineering-standard":
            if len(items) != 20:
                problems.append(f"{rel}: the minimum list has {len(items)} items, and section 0.2 relies on 20")
            continue
        if not items:
            problems.append(f"{rel}: the minimum list is empty")
        for line in items:
            cited = ID_RE.findall(line)
            if not cited:
                problems.append(f"{rel}: this minimum list item cites no rule: {line}")
            for rule_id in cited:
                if not levels.get(rule_id, "").startswith("MUST"):
                    problems.append(f"{rel}: the minimum list cites {rule_id}, which is not a MUST")
    return problems


def check_skills(root):
    """Each skill follows the Agent Skills format and links every file it ships."""
    expected = sorted([*RELEASED_PARTS, *DRAFT_PARTS])
    folders = sorted(p.name for p in (root / "skills").iterdir() if p.is_dir())
    problems = [] if folders == expected else [f"skills/: expected {expected}, found {folders}"]
    for name in folders:
        rel = f"skills/{name}/SKILL.md"
        if not (root / rel).exists():
            problems.append(f"{rel}: is missing")
            continue
        text = read(root, rel)
        m = FRONTMATTER_RE.match(text)
        if not m:
            problems.append(f"{rel}: has no frontmatter")
            continue
        fields = dict(re.findall(r'^(name|description|compatibility): "?(.*?)"?$', m.group(1), re.M))
        for key in sorted(set(re.findall(r"^([A-Za-z_-]+):", m.group(1), re.M)) - SKILL_KEYS):
            problems.append(f"{rel}: frontmatter key {key} is not part of the Agent Skills format we use")
        if not re.search(r'^description: "[^"]*"$', m.group(1), re.M):
            problems.append(f"{rel}: description must be one double-quoted line with no double quote inside")
        if fields.get("name") != name or not SKILL_NAME_RE.match(name) or len(name) > 64:
            problems.append(f"{rel}: name must match the folder and use lowercase letters, digits and single hyphens")
        if not 1 <= len(fields.get("description", "")) <= 1024:
            problems.append(f"{rel}: description must be 1 to 1024 characters")
        if len(fields.get("compatibility", "")) > 500:
            problems.append(f"{rel}: compatibility must be at most 500 characters")
        if text.count("\n") > 500:
            problems.append(f"{rel}: is over 500 lines")
        linked = {(root / "skills" / name / m.group(1).partition("#")[0]).resolve() for m in LINK_RE.finditer(text)}
        for folder in ("references", "assets"):
            for path in sorted((root / "skills" / name / folder).rglob("*.md")):
                if path.resolve() not in linked:
                    problems.append(f"{rel}: does not link {path.relative_to(root).as_posix()}")
    return problems


def check_manifests(root):
    plugin = json.loads(read(root, ".claude-plugin/plugin.json"))
    market = json.loads(read(root, ".claude-plugin/marketplace.json"))
    problems = []
    if [entry["name"] for entry in market["plugins"]] != [plugin["name"]]:
        problems.append(".claude-plugin/marketplace.json: must list exactly the plugin in plugin.json")
    for entry in market["plugins"]:
        if not (root / entry["source"]).is_dir():
            problems.append(f".claude-plugin/marketplace.json: source {entry['source']} does not exist")
    if f"{plugin['name']}@{market['name']}" not in read(root, "README.md"):
        problems.append("README.md: the install command does not name this plugin and marketplace")
    version, _ = current_version(root)
    if "version" in plugin and not plugin["version"].startswith(f"{version}."):
        problems.append(f".claude-plugin/plugin.json: version {plugin['version']} does not match the standard's {version}")
    return problems


def check_line_endings(root):
    problems = []
    for path in sorted(root.rglob("*")):
        if ".git" in path.parts or not path.is_file() or path.suffix not in {".md", ".py", ".yml", ".json"}:
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
        if rel.endswith(".md") and part_of(rel) in RELEASED_PARTS:
            shown = git(root, "show", f"{tag}:{rel}")
            old_rules.update({r.rule_id: r for r in parse_rules(shown.stdout)})
    now = {rule.rule_id: rule for rule in rules}
    problems = []
    for rule_id, old in sorted(old_rules.items()):
        if not old.level.startswith("MUST"):
            continue
        if rule_id not in now:
            problems.append(f"{rule_id}: was {old.level} in {tag} and is gone; that needs a new major version (G-07)")
        elif not now[rule_id].level.startswith("MUST"):
            problems.append(f"{rule_id}: was {old.level} in {tag} and is {now[rule_id].level}; that needs a new major version (G-07)")
        elif TIER_RANK[now[rule_id].tier] > TIER_RANK[old.tier]:
            problems.append(f"{rule_id}: applied from tier [{old.tier}] in {tag} and now from [{now[rule_id].tier}]; that needs a new major version (G-07)")
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
    problems += check_minimum_lists(root, rules)
    problems += check_skills(root)
    problems += check_manifests(root)
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
