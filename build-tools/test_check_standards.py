"""Tests for check_standards.py. Run with: python -m unittest discover -s build-tools"""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import check_standards as cs


def remove_tree(path):
    """Git makes its objects read-only, which stops rmtree on Windows."""
    for item in path.rglob("*"):
        if item.is_file():
            item.chmod(0o666)
    shutil.rmtree(path)


class CheckStandardsTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(remove_tree, self.root)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def rules(self):
        return cs.all_rules(self.root)

    def test_must_without_reason_is_reported(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 规则。\n")
        problems = cs.check_rules(self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-01", problems[0])
        self.assertIn("no reason line", problems[0])

    def test_should_with_reason_is_reported(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **SHOULD** `AB-01` 规则。\n  - 理由 · 原因。\n")
        self.assertIn("has a reason line", cs.check_rules(self.rules())[0])

    def test_must_with_reason_is_clean(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST NOT** `AB-01` 规则。\n  - 理由 · 原因。\n- **MAY** `AB-02` 规则。\n")
        self.assertEqual(cs.check_rules(self.rules()), [])

    def test_duplicate_id_is_reported(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MAY** `AB-01` 规则。\n")
        self.write("skills/web-app-standard/references/b.md", "- **MAY** `AB-01` 规则。\n")
        self.assertIn("also defined", cs.check_rules(self.rules())[0])

    def test_broken_link_and_anchor_are_reported(self):
        self.write("a.md", '<a id="here"></a>\n[ok](a.md#here) [no file](b.md) [no anchor](a.md#there)\n')
        problems = cs.check_links(self.root)
        self.assertEqual(len(problems), 2)
        self.assertIn("b.md", problems[0])
        self.assertIn("a.md#there", problems[1])

    def test_links_in_fenced_code_are_ignored(self):
        self.write("a.md", "```\n[x](missing.md)\n```\n")
        self.assertEqual(cs.check_links(self.root), [])

    def test_undefined_reference_is_reported_and_other_tokens_are_not(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MAY** `AB-01` 见 AB-02、SHA-256 和 P-256。\n- **MAY** `P-01` 规则。\n")
        problems = cs.check_references(self.root, self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-02", problems[0])

    def test_history_files_may_name_old_rules(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MAY** `AB-01` 规则。\n")
        self.write("CHANGELOG.md", "Removed AB-09.\n")
        self.assertEqual(cs.check_references(self.root, self.rules()), [])

    def test_expand_ranges_reads_both_forms(self):
        self.assertEqual(cs.expand_ranges("SEC-03–05"), {"SEC-03", "SEC-04", "SEC-05"})
        self.assertEqual(cs.expand_ranges("P-12–P-14"), {"P-12", "P-13", "P-14"})

    def test_must_missing_from_section_24_is_reported(self):
        self.write(f"{cs.GENERAL}/references/24-enforcement.md", "| 机制 | AB-01–02 |\n")
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **MUST** `AB-03` 甲\n  - 理由 · 乙\n")
        self.write("skills/mcp-server-standard/references/a.md", "- **MUST** `CD-01` 甲\n  - 理由 · 乙\n")
        problems = cs.check_enforcement(self.root, self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-03", problems[0])

    def test_template_copy_drift_is_reported_both_ways(self):
        self.write(f"{cs.GENERAL}/references/26-checklists.md", '## <a id="checklist-release"></a>26.1\n\n- [ ] 甲（`AB-01`）。\n- [ ] 乙。\n')
        self.write(cs.RELEASE_TEMPLATE, "## 发布核对\n\n- [ ] 甲（AB-01）。\n- [ ] 丙。\n")
        original = cs.section_items(cs.read(self.root, f"{cs.GENERAL}/references/26-checklists.md"), 'id="checklist-release"')
        copy = cs.section_items(cs.read(self.root, cs.RELEASE_TEMPLATE), "## 发布核对")
        self.assertEqual(original - copy, {"- [ ] 乙。"})
        self.assertEqual(copy - original, {"- [ ] 丙。"})

    def write_skill(self, name, body="## 最小清单\n\n1. **甲**（AB-01）。\n\n## 其他\n\n2. 不算（CD-01）。\n", front=None):
        front = front if front is not None else f'name: {name}\ndescription: "甲"'
        self.write(f"skills/{name}/SKILL.md", f"---\n{front}\n---\n\n{body}")

    def write_all_skills(self):
        for name in [*cs.RELEASED_PARTS, *cs.DRAFT_PARTS]:
            self.write_skill(name)
        twenty = "\n".join(f"{i}. **甲**（AB-01）。" for i in range(1, 21))
        self.write_skill("general-engineering-standard", f"## 最小必做清单\n\n{twenty}\n")

    def test_minimum_list_problems_are_reported(self):
        self.write_all_skills()
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **SHOULD** `CD-01` 甲\n")
        self.assertEqual(cs.check_minimum_lists(self.root, self.rules()), [])
        self.write_skill("web-app-standard", "## 最小清单\n\n1. **甲**（CD-01）。\n2. **乙**没有编号。\n")
        self.write_skill("mobile-app-standard", "没有清单。\n")
        self.write_skill("hmi-standard", "## 最小清单\n\n没有条目。\n")
        problems = cs.check_minimum_lists(self.root, self.rules())
        self.assertEqual(len(problems), 4)
        self.assertIn("hmi-standard/SKILL.md: the minimum list is empty", problems[0])
        self.assertIn("CD-01, which is not a MUST", problems[1])
        self.assertIn("cites no rule", problems[2])
        self.assertIn("has no minimum list", problems[3])

    def test_general_minimum_list_needs_twenty_items(self):
        self.write_all_skills()
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **SHOULD** `CD-01` 甲\n")
        self.write_skill("general-engineering-standard", "## 最小必做清单\n\n1. **甲**（AB-01）。\n")
        problems = cs.check_minimum_lists(self.root, self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("has 1 items", problems[0])

    def test_frontmatter_problems_are_reported(self):
        self.write_all_skills()
        self.write_skill("web-app-standard", front='name: web-app-standard\ndescription: "甲"\nmodel: x')
        self.write_skill("mobile-app-standard", front="name: mobile-app-standard\ndescription: 甲: 乙")
        self.write_skill("hmi-standard", front='name: hmi-standard\ndescription: "甲"\ncompatibility: "' + "乙" * 501 + '"')
        problems = cs.check_skills(self.root)
        self.assertEqual(len(problems), 3)
        self.assertIn("compatibility must be at most 500", problems[0])
        self.assertIn("one double-quoted line", problems[1])
        self.assertIn("frontmatter key model", problems[2])

    def test_a_clean_skill_passes(self):
        self.write_all_skills()
        self.assertEqual(cs.check_skills(self.root), [])

    def test_skill_format_problems_are_reported(self):
        self.write_all_skills()
        self.write_skill("web-app-standard", front='name: other\ndescription: "甲"')
        self.write_skill("mobile-app-standard", front="name: mobile-app-standard")
        self.write("skills/hmi-standard/SKILL.md", "没有开头。\n")
        problems = cs.check_skills(self.root)
        self.assertEqual(len(problems), 4)
        self.assertIn("hmi-standard/SKILL.md: has no frontmatter", problems[0])
        self.assertIn("mobile-app-standard/SKILL.md: description must be one", problems[1])
        self.assertIn("mobile-app-standard/SKILL.md: description must be 1 to", problems[2])
        self.assertIn("web-app-standard/SKILL.md: name", problems[3])

    def test_unlinked_file_and_unknown_skill_are_reported(self):
        self.write_all_skills()
        self.write("skills/hmi-standard/references/lost.md", "甲\n")
        self.write_skill("extra-standard")
        problems = cs.check_skills(self.root)
        self.assertEqual(len(problems), 2)
        self.assertIn("found", problems[0])
        self.assertIn("does not link skills/hmi-standard/references/lost.md", problems[1])

    def test_manifest_problems_are_reported(self):
        self.write(f"{cs.GENERAL}/references/00-purpose.md", "（当前 2.1，2026-11-05）\n")
        self.write(".claude-plugin/plugin.json", '{"name": "a", "version": "2.1.0"}')
        self.write(".claude-plugin/marketplace.json", '{"name": "m", "plugins": [{"name": "a", "source": "./"}]}')
        self.write("README.md", "claude plugin install a@m\n")
        self.assertEqual(cs.check_manifests(self.root), [])
        self.write(".claude-plugin/plugin.json", '{"name": "b", "version": "2.0.0"}')
        self.write(".claude-plugin/marketplace.json", '{"name": "m", "plugins": [{"name": "a", "source": "./gone"}]}')
        problems = cs.check_manifests(self.root)
        self.assertEqual(len(problems), 4)
        self.assertIn("must list exactly", problems[0])
        self.assertIn("source ./gone", problems[1])
        self.assertIn("install command", problems[2])
        self.assertIn("does not match", problems[3])

    def git(self, *args):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args], cwd=self.root, check=True, capture_output=True)

    def test_must_lowered_since_the_last_tag_is_reported(self):
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **MUST** `AB-02` 甲\n  - 理由 · 乙\n- **MUST** `AB-03` 甲\n  - 理由 · 乙\n- **MUST** `AB-04` 甲\n  - 理由 · 乙\n")
        self.git("init", "-q")
        self.git("add", f"{cs.GENERAL}/references/a.md")
        self.git("commit", "-q", "-m", "first")
        self.git("tag", "v2.1")
        self.write(f"{cs.GENERAL}/references/00-purpose.md", "（当前 2.1，2026-11-05）\n")
        self.write(f"{cs.GENERAL}/references/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **SHOULD** `AB-02` 甲\n- **MUST** `AB-04` [M+] 甲\n  - 理由 · 乙\n")
        problems = cs.check_against_tag(self.root, cs.all_rules(self.root))
        self.assertEqual(len(problems), 3)
        self.assertIn("AB-02: was MUST in v2.1 and is SHOULD", problems[0])
        self.assertIn("AB-03: was MUST in v2.1 and is gone", problems[1])
        self.assertIn("AB-04: applied from tier [] in v2.1 and now from [M+]", problems[2])

    def test_crlf_and_bom_are_reported(self):
        self.write("a.md", "line\r\n")
        self.write("b.md", "﻿line\n")
        problems = cs.check_line_endings(self.root)
        self.assertEqual(len(problems), 2)
        self.assertIn("CRLF", problems[0])
        self.assertIn("BOM", problems[1])

    def test_version_mismatch_is_reported(self):
        self.write(f"{cs.GENERAL}/references/00-purpose.md", "（当前 2.1，2026-11-05）\n")
        self.write(f"{cs.GENERAL}/references/contents.md", "版本 2.0 · 2026-11-05\n工程开发规范 2.1 · 2026-11-05\n")
        self.write(f"{cs.GENERAL}/references/appendix/changelog.md", "| 2.1 | 2026-11-05 | x |\n")
        self.write("CHANGELOG.md", "## [2.1] - 2026-11-05\n")
        rows = []
        for skill, (label, status_file) in cs.RELEASED_PARTS.items():
            self.write(f"skills/{skill}/{status_file}", "状态：2.1。\n") if skill != "general-engineering-standard" else None
            rows.append(f"| {label} | x | 2.1 |")
        for skill, (label, status_file) in cs.DRAFT_PARTS.items():
            self.write(f"skills/{skill}/{status_file}", "状态：**草稿 0.2**。\n")
            rows.append(f"| {label} | x | 草稿 0.2 |")
        self.write("README.md", "\n".join(rows) + "\n")
        problems = cs.check_versions(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("版本 2.1", problems[0])


if __name__ == "__main__":
    unittest.main()
