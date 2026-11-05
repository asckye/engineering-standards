# 工程开发规范

维护者今后全部项目的通用工程规范。项目通用部分对任何语言和技术栈有效（部分规则按 Windows/.NET 写成，见 0.1）；领域规范（MCP 服务、上位机、工程软件自动化、桌面、Web、移动）和语言附录按需采用。代码质量第一，流程按项目规模和风险取舍。

版本 1.1 · 2026-11-02 · [最小必做清单](general/00a-minimum.md#minimum)约 3 分钟；加上黄金路径、任务手册与快速交付约 15 分钟；全文浏览约 30–35 分钟（模板、术语表、参考资料和其他语言的附录供查阅）。

用语：**MUST** 必须 · **SHOULD** 默认，偏离写理由 · **MAY** 允许 · [M+] 只对该等级及以上的项目（S/M/L，见 0.2）

## 目录

### 项目通用部分

- 0 [目的、等级与读法](general/00-purpose.md)
- ★ [最小必做清单](general/00a-minimum.md)
- ★ [黄金路径与默认技术决策](general/00b-golden-path.md)
- ★ [任务手册](general/00c-playbooks.md)
- ★ [快速交付](general/00d-fast-delivery.md)
- 1 [工程原则](general/01-principles.md)
- 2 [架构](general/02-architecture.md)
- 3 [代码规范](general/03-code.md)
- 4 [代码质量](general/04-quality.md)
- 5 [错误处理与健壮性](general/05-errors.md)
- 6 [安全](general/06-security.md)
- 7 [用户数据与隐私](general/07-privacy.md)
- 8 [配置与环境](general/08-configuration.md)
- 9 [Windows 平台](general/09-windows.md)
- 10 [国际化与本地化](general/10-i18n.md)
- 11 [性能](general/11-performance.md)
- 12 [测试](general/12-testing.md)
- 13 [缺陷处理](general/13-defects.md)
- 14 [依赖与许可](general/14-dependencies.md)
- 15 [构建、验证与发布](general/15-build-release.md)
- 16 [打包与安装](general/16-packaging.md)
- 17 [兼容、升级与迁移](general/17-compatibility.md)
- 18 [开发流程、评审与 Git](general/18-process-review-git.md)
- 19 [AI 辅助开发](general/19-ai.md)
- 20 [文档](general/20-documentation.md)
- 21 [界面设计](general/21-ui.md)
- 22 [诊断与支持](general/22-diagnostics.md)
- 23 [完成定义](general/23-definition-of-done.md)
- 24 [让规则可执行](general/24-enforcement.md)
- 25 [在新项目中采用](general/25-adoption.md)
- 26 [通用检查清单](general/26-checklists.md)

### 领域规范

- A [领域：MCP 服务](domains/a-mcp.md)
- B [领域：上位机](domains/b-industrial-hmi.md)
- C [领域：工程软件自动化](domains/c-vendor-api.md)
- D [领域：桌面应用](domains/d-desktop.md)
- E [领域：Web 开发](domains/e-web.md)
- F [领域：移动 App](domains/f-mobile.md)

### 语言附录

- L1 [附录：C#/.NET](languages/l1-csharp.md)
- L2 [附录：TypeScript/JavaScript](languages/l2-typescript.md)
- L3 [附录：Python](languages/l3-python.md)

### 模板、术语与参考

- T [附录：模板](appendix/t-templates.md)
- 术 [附录：术语表](appendix/glossary.md)
- 附 [参考资料](appendix/references.md)
- 变 [规范变更记录](appendix/changelog.md)

## 按规则编号查找

规则编号的前缀对应下列文件。

| 前缀 | 文件 |
|---|---|
| `G` | [00-purpose.md](general/00-purpose.md)、[glossary.md](appendix/glossary.md) |
| `FAST` | [00d-fast-delivery.md](general/00d-fast-delivery.md) |
| `P` | [01-principles.md](general/01-principles.md) |
| `ARC` | [02-architecture.md](general/02-architecture.md) |
| `CODE` | [03-code.md](general/03-code.md) |
| `Q`、`CMT` | [04-quality.md](general/04-quality.md) |
| `ERR` | [05-errors.md](general/05-errors.md) |
| `SEC` | [06-security.md](general/06-security.md) |
| `DAT` | [07-privacy.md](general/07-privacy.md) |
| `CFG` | [08-configuration.md](general/08-configuration.md) |
| `WIN` | [09-windows.md](general/09-windows.md) |
| `I18N` | [10-i18n.md](general/10-i18n.md) |
| `PERF` | [11-performance.md](general/11-performance.md) |
| `TST` | [12-testing.md](general/12-testing.md) |
| `BUG` | [13-defects.md](general/13-defects.md) |
| `DEP` | [14-dependencies.md](general/14-dependencies.md) |
| `BLD` | [15-build-release.md](general/15-build-release.md) |
| `PKG` | [16-packaging.md](general/16-packaging.md) |
| `MIG` | [17-compatibility.md](general/17-compatibility.md) |
| `REQ`、`REV`、`GIT` | [18-process-review-git.md](general/18-process-review-git.md) |
| `AI` | [19-ai.md](general/19-ai.md) |
| `DOC` | [20-documentation.md](general/20-documentation.md) |
| `UI` | [21-ui.md](general/21-ui.md) |
| `DIAG` | [22-diagnostics.md](general/22-diagnostics.md) |
| `ENF` | [24-enforcement.md](general/24-enforcement.md) |
| `MCP` | [a-mcp.md](domains/a-mcp.md) |
| `IND` | [b-industrial-hmi.md](domains/b-industrial-hmi.md) |
| `VND` | [c-vendor-api.md](domains/c-vendor-api.md) |
| `DSK` | [d-desktop.md](domains/d-desktop.md) |
| `WEB` | [e-web.md](domains/e-web.md) |
| `MOB` | [f-mobile.md](domains/f-mobile.md) |

---

工程开发规范 1.1 · 2026-11-02 · 由维护者在已运行项目中采纳的决定（ADR、标准文档、评审结论）推广而来。规则变更按 0.4 写 ADR，并更新版本号。
