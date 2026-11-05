---
name: machine-vision-standard
description: "Rules for industrial machine vision software: accuracy metrics and acceptance, traceable verdicts and NG images, regression image sets, camera and library isolation, frame pipelines and cycle time, calibration and recipes, fault handling with PLCs, and deep learning models. Use this skill whenever you build or change software that uses industrial cameras for inspection, measurement, guidance or code reading, including HALCON, VisionPro, OpenCV or deep learning defect detection on a production line, or 视觉检测、工业相机、缺陷检测、定位引导、标定、配方、节拍. Not for generic image processing, photo apps or live view without a verdict. Use it together with general-engineering-standard and desktop-app-standard, and hmi-standard when it talks to a PLC or operators work with it."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard and desktop-app-standard; add hmi-standard when it talks to a PLC or operators work with it."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# 视觉软件规范

规则全文在 [references/rules.md](references/rules.md)。这部分还是草稿，级别还可能调整。只显示实时画面、不做判定的软件不适用。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **故障不判 OK**：超时、丢帧、相机断线和算法异常时的动作事先定义，结果没有到达时 PLC 按同样的动作处理（VIS-20）。
2. **视觉不做安全功能**（VIS-22）。
3. **指标事先写明**：漏检和误检分开统计，目标由工艺负责人确认（VIS-01、VIS-02）。
4. **别拿少量样本下结论**：用已知真值的实物评估，写明样本量和置信度；测量类评估偏倚和重复性（VIS-03、VIS-28）。
5. **图像和产品对得上**：计数不一致就停止判定，重新对齐后才恢复（VIS-27）。
6. **配方和标定对得上**：换型时核对配方，相机重连后读回参数，标定有有效期（VIS-17、VIS-35）。
7. **改动要回归**：算法、模型或配方一变就跑带真值的回归图像集（VIS-06、VIS-07）。
8. **判定能追溯**：记录版本和结果，NG 图像能找回（VIS-04、VIS-05）。
9. **赶得上节拍**：按最坏情况设预算，帧不无限堆积（VIS-13、VIS-15）。
10. **发现慢慢变坏**：定期用标准件核对，NG 率偏离基线时报警（VIS-19、VIS-34）。
11. **回放和旁路混不进生产**：回放时不向 PLC 输出；旁路有权限、审计和时限，产品标为未检测（VIS-11、VIS-36）。
12. **发结果要稳妥**：写给 PLC 有握手，定位结果发给机构前核对范围和分数（VIS-21、VIS-29）。
13. **不反复检测到通过**：复判另行记录，不覆盖原结果（VIS-23）。
14. **模型先验证再上线**：用保留图像集或影子运行，能回滚；模型文件按外部数据处理（VIS-25、VIS-26）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 定指标和验收 | [指标与验收](references/rules.md#vis-metrics) |
| 记录判定、保存图像 | [结果可追溯](references/rules.md#vis-trace) |
| 回归图像集 | [回归图像集](references/rules.md#vis-regression) |
| 相机、算法库 | [相机与算法库](references/rules.md#vis-isolation) |
| 帧管道、节拍 | [帧管道与性能](references/rules.md#vis-pipeline) |
| 标定、配方、光照和环境 | [标定、配方与环境](references/rules.md#vis-recipe) |
| 判定、故障、和 PLC 交互 | [判定与故障](references/rules.md#vis-faults) |
| 深度学习模型 | [模型](references/rules.md#vis-models) |
| 发布前 | [发布清单](references/rules.md#vis-checklist) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
