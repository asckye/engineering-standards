# 通用规范

所有项目都适用的规范：代码规范、注释、易读易维护、错误处理、安全、测试、依赖、构建与发布、开发流程和 AI 协作。每类项目专属的规则在根目录各自的文件夹，见 [0.1](00-purpose.md#purpose-parts)。代码质量第一，流程按项目规模和风险取舍。

版本 2.0 · 2026-11-05 · [最小必做清单](00a-minimum.md)约 3 分钟；加上黄金路径、任务手册与快速交付约 15 分钟。

用语：**MUST** 必须 · **SHOULD** 默认，偏离写理由 · **MAY** 允许 · [M+] 只对该等级及以上的项目（S/M/L，见 0.2）

## 目录

第 9 节（Windows 平台）、第 16 节（打包与安装）和第 22 节（诊断与支持）在 [desktop/](../desktop/README.md)，A 和 C 领域由 [mcp/](../mcp/README.md) 取代，其余编号不变。

- [0 目的、等级与读法](00-purpose.md)
- [★ 最小必做清单](00a-minimum.md)
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

## <a id="languages"></a>语言附录

- [附录 L1：C#/.NET](languages/l1-csharp.md)
- [附录 L2：TypeScript/JavaScript](languages/l2-typescript.md)
- [附录 L3：Python](languages/l3-python.md)

## 模板、术语与参考

- [附录 T：模板](appendix/t-templates.md)
- [附录：术语表](appendix/glossary.md)
- [参考资料](appendix/references.md)
- [规范变更记录](appendix/changelog.md)

## 按规则编号查找

规则编号的前缀对应下列文件，包括各项目类型的文件夹。

| 前缀 | 文件 |
|---|---|
| `AI` | [general/19-ai.md](19-ai.md) |
| `ARC` | [general/02-architecture.md](02-architecture.md) |
| `BLD` | [general/15-build-release.md](15-build-release.md) |
| `BUG` | [general/13-defects.md](13-defects.md) |
| `CFG` | [desktop/local-software.md](../desktop/local-software.md)、[general/08-configuration.md](08-configuration.md) |
| `CMT` | [general/04-quality.md](04-quality.md) |
| `CODE` | [general/03-code.md](03-code.md) |
| `DAT` | [desktop/local-software.md](../desktop/local-software.md)、[general/07-privacy.md](07-privacy.md) |
| `DEP` | [general/14-dependencies.md](14-dependencies.md) |
| `DIAG` | [desktop/diagnostics.md](../desktop/diagnostics.md) |
| `DOC` | [general/20-documentation.md](20-documentation.md) |
| `DSH` | [dashboard/README.md](../dashboard/README.md) |
| `DSK` | [desktop/README.md](../desktop/README.md) |
| `ENF` | [general/24-enforcement.md](24-enforcement.md) |
| `ENG` | [mcp/04-engineering-adapters.md](../mcp/04-engineering-adapters.md) |
| `ERR` | [general/05-errors.md](05-errors.md) |
| `FAST` | [general/00d-fast-delivery.md](00d-fast-delivery.md) |
| `G` | [general/00-purpose.md](00-purpose.md)、[general/appendix/glossary.md](appendix/glossary.md) |
| `GIT` | [general/18-process-review-git.md](18-process-review-git.md) |
| `I18N` | [general/10-i18n.md](10-i18n.md) |
| `IND` | [hmi/README.md](../hmi/README.md) |
| `MIG` | [desktop/packaging.md](../desktop/packaging.md)、[general/17-compatibility.md](17-compatibility.md) |
| `MOB` | [mobile/README.md](../mobile/README.md) |
| `P` | [general/01-principles.md](01-principles.md) |
| `PERF` | [general/11-performance.md](11-performance.md) |
| `PKG` | [desktop/packaging.md](../desktop/packaging.md)、[general/15-build-release.md](15-build-release.md) |
| `PRO` | [mcp/01-protocol.md](../mcp/01-protocol.md) |
| `Q` | [general/04-quality.md](04-quality.md) |
| `REQ` | [general/18-process-review-git.md](18-process-review-git.md) |
| `REV` | [general/18-process-review-git.md](18-process-review-git.md) |
| `SEC` | [desktop/local-software.md](../desktop/local-software.md)、[general/06-security.md](06-security.md) |
| `TL` | [mcp/02-tool-design.md](../mcp/02-tool-design.md) |
| `TST` | [general/12-testing.md](12-testing.md) |
| `UI` | [desktop/ui.md](../desktop/ui.md)、[general/21-ui.md](21-ui.md) |
| `VER` | [mcp/05-verification.md](../mcp/05-verification.md) |
| `VIS` | [vision/README.md](../vision/README.md) |
| `WEB` | [web/README.md](../web/README.md) |
| `WIN` | [desktop/windows.md](../desktop/windows.md)、[general/05-errors.md](05-errors.md)、[general/18-process-review-git.md](18-process-review-git.md) |
| `WS` | [mcp/03-write-safety.md](../mcp/03-write-safety.md) |

---

工程开发规范 2.0 · 2026-11-05 · 由维护者在已运行项目中采纳的决定（ADR、标准文档、评审结论）推广而来。规则变更按 0.4 写 ADR，并更新版本号。
