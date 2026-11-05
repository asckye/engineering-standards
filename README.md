# 工程开发规范

通用的工程开发规范，做成 AI 编码代理可以直接加载的 [Agent Skills](https://agentskills.io)，也可以当文档读。规则用中文写成，都有编号和级别。

## 安装

Claude Code：

```bash
claude plugin marketplace add asckye/engineering-standards
```

```bash
claude plugin install engineering-standards@asckye-standards
```

其他读取 `SKILL.md` 的工具：把 `skills/` 里需要的文件夹复制到工具的 skill 目录（Codex 是 `.agents/skills/`）。最简单是复制全部 8 个文件夹，它们之间有链接，要放在同一个目录下。其他工具还没有测试过。

## 有哪些 skill

| 项目类型 | Skill | 同时用 | 规则全文 | 状态 |
|---|---|---|---|---|
| 所有项目 | [general-engineering-standard](skills/general-engineering-standard/SKILL.md) | | [目录](skills/general-engineering-standard/references/contents.md) | 3.0 |
| MCP 服务 | [mcp-server-standard](skills/mcp-server-standard/SKILL.md) | 桌面的本机部分 | [概述](skills/mcp-server-standard/references/overview.md) | 草稿 0.2 |
| 上位机 | [hmi-standard](skills/hmi-standard/SKILL.md) | 桌面 | [规则](skills/hmi-standard/references/rules.md) | 3.0 |
| 视觉 | [machine-vision-standard](skills/machine-vision-standard/SKILL.md) | 桌面，连 PLC 或供操作员操作时加上位机 | [规则](skills/machine-vision-standard/references/rules.md) | 草稿 0.2 |
| 大屏 | [dashboard-standard](skills/dashboard-standard/SKILL.md) | Web 或桌面 | [规则](skills/dashboard-standard/references/rules.md) | 草稿 0.2 |
| 桌面应用 | [desktop-app-standard](skills/desktop-app-standard/SKILL.md) | | [规则](skills/desktop-app-standard/references/rules.md) | 3.0 |
| Web | [web-app-standard](skills/web-app-standard/SKILL.md) | | [规则](skills/web-app-standard/references/rules.md) | 3.0 |
| 移动 App | [mobile-app-standard](skills/mobile-app-standard/SKILL.md) | | [规则](skills/mobile-app-standard/references/rules.md) | 3.0 |

所有项目都用通用规范。这些规范都还没有实测数据，也没有外部评审。

## 怎么起作用

代理做相关工作时加载对应的 skill。`SKILL.md` 只放最小清单和“正在做什么就读哪个文件”，规则全文在 `references/`，模板在 `assets/`，用到时才读，所以不占太多上下文。

Skill 只能提醒，不能强制：代理可能没加载，也可能没照做。能自动检查的规则仍要放进项目的 CI，见[第 24 节](skills/general-engineering-standard/references/24-enforcement.md)。

## 在项目中采用

1. 读[最小必做清单](skills/general-engineering-standard/SKILL.md#minimum)、[黄金路径](skills/general-engineering-standard/references/00b-golden-path.md)、[任务手册](skills/general-engineering-standard/references/00c-playbooks.md)和[快速交付](skills/general-engineering-standard/references/00d-fast-delivery.md)。
2. 按 [0.1](skills/general-engineering-standard/references/00-purpose.md#purpose-parts) 和 [0.2](skills/general-engineering-standard/references/00-purpose.md#purpose-tiers) 确定项目的等级（S、M、L）和项目类型，写进项目 README 的“工程规范”一行（[T.1](skills/general-engineering-standard/references/appendix/t-templates.md#tpl-readme)），代理靠这一行知道该守哪些规则。
3. 按[第 25 节](skills/general-engineering-standard/references/25-adoption.md)建骨架、构建入口和执行机制。
4. 想把等级、项目类型和长期偏差汇总在一处时，复制[采用记录模板](skills/general-engineering-standard/assets/project-adoption.md)。

## 版本与变更

通用规范和各 skill 各自标明版本和状态。发布时同时改 `.claude-plugin/plugin.json` 的 `version`，已安装插件的人靠它收到更新。版本规则见 [G-07](skills/general-engineering-standard/references/00-purpose.md#purpose-gov)，变更见 [CHANGELOG.md](CHANGELOG.md)。

改动规范后运行 `python build-tools/check_standards.py`，它核对内部链接、规则编号、理由行、第 24 节、版本号、模板里的清单、skill 的基本格式和插件名称，并确认已发布的 MUST 没有被降级、删除或缩小等级范围。检查脚本的测试：`python -m unittest discover -s build-tools`。

`evals/` 里是 skill 的测试用例，用 Claude Code 运行（需要先登录），结果写到 `evals/results/`：

```bash
claude plugin eval . --allow-tools Write --no-publish
```

## 路线图

- 通用规范下一版（计划中）：加入实测数据和按项目规模选用的清单。
- MCP 规范：用一个新项目从零试用，再定 1.0。
- 视觉、大屏：各用一个新项目试用，按结果调整规则和级别，再定 1.0。

## 反馈

问题和建议请提 [GitHub Issue](https://github.com/asckye/engineering-standards/issues)。

## 许可

Copyright © 2026 asckye。本仓库的文档、skill 和测试用例以 [CC BY 4.0](LICENSE) 授权，`build-tools/` 里的脚本以 [MIT 许可证](build-tools/LICENSE)授权。

引用或改编时请注明：《工程开发规范》，asckye，CC BY 4.0，并附仓库链接；改动过的内容要说明。
