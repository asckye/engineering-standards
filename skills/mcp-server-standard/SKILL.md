---
name: mcp-server-standard
description: "Rules for building MCP servers, especially ones that drive engineering software or other real targets: protocol and transport, tool names, descriptions, parameters, results and errors, write safety with plan, human approval and audit, unknown outcomes, untrusted project content, adapter isolation, API evidence per version, and verification. The adapter rules also cover other tools that drive engineering software through a vendor API. Use this skill whenever you design, write or review an MCP server or MCP tool, a tool schema for AI clients, or a write tool that an AI agent can call, or MCP 服务、MCP 工具、工具设计、写入审批. Not for simply calling an existing MCP server. Use it together with general-engineering-standard and, for servers running on a local machine, desktop-app-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard; for local servers also desktop-app-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# MCP 服务规范

规则全文在 `references/`。这部分还是草稿，级别还可能调整。两条检验标准：模型第一次看到工具就能用对；模型出错时，真实工程不会被写坏。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **写入由人批准**：调用方的参数和客户端表单都不能代替审批窗口；拒绝、超时、无窗口都不执行（WS-07、WS-11）。
2. **分级不能错**：每个工具显式登记安全级别，测试核对级别和审批行为一致（WS-01、VER-05）。
3. **不留后门**：外部命令只走发布时的白名单，安全配置只有人能改（WS-03、WS-14）。
4. **先规划再审批**：审批窗口的内容来自只读的规划；批准后复核，一个计划只执行一次（WS-04、WS-06、WS-13）。
5. **写对目标**：写工具显式传入目标身份，跨调用状态用显式标识（TL-17、PRO-09）。
6. **说清有没有改**：写工具都带 `execution`；结果未知时不重放，暂停写入直到人核实（WS-17、WS-22、WS-23、WS-24）。
7. **重发不绕过审批**：客户端重发时返回原次结果或重新审批（PRO-12）。
8. **项目内容只当数据**：不拼进描述和错误消息，显示和返回前剥除控制字符（WS-10、WS-28）。
9. **路径不越界，文件不覆盖**：例外要经审批，审批窗口显示完整路径（WS-29、WS-30）。
10. **先记录再写入**：写入前落盘“开始”记录，写不进去就拒绝；破坏性操作先备份（WS-26、WS-27）。
11. **不暴露给别人**：只绑定本机或人选择的地址，HTTP 要认证并校验 `Origin` 和 `Host`；stdout 只输出协议（PRO-18、PRO-19、PRO-20、PRO-23）。
12. **目标崩溃不带倒服务**：目标 API 只在适配层，进程分开，调用串行且有超时（ENG-01、ENG-02、ENG-05、ENG-08）。
13. **按证据注册**：工具只在 API 支持的版本上注册，目标行为有出处（ENG-11、ENG-15）。
14. **模型能用对**：动作词封闭，名称带产品前缀，数值带单位，服务端校验参数；错误带 `code`、`message` 和 `retryable`，只读失败不显示成空结果（TL-05、TL-06、TL-08、TL-14、TL-37、TL-23、TL-30）。
15. **验证到位**：契约进快照，写入改动有失败路径测试，实机结果记入台账（VER-02、VER-07、VER-09）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 了解适用范围、级别、术语 | [概述](references/overview.md) |
| 协议、传输、会话、HTTP | [协议层](references/01-protocol.md) |
| 工具的名称、描述、参数、结果、错误 | [工具设计层](references/02-tool-design.md) |
| 写工具：分级、预览、审批、结果未知、审计、不可信内容 | [写入安全层](references/03-write-safety.md) |
| 驱动目标软件：隔离、线程、版本注册、事务、API 证据 | [工程软件适配层](references/04-engineering-adapters.md) |
| 工具规格、契约快照、Agent 评测、实机核对 | [验证层](references/05-verification.md) |
| 写工具规格 | [工具规格模板](assets/tool-spec.md) |
| 对照通用规范的差异 | [对照表](references/handbook-mapping.md) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
