---
name: dashboard-standard
description: "Rules for wall displays and unattended dashboards: layout for viewing distance and video walls, data age and failure states, metric definitions, read-only access, automatic recovery, watchdogs, soak tests, display security and simulated data. Use this skill whenever you build or change a big-screen dashboard, control-room or shop-floor display, KPI wall or kiosk board that runs for long periods, or 大屏、看板、数据大屏、车间看板、展厅屏幕. Not for ordinary analytics pages that people open and close. Use it together with general-engineering-standard and web-app-standard or desktop-app-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard and web-app-standard or desktop-app-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# 大屏规范

规则全文在 [references/rules.md](references/rules.md)。这部分还是草稿，级别还可能调整。大屏要在远处一眼看懂，并且长期无人值守地运行。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **只读**：大屏不提供写入目标或设备的操作（DSH-01）。
2. **过期看得出来**：数据时间取来源的时间，超过更新周期就标为过期（DSH-08）。
3. **失败不显示成 0**：区分没有数据、数据为零和取数失败（DSH-09）。
4. **指标口径清楚**：写明口径和更新周期，只有一份实现，核对班次和日切换（DSH-11、DSH-23、DSH-24）。
5. **不拖累生产**：前端不直连生产数据库或设备（DSH-10）。
6. **告警看得到**：轮播时新告警在任何页面都看得到，大屏不是告警的唯一途径（DSH-25）。
7. **看得清**：不裁切，关键数字不压拼接缝，字号按观看距离定（DSH-03、DSH-04、DSH-05）。
8. **自己能恢复**：断线自动重连，崩溃自动恢复，没有系统弹窗（DSH-13、DSH-15）。
9. **冻结能发现**：外部看门狗检查渲染循环的心跳（DSH-22）。
10. **能长期运行**：至少 72 小时浸泡测试（DSH-14）。
11. **内容和凭据安全**：按摆放场所脱敏，展示端用只读设备凭据（DSH-18、DSH-19）。
12. **模拟数据混不进生产显示**（DSH-28）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 确定范围 | [范围](references/rules.md#dsh-scope) |
| 布局、字号、拼接屏 | [显示与布局](references/rules.md#dsh-layout) |
| 取数、过期、失败、口径 | [数据](references/rules.md#dsh-data) |
| 断线、崩溃、看门狗 | [长期运行](references/rules.md#dsh-running) |
| 性能 | [性能](references/rules.md#dsh-performance) |
| 脱敏、凭据 | [安全与隐私](references/rules.md#dsh-security) |
| 测试 | [测试](references/rules.md#dsh-testing) |
| 发布前 | [发布清单](references/rules.md#dsh-checklist) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
