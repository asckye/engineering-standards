# <a id="windows"></a>9 Windows 平台

> **要点** 长路径、文件锁、杀毒软件、编码和进程管理是 Windows 上最常见的故障来源；照做可以省掉大部分排查时间。

只对在 Windows 上运行或构建的项目。规则来自真实项目中反复出现的故障。

## <a id="windows-paths"></a>9.1 长路径与路径规范化

- **SHOULD** `WIN-01` 假设 `LongPathsEnabled=0`：安装根、数据根、构建输出和临时目录的深度保持很小；产品内部固定子路径预留余量。路径超过 260 字符时立即以明确的错误失败，不产生半截文件。

## <a id="windows-files"></a>9.2 文件锁与原子替换

- **SHOULD** `WIN-06` 遇到共享冲突（被其他进程打开）时有界重试并报告占用者能识别的信息；升级时不强制结束正在写入的进程。

## <a id="windows-av"></a>9.3 杀毒软件干扰

- **SHOULD** `WIN-07` 假设杀毒软件会短暂锁定刚写入的可执行文件和压缩包：替换、删除、加载新文件时有界重试；构建与测试不依赖“写完立刻能执行”。

## <a id="windows-encoding"></a>9.4 编码与区域

- **SHOULD** `WIN-10` 读写文件和管道显式指定编码；不依赖控制台代码页。子进程的输出按约定的 UTF-8 读取；必须读取旧程序输出时，按其实际代码页（例如 cp936、cp1252）显式解码。

## <a id="windows-crlf"></a>9.5 换行策略

- **SHOULD** `WIN-12` 仓库设置 `core.autocrlf=false`，换行由 `.gitattributes`（`* text=auto eol=lf`）决定；需要 BOM 或 CRLF 的文件逐项声明。

## <a id="windows-process"></a>9.6 进程树与作业对象

- **MUST** `WIN-13` 产品启动的子进程放进作业对象，设置 `JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`；需要比宿主活得久的进程（例如用户的目标软件实例）显式脱离作业。
  - 理由 · 孤儿子进程会占住目标实例和文件。
- **MUST NOT** `WIN-14` 按进程名、窗口标题或模式匹配结束进程。只结束自己启动的进程：记录 PID 和启动时间，结束前核对可执行文件路径。
  - 理由 · 按名称结束进程会关掉用户的其他程序。
- **MUST** `WIN-15` 测试夹具和辅助进程关闭 Windows 错误报告对话框：`SetErrorMode(SEM_FAILCRITICALERRORS | SEM_NOGPFAULTERRORBOX)`，并注册未处理异常处理程序，把异常写入 stderr 后以约定的非零退出码退出，不弹出 WER 对话框阻塞无人值守运行。
  - 理由 · WER 对话框会让无人值守的运行一直挂起。

## <a id="windows-env"></a>9.7 环境变量与 PATH

---

[← 上一节：8 配置与环境](08-configuration.md) · [目录](../README.md) · [下一节：10 国际化与本地化 →](10-i18n.md)
