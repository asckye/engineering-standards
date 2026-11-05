# 通用规范

所有项目都适用的规范：代码规范、注释、易读易维护、错误处理、安全、测试、依赖、构建与发布、验收交付、运行运维、退役、开发流程和 AI 协作。每类项目专属的规则在各自的 skill，见 [0.1](00-purpose.md#purpose-parts)。代码质量第一，流程按项目规模和风险取舍。

版本 3.0 · 2026-11-05 · [最小必做清单](../SKILL.md)约 3 分钟；加上黄金路径、任务手册与快速交付约 15 分钟。

用语：**MUST** 必须 · **SHOULD** 默认，偏离写理由 · **MAY** 允许 · [M+] 只对该等级及以上的项目（S/M/L，见 0.2）· 未标等级的规则：M、L 按其级别，S 作默认做法

## 目录

第 9 节（Windows 平台）、第 16 节（打包与安装）和第 22 节（诊断与支持）在 [desktop-app-standard](../../desktop-app-standard/references/rules.md)，原来的 MCP 和厂商 API 规则由 [mcp-server-standard](../../mcp-server-standard/references/overview.md) 取代，其余编号不变。

- [0 目的、等级与读法](00-purpose.md)
- [★ 最小必做清单](../SKILL.md)
- [★ 黄金路径与默认技术决策](00b-golden-path.md)
- [★ 任务手册](00c-playbooks.md)
- [★ 快速交付](00d-fast-delivery.md)
- [1 工程原则](01-principles.md)
- [2 架构](02-architecture.md)
- [3 代码规范](03-code.md)
- [4 代码质量](04-quality.md)
- [5 错误处理与健壮性](05-errors.md)
- [6 安全](06-security.md)
- [7 用户数据与隐私](07-privacy.md)
- [8 配置与环境](08-configuration.md)
- [10 国际化与本地化](10-i18n.md)
- [11 性能](11-performance.md)
- [12 测试](12-testing.md)
- [13 缺陷处理](13-defects.md)
- [14 依赖与许可](14-dependencies.md)
- [15 构建、验证与发布](15-build-release.md)
- [17 兼容、升级与迁移](17-compatibility.md)
- [18 开发流程、评审与 Git](18-process-review-git.md)
- [19 AI 辅助开发](19-ai.md)
- [20 文档](20-documentation.md)
- [21 界面设计](21-ui.md)
- [23 完成定义](23-definition-of-done.md)
- [24 让规则可执行](24-enforcement.md)
- [25 在新项目中采用](25-adoption.md)
- [26 通用检查清单](26-checklists.md)
- [27 验收与交付](27-acceptance-delivery.md)
- [28 运行与运维](28-operations.md)
- [29 支持期与退役](29-support-retirement.md)

## <a id="languages"></a>语言附录

- [附录 L1：C#/.NET](languages/l1-csharp.md)
- [附录 L2：TypeScript/JavaScript](languages/l2-typescript.md)
- [附录 L3：Python](languages/l3-python.md)

## 模板、术语与参考

- [附录 T：模板](appendix/t-templates.md)
- [附录：术语表](appendix/glossary.md)
- [参考资料](appendix/references.md)
- [标准对照](appendix/standards-mapping.md)
- [规范变更记录](appendix/changelog.md)

## 按规则编号查找

规则编号的前缀对应下列文件，包括各项目类型的 skill。

| 前缀 | 文件 |
|---|---|
| `ACC` | [27-acceptance-delivery.md](27-acceptance-delivery.md) |
| `AI` | [19-ai.md](19-ai.md) |
| `ARC` | [02-architecture.md](02-architecture.md) |
| `BLD` | [15-build-release.md](15-build-release.md) |
| `BUG` | [13-defects.md](13-defects.md) |
| `CFG` | [desktop-app-standard/references/local-software.md](../../desktop-app-standard/references/local-software.md)、[08-configuration.md](08-configuration.md) |
| `CMT` | [04-quality.md](04-quality.md) |
| `CODE` | [03-code.md](03-code.md) |
| `DAT` | [desktop-app-standard/references/local-software.md](../../desktop-app-standard/references/local-software.md)、[07-privacy.md](07-privacy.md) |
| `DEP` | [14-dependencies.md](14-dependencies.md) |
| `DIAG` | [desktop-app-standard/references/diagnostics.md](../../desktop-app-standard/references/diagnostics.md) |
| `DOC` | [20-documentation.md](20-documentation.md) |
| `DSH` | [dashboard-standard](../../dashboard-standard/references/rules.md) |
| `DSK` | [desktop-app-standard](../../desktop-app-standard/references/rules.md) |
| `ENF` | [24-enforcement.md](24-enforcement.md) |
| `ENG` | [mcp-server-standard/references/04-engineering-adapters.md](../../mcp-server-standard/references/04-engineering-adapters.md) |
| `EOL` | [29-support-retirement.md](29-support-retirement.md) |
| `ERR` | [05-errors.md](05-errors.md) |
| `FAST` | [00d-fast-delivery.md](00d-fast-delivery.md) |
| `G` | [00-purpose.md](00-purpose.md)、[appendix/glossary.md](appendix/glossary.md) |
| `GIT` | [18-process-review-git.md](18-process-review-git.md) |
| `I18N` | [10-i18n.md](10-i18n.md) |
| `IND` | [hmi-standard](../../hmi-standard/references/rules.md) |
| `MIG` | [desktop-app-standard/references/packaging.md](../../desktop-app-standard/references/packaging.md)、[17-compatibility.md](17-compatibility.md) |
| `MOB` | [mobile-app-standard](../../mobile-app-standard/references/rules.md) |
| `OPS` | [28-operations.md](28-operations.md) |
| `P` | [01-principles.md](01-principles.md) |
| `PERF` | [11-performance.md](11-performance.md) |
| `PKG` | [desktop-app-standard/references/packaging.md](../../desktop-app-standard/references/packaging.md)、[15-build-release.md](15-build-release.md) |
| `PLN` | [18-process-review-git.md](18-process-review-git.md) |
| `PRO` | [mcp-server-standard/references/01-protocol.md](../../mcp-server-standard/references/01-protocol.md) |
| `Q` | [04-quality.md](04-quality.md) |
| `REQ` | [18-process-review-git.md](18-process-review-git.md) |
| `REV` | [18-process-review-git.md](18-process-review-git.md) |
| `SEC` | [desktop-app-standard/references/local-software.md](../../desktop-app-standard/references/local-software.md)、[06-security.md](06-security.md) |
| `SUP` | [29-support-retirement.md](29-support-retirement.md) |
| `TL` | [mcp-server-standard/references/02-tool-design.md](../../mcp-server-standard/references/02-tool-design.md) |
| `TST` | [12-testing.md](12-testing.md) |
| `UI` | [desktop-app-standard/references/ui.md](../../desktop-app-standard/references/ui.md)、[21-ui.md](21-ui.md) |
| `VER` | [mcp-server-standard/references/05-verification.md](../../mcp-server-standard/references/05-verification.md) |
| `VIS` | [machine-vision-standard](../../machine-vision-standard/references/rules.md) |
| `WEB` | [web-app-standard](../../web-app-standard/references/rules.md) |
| `WIN` | [desktop-app-standard/references/windows.md](../../desktop-app-standard/references/windows.md)、[05-errors.md](05-errors.md)、[18-process-review-git.md](18-process-review-git.md) |
| `WS` | [mcp-server-standard/references/03-write-safety.md](../../mcp-server-standard/references/03-write-safety.md) |

---

工程开发规范 3.0 · 2026-11-05。规则变更按 0.4 写 ADR，并更新版本号。
