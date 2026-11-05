---
name: desktop-app-standard
description: "Rules for desktop apps and other software that runs on a user's or site machine: MVVM and the UI thread, local data and backups, local HTTP and named pipes, per-user install, signed updates and rollback, uninstall, crash logs and diagnostic bundles, Windows paths, file locks, job objects and encoding. Use this skill whenever you build or change a WPF, WinUI, Electron, .NET MAUI or other desktop app, an installer or updater, a local service, or a tool shipped to run on other people's machines, including 桌面应用、本机软件、安装包、自动更新、上位机界面. Use it together with general-engineering-standard."
license: CC-BY-4.0
compatibility: "Use together with general-engineering-standard."
metadata:
  source: "https://github.com/asckye/engineering-standards"
---

# 桌面与本机软件规范

规则全文在 `references/`。MCP 服务、上位机和视觉软件也用其中的本机软件、Windows、打包和诊断部分。

级别的含义、例外和评审做法见 `general-engineering-standard`。这里的规则比通用规范更具体，冲突时以这里为准，但除了 `references/` 里明确写明的例外，这里不放宽别处的 MUST。在设计、评审和报告里写规则编号，让人能查到原文。MUST 做不到时不要悄悄跳过，告诉维护者。

## 最小清单

开工时先看这几条，它们防的是这类项目最严重的问题。这份清单只是入口，不改变任何规则的级别，其余规则照常适用。

1. **界面不卡**：界面线程不做 IO、不阻塞等待，长操作显示进度并可取消（DSK-02）。
2. **用户的文件不丢**：覆盖或删除前先备份并核对副本；改用户的配置文件前先展示内容（DAT-02、DAT-03）。
3. **数据不离开这台电脑**：没有人明确同意，日志、崩溃转储和使用统计都不上传（DAT-06、DIAG-01）。
4. **本机服务不外露**：HTTP 默认只听 `127.0.0.1`，请求带密钥，校验 `Origin` 和 `Host`（SEC-15、SEC-16、SEC-17）。
5. **本机管道只给当前用户**：拒绝远程客户端，核对对方身份（SEC-14）。
6. **密钥放受保护的存储**：不写进明文配置（SEC-19）。
7. **更新安全**：更新器核对发布者签名和哈希，失败自动回滚，不动用户数据（MIG-05）。
8. **卸载不删数据**：卸载保留用户数据并说明位置，删除数据要单独确认（PKG-04）。
9. **进程不乱来**：启动的子进程放进作业对象，只结束自己启动的进程（WIN-13、WIN-14）。
10. **崩溃有线索**：未处理异常写日志并给出诊断编号（DIAG-04）。
11. **键盘和对比度达标**：全部功能可用键盘完成，对比度达标，不只靠颜色传达信息（UI-10、UI-13、UI-24）。
12. **用 Electron 时**：开启隔离和沙箱，不加载远程内容执行代码（DSK-09）。

## 按任务读规则

只读和当前任务有关的部分。

| 正在做 | 读 |
|---|---|
| 架构、界面线程、MVVM | [桌面应用的规则](references/rules.md#desktop-rules) |
| 界面：窗口、字体、颜色、键盘、界面测试 | [桌面界面](references/ui.md)，以及通用规范第 21 节 |
| 本机管道和 HTTP | [6.6](references/local-software.md#security-ipc) |
| 用户数据、备份、权限、数据目录 | [本机运行的软件](references/local-software.md) |
| 路径、文件锁、杀毒软件、编码、进程、PATH | [Windows 平台](references/windows.md) |
| 安装、更新、卸载 | [打包与安装](references/packaging.md) |
| 崩溃、日志、诊断包 | [诊断与支持](references/diagnostics.md) |
| 发布前 | [桌面发布清单](references/rules.md#pd-checklist) |

---

《工程开发规范》，asckye，CC BY 4.0，https://github.com/asckye/engineering-standards
