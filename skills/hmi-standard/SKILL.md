---
name: hmi-standard
description: "Rules for HMI, SCADA and operator software that talks to PLCs, instruments and drives: the safety boundary, communication failure and safe state, data quality and timestamps, confirmed and read-back writes, alarms per ISA-18.2, screens per ISA-101, roles and audit, history, 24/7 stability, IEC 62443 basics, commissioning and site acceptance. Use this skill whenever you build or change software that reads from or writes to industrial devices over Modbus, OPC UA or similar, including operator screens, alarm handling, setpoint or command writes and data logging, or 上位机、组态、操作员界面、报警、写入 PLC 变量、设定值. Not for writing PLC programs themselves. Use it together with general-engineering-standard and desktop-app-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard and desktop-app-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# 上位机规范

规则全文在 [references/rules.md](references/rules.md)。等级标记照常适用；7×24 运行的产线系统通常是 L 级。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **软件不做安全功能**：人员和设备安全靠安全 PLC 和硬接线联锁，软件不绕过、不屏蔽（IND-01、IND-02）。
2. **断线时设备安全**：每条写入路径事先定义通信中断时的安全状态，由工艺负责人确认（IND-03）。
3. **通信不卡死**：每次读写有超时，断线后按退避重连，不做紧密循环（IND-05）。
4. **数据看得出好坏**：每个值带质量和时间戳，坏值和过期值不显示成正常（IND-09）。
5. **写入前确认和检查**：显示设备、变量、旧值、新值和单位；量程和允许条件不通过就不发送（IND-14、IND-15）。
6. **写入后核对**：设定值读回，命令按设备反馈的状态核对（IND-16）。
7. **结果未知不重发**：运动命令每次都要操作员明确动作（IND-17）。
8. **接口版本对得上**：PLC 接口数据块带版本字，不匹配就拒绝写入（IND-42）。
9. **报警压不住**：不提供确认全部，搁置有时限和原因（IND-20）。
10. **操作查得到**：角色按最小权限，操作员动作有防篡改的审计（IND-26、IND-27）。
11. **历史数据不造假**：数据缺口明确记录，不跨中断插值（IND-30）。
12. **能长期运行**：做浸泡测试；磁盘将满时报警，不停止采集（IND-32、IND-34）。
13. **坏了能恢复**：配置能导出备份并恢复，恢复流程测过（IND-40）。
14. **现场实测**：逐点核对变量，实测断网、PLC 停机、重启和断电（IND-44、IND-46）。
15. **现场调试有人负责**：工艺负责人确认范围和安全条件并在场，AI 代理不写入现场设备，调试用的强制值交付前撤销（IND-45）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 判断什么算安全功能 | [B.1 安全功能边界](references/rules.md#pb-safety) |
| 设备通信、超时、重连 | [B.2 设备通信](references/rules.md#pb-comm) |
| 采集、数据质量 | [B.3 数据与采集](references/rules.md#pb-data) |
| 写入设备 | [B.4 写入设备](references/rules.md#pb-write) |
| 报警 | [B.5 报警管理](references/rules.md#pb-alarm) |
| 操作画面 | [B.6 操作画面](references/rules.md#pb-hmi) |
| 用户、权限、操作记录 | [B.7 用户、权限与记录](references/rules.md#pb-users) |
| 历史数据、时间 | [B.8 历史数据与时间](references/rules.md#pb-hist) |
| 长期稳定运行 | [B.9 7×24 稳定性](references/rules.md#pb-247) |
| 网络安全 | [B.10 网络安全](references/rules.md#pb-62443) |
| 离线部署、仿真 | [B.11 离线现场部署与仿真](references/rules.md#pb-deploy) |
| 硬件在环测试 | [B.12 硬件在环测试清单](references/rules.md#pb-checklist) |
| 工厂验收、现场验收 | [B.13 工厂验收与现场验收](references/rules.md#pb-acceptance) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
