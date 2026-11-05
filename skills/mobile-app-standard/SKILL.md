---
name: mobile-app-standard
description: "Rules for iOS, Android and cross-platform mobile apps: platform guidelines, permissions, secrets in Keychain or Keystore, privacy labels, deep links, notifications, accessibility, offline use, crash reporting consent and store release. Use this skill whenever you build or change a SwiftUI, Jetpack Compose, Flutter, React Native or other mobile app, including login, push notifications and deep links, or 移动 App、手机应用、安卓、iOS、应用商店. Use it together with general-engineering-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# 移动 App 规范

规则全文在 [references/rules.md](references/rules.md)。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **密钥放系统存储**：Keychain 或 Keystore，不放普通文件（MOB-08）。
2. **隐私说实话**：数据最少化，隐私标签和实际行为一致，第三方 SDK 也算（MOB-07）。
3. **深度链接不可信**：校验域名，参数按外部输入校验，不能直接触发写入（MOB-10）。
4. **通知不含敏感数据**：锁屏上谁都能看到（MOB-11）。
5. **读屏和大字号能用**（MOB-12）。
6. **崩溃报告要同意**（MOB-15）。
7. **传输加密**：用 TLS 并校验证书（SEC-38）。
8. **升级不丢数据**：发布前用上一版本的数据测升级（TST-13）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 设计、权限、网络、隐私、发布 | [规则全文](references/rules.md) |
| 发布前 | [F.1 移动发布清单](references/rules.md#pf-checklist) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
