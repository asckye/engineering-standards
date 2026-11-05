# <a id="playbooks"></a>★ 任务手册

> **要点** 日常工作按手册走，不必先读章节。每一步链接到规则，遇到问题再查。

## <a id="play-new"></a>新建项目

1. 定等级（S/M/L）和领域，写进 README（[T.1](../appendix/t-templates.md#tpl-readme)）。
2. 按黄金路径建骨架、构建入口、锁文件、分析器和格式化配置（[★ 黄金路径](00b-golden-path.md#golden)）。
3. 建合并门命令和 CI，让第一条测试在两分钟内跑完（[★ 快速交付](00d-fast-delivery.md#fast)）。
4. 写代理说明（[T.8](../appendix/t-templates.md#tpl-agents)），复制术语表（[附录](../appendix/glossary.md#glossary)）。
5. [M+] 写 ADR 0001“采用本规范”、`SECURITY.md`、`THIRD-PARTY-NOTICES`。
6. 用“新增功能”手册做第一个功能。

## <a id="play-feature"></a>新增功能

1. 写需求与验收标准（[18.2](18-process-review-git.md#review-req)）。
2. L2 且 [M+]：一页设计说明，维护者批准（[T.3](../appendix/t-templates.md#tpl-rfc)）。
3. 拆成可独立合并的任务，每个写任务说明（[T.4](../appendix/t-templates.md#tpl-task)）。
4. 先把验收标准写成测试，再实现；只在边界校验（P-21）。
5. 内循环：构建 + 相关测试，两分钟内反馈。
6. 提交 PR（[T.5](../appendix/t-templates.md#tpl-pr)）；评审（[18.5](18-process-review-git.md#review-code)）；合并门。
7. CHANGELOG、文档、实机核对清单同步（[第 23 节](23-definition-of-done.md#dod)）。

## <a id="play-bug"></a>修复缺陷

1. 登记（[T.6](../appendix/t-templates.md#tpl-bug)），按 S1–S3 分级；S1 先用配置停用相关功能（[13.1](13-defects.md#bugs-triage)）。
2. 归类：真实缺陷、不稳定测试、环境、本分支回归（BUG-03）。
3. 复现并定位根因；不试错（BUG-04）。
4. 写一个修复前失败的测试（BUG-02）。
5. 最小修复，内循环通过，评审与合并门。
6. [M+] S1 写复盘（BUG-06）。

## <a id="play-refactor"></a>重构

1. 写明“行为不变”的范围和目的（可读性、去重复、为某个功能铺路）。
2. 先补对等测试，锁住现有行为（Q-17）。
3. 单独成批，不混入行为变化；新旧路径并存（Q-18）。
4. 小步合并，每步过合并门；对等测试通过后删除旧路径。

## <a id="play-dep"></a>增加依赖

1. 先确认标准库或已有依赖做不到。
2. 核对许可证（DEP-02）、维护状况、体积与传递依赖。
3. 精确锁定版本并入锁文件（DEP-03）；离线还原可用（DEP-04）。
4. 更新 `THIRD-PARTY-NOTICES`（DEP-06）；[M+] 更新 SBOM（DEP-11）。
5. [M+] 运行时依赖经维护者批准，写一行理由或 ADR。

## <a id="play-release"></a>发布

1. 维护者确认版本号和范围；发布期间不改代码（BLD-07）。
2. 核对发布证据：[M+] 最近一次夜间检查通过且之后无失败。
3. 生成发布说明和“未验证”清单（[T.7](../appendix/t-templates.md#tpl-release)），核对支持矩阵。
4. 由发布命令改版本号、打包、算 SHA-256；[M+] 生成 SBOM。
5. 预发布标为预发布、不设为最新；附测试清单与反馈模板（PKG-08）。
6. 上传后更新交接文档与发布记录。

## <a id="play-hotfix"></a>热修复

1. S1 先用配置停用受影响的功能，告知用户。
2. 在主干上按“修复缺陷”手册修复，带回归测试。
3. 合并门加受影响的实机核对；发布修订版本（`X.Y.Z+1`）。
4. 发布说明写清影响范围和升级要求；复盘。

## <a id="play-onboard"></a>新成员或新代理入门

1. 读最小必做清单、黄金路径和本手册（约 15 分钟）。
2. 读项目的代理说明、交接文档和术语表。
3. 本机跑一次构建和合并门，确认环境可用。
4. 代理：只接收按 T.4 写的任务说明，遵守 [19.4](19-ai.md#ai-machine) 的开发机规则。
5. 第一个任务选 L1（小修复或补测试），走完整的评审与合并。

---

[← 上一节：★ 黄金路径与默认技术决策](00b-golden-path.md) · [目录](../README.md) · [下一节：★ 快速交付 →](00d-fast-delivery.md)
