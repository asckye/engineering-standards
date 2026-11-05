# <a id="glossary"></a>附录：术语表

- **SHOULD** `G-11` 一个概念一个词，在代码、界面和文档中一致。每个项目复制本表到 `docs/standards/glossary.md`，再补充自己的领域术语。

| 中文 | English | 代码中 | 说明与避免的说法 |
|---|---|---|---|
| 服务 | service | `Host`、`Service` | 面向用户的总称；不说“引擎” |
| 项目 | project | `Project` | 目标软件中的工程文件；不说“工程” |
| 目标（目标软件） | target (target software) | `Target` | 被接入或被自动化的软件或设备 |
| 厂商 API | vendor API | `Adapter` | 只在适配层出现 |
| 写入 | write | `Write` | 任何改变目标、设备、配置或用户文件的操作 |
| 预览 | preview | `dryRun` | 不写入，返回变更清单 |
| 审批 | approval | `Approval` | 人在独立界面对写入请求作决定；不说“授权” |
| 确认 | confirmation | `Confirm` | 人对自己发起的操作再次确认 |
| 读回 | readback | `Readback`、`Verify` | 写入后读取实际状态比较 |
| 回滚 | rollback | `Rollback` | 撤销未提交的写入 |
| 结果未知 | outcome unknown | `OUTCOME_UNKNOWN` | 写入已发出、结果无法确认；禁止重放 |
| 边界 | boundary | 无 | 校验发生的位置（1.3） |
| 请求号 | request id | `requestId` | 一次操作的关联标识 |
| 诊断编号 | diagnostic id | `diagnosticId` | 把对外失败关联到日志 |
| 审计 | audit trail | `Audit` | 只追加的操作记录；与运行日志分开 |
| 基线 | baseline | `Baseline` | 快照、警告存量等只由工具更新的参照 |
| 门禁 | gate | `Gate` | 阻止合并或发布的检查集合；合并门、发布门 |
| 夜间检查 | nightly | `Nightly` | 每日冷启动的完整检查 |
| 台账 | ledger | 无 | 实机验证结果的记录 |
| 等级 | tier | 无 | 项目等级 S、M、L |
| 项目类型规范 | profile | 无 | 根目录按项目类型分的文件夹；“配置”只指 configuration |
| 配置 | configuration | `Options`、`Config` | 启动时读取的设置来源（第 8 节） |
| 设置 | settings | `Settings` | 用户可改的选项 |
| 报警确认 | acknowledge | `Acknowledge` | 操作员确认报警；不与“确认”混用 |
| 运行手册 | runbook | — | 启动、停止、故障处置和恢复的步骤文档 |
| 事故 | incident | — | 已经影响用户或现场的问题；级别按 13.1 |
| 告警 | alert | — | 发给运行负责人的通知；不与操作员的“报警”混用 |
| 回退 | rollback（部署） | — | 退回上一个版本或系统；不同于撤销未提交写入的“回滚” |
| 工厂验收 | factory acceptance test（FAT） | — | 出厂前用真实控制器或仿真核对功能 |
| 现场验收 | site acceptance test（SAT） | — | 在现场核对系统已按规范和安装要求安装，并接真实设备核对。IEC 62381 把子系统联调单列为现场集成测试（SIT），逐点回路检查见 IEC 62382；本规范的现场验收包含这些部分 |
| 恢复时间目标 | recovery time objective（RTO） | — | 故障后多久要恢复 |
| 恢复点目标 | recovery point objective（RPO） | — | 恢复后最多丢失多长时间的数据 |
| 退役 | retirement | — | 产品停止运行并收尾；和“停止支持”不同，后者只是不再修复 |

---

[目录](../README.md)
