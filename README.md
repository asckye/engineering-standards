# 工程开发规范

通用的工程开发规范（engineering handbook）和配套模板，用中文写成。当前版本 1.1（2026-11-02）。

## 这是什么

- [手册](handbook/README.md)：项目通用部分（第 0–26 节）对任何语言和技术栈有效；领域规范 A–F（MCP 服务、上位机、工程软件自动化、桌面、Web、移动）和语言附录 L1–L3（C#/.NET、TypeScript/JavaScript、Python）按需采用。
- [模板](templates/)：任务说明、架构决策记录（ADR）、评审清单、完成定义、发布清单和项目采用文件，复制后填写。

## 给谁用

软件项目的维护者、开发者和 AI 编码代理。流程按项目规模和风险取舍：小工具只需最小必做清单、黄金路径和任务手册，对外发布的产品和关键系统采用更多规则。

## 在项目中采用

1. 读[最小必做清单](handbook/general/00a-minimum.md)、[黄金路径](handbook/general/00b-golden-path.md)、[任务手册](handbook/general/00c-playbooks.md)和[快速交付](handbook/general/00d-fast-delivery.md)，约 15 分钟。
2. 按 [0.1](handbook/general/00-purpose.md#purpose-parts) 和 [0.2](handbook/general/00-purpose.md#purpose-tiers) 确定项目的等级（S、M、L）和领域，写进项目 README 的“工程规范”一行。
3. 按[第 25 节](handbook/general/25-adoption.md)建骨架、构建入口和执行机制。
4. 想把等级、领域和长期偏差汇总在一处时，复制 [templates/project-adoption.md](templates/project-adoption.md)。

## 版本与变更

版本规则见 [G-07](handbook/general/00-purpose.md#purpose-gov)。本仓库的变更见 [CHANGELOG.md](CHANGELOG.md)，手册内的记录见[规范变更记录](handbook/appendix/changelog.md)。

## 路线图

- 1.2（计划中）：加入实测数据和按项目规模选用的清单。

## 许可

Copyright © 2026 asckye。本仓库的文档以 [CC BY 4.0](LICENSE) 授权。今后如加入脚本，脚本以 MIT 许可证授权。
