---
name: web-app-standard
description: "Rules for web products: TypeScript front ends, accessibility, back-end APIs and OpenAPI contracts, OAuth and session cookies, injection, SSRF and upload safety, database migrations, backups and personal data, health checks, alerts and deployment. Use this skill whenever you build or change a website, web app, REST or GraphQL API, back-end service or its database, including login, file upload and schema changes, or 前端、后端、网站、接口、数据库迁移、登录. Use it together with general-engineering-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# Web 规范

规则全文在 [references/rules.md](references/rules.md)。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **认证和授权在服务端**：用 OAuth 2.0 或 OIDC，按资源检查授权；Cookie 设安全属性（WEB-13、WEB-14）。
2. **前端不放密钥**：发到浏览器的一切都是公开的（WEB-08）。
3. **口令和传输**：口令只存加盐的慢哈希，跨网络用 TLS（SEC-37、SEC-38）。
4. **防注入**：SQL 只用参数化查询，HTML 依赖框架转义并设 CSP（WEB-17、WEB-18）。
5. **防 SSRF 和恶意上传**：服务端请求走白名单，上传有大小上限，按内容判断类型（WEB-19、WEB-20）。
6. **数据库改动可控**：结构变更用入库的版本化迁移，由工具执行（WEB-23）。
7. **备份能恢复**：备份自动执行，定期演练恢复（WEB-25）。
8. **个人信息有清单**：最少收集，加密，有保留期和删除（WEB-26）。
9. **键盘和读屏能用**：全部键盘可用，面向公众的产品满足 WCAG 2.2 AA（WEB-03）。
10. **API 不破坏现有调用方**：同一主版本内只做增量（MIG-01）。
11. **坏了有人知道**：有健康检查和告警（OPS-03、OPS-05）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 前端 | [E.1 前端](references/rules.md#pe-front) |
| 后端和 API | [E.2 后端与 API](references/rules.md#pe-api) |
| 认证、注入、上传、SSRF | [E.3 Web 安全](references/rules.md#pe-sec) |
| 数据库、迁移、备份、个人数据 | [E.4 数据](references/rules.md#pe-data) |
| 部署、监控、告警 | [E.5 运维](references/rules.md#pe-ops) |
| 发布前 | [E.6 Web 发布清单](references/rules.md#pe-checklist) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
