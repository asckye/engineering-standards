# 工程软件 MCP 开发规范

状态：**草稿 0.2**。还没有用项目从零验证过。草稿阶段级别还可能调整，不按 [G-07](../../general-engineering-standard/references/00-purpose.md#purpose-gov) 升主版本。

本规范写给开发 MCP 服务的人和 AI 编码代理。检验标准有两条：模型第一次看到工具就能用对；模型出错时，真实工程不会被写坏。

## 适用范围

**适用：** 通过 MCP 连接工程软件或设备，并且能写入真实工程的服务。这类服务通常运行在用户本机或虚拟机中，一次服务一位工程师，写错的代价很高，也可能很久之后才被发现。

**部分适用：** 多租户的远程服务和纯只读的查询服务。协议层和工具设计层仍然适用，但多租户远程服务的授权按 MCP 规范，不按 `PRO-19`、`PRO-23`。写入安全层和适配层按需要取舍，`WS-28`、`WS-29`、`WS-32` 始终适用。

**等级：** 能写入真实工程的服务至少按 M 级。

## 五层结构

| 层 | 文件 | 前缀 | 内容 |
|---|---|---|---|
| 协议层 | [01-protocol.md](01-protocol.md) | `PRO` | 按 MCP 修订固定；MCP 改版时主要改这一层 |
| 工具设计层 | [02-tool-design.md](02-tool-design.md) | `TL` | 词表、描述、参数、结果、错误、大小 |
| 写入安全层 | [03-write-safety.md](03-write-safety.md) | `WS` | 分级、预览、审批、结果未知、审计、不可信内容 |
| 工程软件适配层 | [04-engineering-adapters.md](04-engineering-adapters.md) | `ENG` | 隔离、线程、版本注册、事务、API 证据 |
| 验证层 | [05-verification.md](05-verification.md) | `VER` | 工具规格、契约快照、Agent 评测、实机核对 |

另有[工具规格模板](../assets/tool-spec.md)和[与工程开发规范 1.1 的对照表](handbook-mapping.md)。

## 级别怎么定

级别按[工程开发规范 0.7](../../general-engineering-standard/references/00-purpose.md#purpose-levels) 的标准定：按违反规则的后果，不看现有项目做到了多少。在本规范里，这些后果具体包括：

- 工程或数据被写坏，或者无法恢复、无法追查；
- 写入绕过人的确认；
- 凭据泄露，或写入能力暴露给预期以外的调用方；
- 模型选错工具、传错数值，或误判目标有没有被改；
- 目标软件或服务崩溃、挂起，工程师无法工作；
- 违反 MCP 规范的必需项，或升级后现有客户端失效；
- 对外声称了没有验证过的能力。

标 `[规范]` 的规则来自 MCP 2026-07-28 规范本身，其余是本规范的决定。`PRO-02` 是例外：它规定本规范的前提，不按后果定级。

`MUST`、`SHOULD`、`MAY` 的含义和优先级与[工程开发规范 0.3](../../general-engineering-standard/references/00-purpose.md#purpose-read) 相同。

## 和工程开发规范的关系

[通用规范](../../general-engineering-standard/references/contents.md)仍然适用，包括代码规范、注释、易读易维护、错误处理、依赖、测试和 Git。本机运行的服务还要采用[桌面与本机软件](../../desktop-app-standard/references/rules.md)中的本机软件、Windows、打包和诊断规则。

本规范取代工程开发规范 1.1 的领域 A（MCP 服务）和领域 C（工程软件自动化）。不做 MCP、但要经厂商 API 驱动工程软件的工具，也按[工程软件适配层](04-engineering-adapters.md)。本规范和通用规范或 `desktop-app-standard` 不一致时，以本规范为准。下面这些是明确的例外：`WS-29` 与 `SEC-07`，`WS-33` 与 `SEC-12`，`WS-15`、`WS-16` 与 `P-04`、`SEC-03`，`ENG-15` 与 `P-01`，`WS-34` 与 `SEC-14`，`PRO-18` 与 `SEC-17`，`PRO-19` 与 `SEC-16`，`WS-25`、`PRO-13` 与 `ERR-16`。服务把项目内容作为工具结果返回给用户配置的客户端时，不受 `AI-18`、`AI-21` 约束（[19.5](../../general-engineering-standard/references/19-ai.md#ai-data)），用户文档写明工具结果会经客户端发给所配置的模型。服务带 WPF 审批窗口时，再加[桌面应用](../../desktop-app-standard/references/rules.md)和[桌面界面](../../desktop-app-standard/references/ui.md)。规则对应关系和每处变化见[对照表](handbook-mapping.md)。


## 项目怎么采用

项目在[项目采用文件](../../general-engineering-standard/assets/project-adoption.md)或 README 的“工程规范”一行写明版本。做不到的规则登记为偏差：对 MUST 的例外写 ADR，偏离 SHOULD 写一行理由。规范不因为某个项目做不到而改变。

已发布的工具名和字段属于已发布的对外契约，优先级高于本规范（[0.3](../../general-engineering-standard/references/00-purpose.md#purpose-read)），不为本规范改名，登记为偏差即可。还在 MCP 旧修订上的服务同样登记偏差，并写明迁移计划。

## 目标协议

本规范按 [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) 编写。这次修订取消了协议会话和 `initialize` 握手，所有结果都带 `resultType`，服务端发起的请求改为多轮请求（MRTR），Tasks 移到了扩展。

## 设计决定

下面几处常有不同做法，本规范这样定：

1. **协议：** 服务用 2026-07-28；官方 SDK 有稳定版本时用稳定版本。
2. **命名：** 工具名带产品前缀，写成 `<产品>_<资源>_<动作>`；动作词是封闭词表；参数和结果字段用 snake_case。
3. **结果：** 不强制统一信封，一个服务内结构一致。写工具必须用 `execution` 说清目标有没有被改。
4. **错误：** 错误对象带 `code`、`message` 和 `retryable`。
5. **审批结果：** 拒绝、过期和无可用窗口用不同的错误码，因为模型的下一步不同。
6. **一次性项目：** 只有安全级别为“写入”、且只改这个一次性项目的操作可以免审批，是否一次性由服务端认定。

进程模型按目标 API 定：目标软件有进程外 API 时用独立 worker 进程，只有插件 API 时用目标软件内的插件。本规范只规定隔离和故障时的行为。

## 术语

| 词 | 含义 |
|---|---|
| 服务 | MCP 服务进程，负责协议、策略、审批和审计 |
| 目标 | 服务操作的工程软件或设备 |
| 适配层 | 唯一调用目标 API 的代码，可能在独立进程或目标软件的插件中 |
| 写入 | 任何改变目标、设备、配置或用户文件的操作 |
| 写工具、本地工具 | 定义见[写入安全层](03-write-safety.md) |
| 预览 | 不写入，返回变更清单 |
| 计划 | 规划或预览得到的变更清单 |
| 计划哈希 | 计划内容的摘要，用来把批准绑定到这份计划 |
| 状态指纹 | 目标身份和受影响对象当前状态的摘要，用来发现批准之后的变化 |
| 审批窗口 | 人独立操作的界面：服务自己的窗口或目标软件内的对话框 |
| 一次性项目 | 服务创建和认定的 scratch 工程，可以随时丢弃 |

## 路线图

- 下一版：用一个新的工程软件 MCP 项目从零试用，按结果调整规则和级别。
