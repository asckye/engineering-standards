# 工程开发规范

通用的工程开发规范（engineering handbook）和配套模板，用中文写成。通用规则放在一处，每类项目有自己的文件夹。

## 怎么选

先读[通用规范](general/README.md)，再加项目类型对应的文件夹：

| 项目类型 | 读这些 | 状态 |
|---|---|---|
| 所有项目 | [general/](general/README.md)：代码规范、注释、易读易维护、错误处理、测试、Git、发布、验收交付、运行运维、退役、AI 协作 | 2.1 |
| MCP 服务 | [mcp/](mcp/README.md) + [desktop/](desktop/README.md) 的本机部分 | 草稿 0.2 |
| 上位机 | [hmi/](hmi/README.md) + [desktop/](desktop/README.md) | 2.1 |
| 视觉 | [vision/](vision/README.md) + [desktop/](desktop/README.md)，需要时加 [hmi/](hmi/README.md) | 草稿 0.2 |
| 大屏 | [dashboard/](dashboard/README.md) + [web/](web/README.md) 或 [desktop/](desktop/README.md) | 草稿 0.2 |
| 桌面应用 | [desktop/](desktop/README.md) | 2.1 |
| Web | [web/](web/README.md) | 2.1 |
| 移动 App | [mobile/](mobile/README.md) | 2.1 |

这些规范都还没有实测数据，也没有外部评审。

语言附录在 [general/languages/](general/README.md#languages)，填写用的模板在 [templates/](templates/)。

## 给谁用

软件项目的维护者、开发者和 AI 编码代理。流程按项目规模和风险取舍：小工具只需最小必做清单、黄金路径和任务手册，对外发布的产品和关键系统采用更多规则。

## 在项目中采用

1. 读[最小必做清单](general/00a-minimum.md)、[黄金路径](general/00b-golden-path.md)、[任务手册](general/00c-playbooks.md)和[快速交付](general/00d-fast-delivery.md)，约 15 分钟。
2. 按 [0.1](general/00-purpose.md#purpose-parts) 和 [0.2](general/00-purpose.md#purpose-tiers) 确定项目的等级（S、M、L）和项目类型，写进项目 README 的“工程规范”一行，并读上表对应的文件夹。
3. 按[第 25 节](general/25-adoption.md)建骨架、构建入口和执行机制。
4. 想把等级、项目类型和长期偏差汇总在一处时，复制 [templates/project-adoption.md](templates/project-adoption.md)。

## 版本与变更

通用规范和各文件夹各自标明版本和状态。版本规则见 [G-07](general/00-purpose.md#purpose-gov)，变更见 [CHANGELOG.md](CHANGELOG.md)。

改动规范后运行 `python build-tools/check_standards.py`，它核对内部链接、规则编号、理由行、第 24 节、版本号和模板里的清单，并确认 MUST 没有比上一个标签放宽。每次推送时 CI 也会运行。

## 路线图

- 通用规范下一版（计划中）：加入实测数据和按项目规模选用的清单。
- MCP 规范：用一个新项目从零试用，再定 1.0。
- 视觉、大屏：各用一个新项目试用，按结果调整规则和级别，再定 1.0。

## 反馈

问题和建议请提 [GitHub Issue](https://github.com/asckye/engineering-standards/issues)。

## 许可

Copyright © 2026 asckye。本仓库的文档以 [CC BY 4.0](LICENSE) 授权，`build-tools/` 里的脚本以 [MIT 许可证](build-tools/LICENSE)授权。

引用或改编时请注明：《工程开发规范》，asckye，CC BY 4.0，并附仓库链接；改动过的内容要说明。
