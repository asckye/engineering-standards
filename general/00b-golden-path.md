# <a id="golden"></a>★ 黄金路径与默认技术决策

> **要点** 新项目不讨论技术选型：按下表直接开工，几小时内能构建、测试、提交。偏离默认值在 README 或 ADR 中写一行理由。

## <a id="golden-defaults"></a>默认技术决策

| 方面 | .NET | TypeScript（Web） | Python |
|---|---|---|---|
| 运行时 | 当前 LTS 版 .NET；需要厂商 API 的进程按厂商要求（如 .NET Framework 4.8） | Node LTS；TypeScript `strict` | 3.12 及以上，版本文件固定 |
| 构建入口 | `dotnet run --project build-tools/Build -- <cmd>` | `pnpm run <script>` | `uv run <task>` |
| 依赖锁定 | `Directory.Packages.props` + `packages.lock.json` | `pnpm-lock.yaml`，精确版本 | `uv.lock` |
| 测试 | xUnit、`FakeTimeProvider`、Verify 快照 | Vitest、Testing Library、Playwright | pytest |
| 检查与格式化 | .NET 分析器 `latest-recommended`、`.editorconfig`、`dotnet format` | ESLint（typescript-eslint strict-type-checked）、Prettier | Ruff（lint 与格式化）、mypy strict |
| 日志、DI、配置 | Microsoft.Extensions.Logging / DependencyInjection / Configuration | 后端 pino；配置经环境变量，用 zod 校验 | `logging`（JSON 格式）；pydantic-settings |
| 序列化与校验 | System.Text.Json | zod | pydantic |
| 界面 | WPF + MVVM（桌面、上位机） | React + Vite（无特殊需求时） | 不做界面 |
| 契约 | MCP 官方 C# SDK；JSON Schema 2020-12 | OpenAPI 3.1 | OpenAPI（如有服务） |
| CI | 托管 CI 运行同一个构建入口；本机合并门为准（BLD-03） | 托管 CI 运行同一个构建入口；本机合并门为准（BLD-03） | 托管 CI 运行同一个构建入口；本机合并门为准（BLD-03） |

## <a id="golden-types"></a>按项目类型

| 类型 | 默认栈 | 额外的骨架 | 交付 |
|---|---|---|---|
| CLI 或库 | .NET 或 Python | `src/`、`tests/`、`build-tools/`；命令行输出一行 JSON 加退出码 | 按用户的 zip 或包仓库，附 SHA-256 |
| MCP 服务（`mcp/`，草稿） | .NET + 官方 MCP SDK，stdio 优先 | Contracts、Host、Adapters、worker 进程；`reference/` 示例源数据；契约快照 | 按用户的 zip；客户端配置写入带备份 |
| 上位机（`hmi/`） | .NET + WPF；通信库按 DEP-02 选定并写 ADR | 每种协议一个适配器；设备模拟器；变量配置 schema | 离线安装包；配置备份与恢复 |
| 桌面应用（`desktop/`） | .NET + WPF（或 WinUI） | Ui 工程（MVVM）、设计 token 资源、渲染测试 | 按用户安装与更新，签名 [M+] |
| Web（`web/`） | TypeScript 前端 + .NET 或 Node 后端 | `apps/web`、`apps/api`、`openapi/`、`migrations/`、`infra/` | 容器镜像，dev/staging/prod 晋升 |
| 移动（`mobile/`） | SwiftUI 与 Jetpack Compose；跨平台框架需 ADR | 按平台的工程；共享 API 客户端由 OpenAPI 生成 | 内部测试渠道，分阶段发布 |
| 视觉（`vision/`，草稿） | .NET + WPF；视觉库按 DEP-02 选定并写 ADR | 相机适配器；离线图像回放；带真值的回归图像集 | 离线安装包；配方与标定的备份和恢复 |
| 大屏（`dashboard/`，草稿） | TypeScript 前端 + 只读聚合 API | 展示层和聚合层；按目标分辨率的布局；模拟数据源 | 展示机上的固定运行环境 |

通用骨架见 [2.6](02-architecture.md#arch-modules)；代理说明用模板 [T.8](appendix/t-templates.md#tpl-agents)；采用步骤见 [第 25 节](25-adoption.md#adopt)。

---

[← 上一节：★ 最小必做清单](00a-minimum.md) · [目录](README.md) · [下一节：★ 任务手册 →](00c-playbooks.md)
