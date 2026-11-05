"""Tests for check_standards.py. Run with: python -m unittest discover -s build-tools"""
import shutil
import tempfile
import unittest
from pathlib import Path

import check_standards as cs


class CheckStandardsTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def rules(self):
        return cs.all_rules(self.root)

    def test_must_without_reason_is_reported(self):
        self.write("general/a.md", "- **MUST** `AB-01` 规则。\n")
        problems = cs.check_rules(self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-01", problems[0])
        self.assertIn("no reason line", problems[0])

    def test_should_with_reason_is_reported(self):
        self.write("general/a.md", "- **SHOULD** `AB-01` 规则。\n  - 理由 · 原因。\n")
        self.assertIn("has a reason line", cs.check_rules(self.rules())[0])

    def test_must_with_reason_is_clean(self):
        self.write("general/a.md", "- **MUST NOT** `AB-01` 规则。\n  - 理由 · 原因。\n- **MAY** `AB-02` 规则。\n")
        self.assertEqual(cs.check_rules(self.rules()), [])

    def test_duplicate_id_is_reported(self):
        self.write("general/a.md", "- **MAY** `AB-01` 规则。\n")
        self.write("web/b.md", "- **MAY** `AB-01` 规则。\n")
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
        self.write("general/a.md", "- **MAY** `AB-01` 见 AB-02、SHA-256 和 P-256。\n- **MAY** `P-01` 规则。\n")
        problems = cs.check_references(self.root, self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-02", problems[0])

    def test_history_files_may_name_old_rules(self):
        self.write("general/a.md", "- **MAY** `AB-01` 规则。\n")
        self.write("CHANGELOG.md", "Removed AB-09.\n")
        self.assertEqual(cs.check_references(self.root, self.rules()), [])

    def test_expand_ranges_reads_both_forms(self):
        self.assertEqual(cs.expand_ranges("SEC-03–05"), {"SEC-03", "SEC-04", "SEC-05"})
        self.assertEqual(cs.expand_ranges("P-12–P-14"), {"P-12", "P-13", "P-14"})

    def test_must_missing_from_section_24_is_reported(self):
        self.write("general/24-enforcement.md", "| 机制 | AB-01–02 |\n")
        self.write("general/a.md", "- **MUST** `AB-01` 甲\n  - 理由 · 乙\n- **MUST** `AB-03` 甲\n  - 理由 · 乙\n")
        self.write("mcp/a.md", "- **MUST** `CD-01` 甲\n  - 理由 · 乙\n")
        problems = cs.check_enforcement(self.root, self.rules())
        self.assertEqual(len(problems), 1)
        self.assertIn("AB-03", problems[0])

    def test_template_copy_drift_is_reported_both_ways(self):
        self.write("general/26-checklists.md", '## <a id="checklist-release"></a>26.1\n\n- [ ] 甲（`AB-01`）。\n- [ ] 乙。\n')
        self.write("templates/release-checklist.md", "## 发布核对\n\n- [ ] 甲（AB-01）。\n- [ ] 丙。\n")
        original = cs.section_items(cs.read(self.root, "general/26-checklists.md"), 'id="checklist-release"')
        copy = cs.section_items(cs.read(self.root, "templates/release-checklist.md"), "## 发布核对")
        self.assertEqual(original - copy, {"- [ ] 乙。"})
        self.assertEqual(copy - original, {"- [ ] 丙。"})

    def test_crlf_and_bom_are_reported(self):
        self.write("a.md", "line\r\n")
        self.write("b.md", "﻿line\n")
        problems = cs.check_line_endings(self.root)
        self.assertEqual(len(problems), 2)
        self.assertIn("CRLF", problems[0])
        self.assertIn("BOM", problems[1])

    def test_version_mismatch_is_reported(self):
        self.write("general/00-purpose.md", "（当前 2.1，2026-11-05）\n")
        self.write("general/README.md", "版本 2.0 · 2026-11-05\n工程开发规范 2.1 · 2026-11-05\n")
        self.write("general/appendix/changelog.md", "| 2.1 | 2026-11-05 | x |\n")
        self.write("CHANGELOG.md", "## [2.1] - 2026-11-05\n")
        for part in ["desktop", "hmi", "web", "mobile"]:
            self.write(f"{part}/README.md", "状态：2.1。\n")
        for part in ["mcp", "vision", "dashboard"]:
            self.write(f"{part}/README.md", "状态：**草稿 0.2**。\n")
        self.write(
            "README.md",
            "| 所有项目 | x | 2.1 |\n| 上位机 | x | 2.1 |\n| 桌面应用 | x | 2.1 |\n| Web | x | 2.1 |\n| 移动 App | x | 2.1 |\n"
            "| M | [mcp/](mcp/README.md) | 草稿 0.2 |\n| V | [vision/](vision/README.md) | 草稿 0.2 |\n| D | [dashboard/](dashboard/README.md) | 草稿 0.2 |\n",
        )
        problems = cs.check_versions(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("版本 2.1", problems[0])


if __name__ == "__main__":
    unittest.main()
