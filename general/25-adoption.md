# <a id="adopt"></a>25 在新项目中采用

> **要点** 照黄金路径和模板建项目，半天内可以开工。

1. 确定等级（S、M、L）和项目类型（根目录的文件夹，见 [0.1](00-purpose.md#purpose-parts)），写进 README 的“工程规范”一行，并读对应文件夹的规范。
2. 建目录骨架（2.6），加入 `.editorconfig`、`.gitattributes`（`* text=auto eol=lf`）、`core.autocrlf=false`、分析器与格式化配置、中央版本管理和锁文件。
3. 在 `build-tools/` 建唯一入口，至少提供 `build`、`test`、`check`（合并门）、`package`。
4. 加入执行机制（24 节表格中本等级需要的行）：架构测试、仓库检查、密钥扫描、套件注册表、PR 模板。
5. 写 `CHANGELOG.md`、`SECURITY.md` [M+]、`THIRD-PARTY-NOTICES`，以及 ADR 0001“采用工程开发规范 <版本> 与项目类型 X”。[M+] 开启多因素认证（SEC-43）；面向欧盟用户时写 CRA 的 ADR（SEC-44）。
6. 写简短的代理说明文件（模板 [T.8](appendix/t-templates.md#tpl-agents)），只放规范版本、等级、项目类型和项目特有的规则；复制术语表并补充领域术语。

---

[← 上一节：24 让规则可执行](24-enforcement.md) · [目录](README.md) · [下一节：26 通用检查清单 →](26-checklists.md)
