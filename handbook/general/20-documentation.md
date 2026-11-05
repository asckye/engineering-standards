# <a id="docs"></a>20 文档

> **要点** 文档只写当前行为，决定写 ADR，数字由生成器产出。

## <a id="docs-structure"></a>20.1 结构与语言

- **SHOULD** `DOC-01` 仓库根有 `README.md`（做什么、怎么安装、怎么用、支持矩阵）；需要时另有 `README.zh-CN.md`。
- **SHOULD** `DOC-03` 每个仓库写明语言政策，并且一个文件只用一种语言。默认：开发文档与用户文档用中文；发布记录、代码注释、面向机器或模型的文本用英文。

## <a id="docs-adr"></a>20.2 ADR

- **SHOULD** `DOC-04` ADR 放在 `docs/adr/NNNN-<short-title>.md`，四位递增编号不复用；一页一个决定；字段：状态、日期、决策者、背景、选项、决定、后果、置信度、相关链接。
- **SHOULD** `DOC-05` ADR 只追加：已采纳的不改写正文；决定改变时写新 ADR 取代旧的，两边互链。状态：提议、已采纳、已拒绝、已被 NNNN 取代、已废弃。目录 README 列出全部 ADR。

## <a id="docs-generated"></a>20.3 生成文档

规则见 [`P-26`](01-principles.md#principles-truth)。

## <a id="docs-style"></a>20.4 写作

- **SHOULD** `DOC-08` 按 Microsoft Writing Style Guide：先结论和下一步，短句，常用词；中文用“选择”而不是“点击”，用“你”而不是“您”；中英文与数字之间空一格。
- **SHOULD** `DOC-09` 文档只描述当前行为；历史在 Git 和发布记录中。开发文档开头写状态行（现行、部分过时、历史记录）和最后核对日期。

## <a id="docs-status"></a>20.5 交接、计划与变更记录

- **MUST** `DOC-06` 用户可见的变化当次写入 `CHANGELOG.md` 的 `Unreleased`（Keep a Changelog 格式，英文）。
  - 理由 · 发布时补写 CHANGELOG 会遗漏变化。
- **SHOULD** `DOC-11` [M+] `docs/plan/progress.md` 记当前事实（主干提交、进行中的任务、阻塞项）；`docs/plan/plan.md` 记范围、任务状态和放行条件；临时收件箱里的决定当天转写到计划或 ADR。机器地址和进程号从当前环境确认，不从旧文档推断。

---

[← 上一节：19 AI 辅助开发](19-ai.md) · [目录](../README.md) · [下一节：21 界面设计 →](21-ui.md)
