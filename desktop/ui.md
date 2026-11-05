# 桌面界面

> **要点** [第 21 节](../general/21-ui.md)的原则和规则对所有带界面的项目有效。这里是按桌面写成的值和规则，用于桌面应用和上位机。

## <a id="ui-token-values"></a>21.2 Token 参考值

| 类别 | Token（值） |
|---|---|
| 间距（4 px 网格） | `space-1` 4 · `space-2` 8 · `space-3` 12 · `space-4` 16 · `space-5` 20 · `space-6` 24 · `space-8` 32（页面左右边距） |
| 尺寸 | `control-sm` 28 · `control-md` 32（普通控件）· `control-lg` 44（决策按钮、确认面板按钮）· 行高：密集数据或桌面表格 36，触控或宽松列表 44，每个产品选定一种 · `sheet-width` 420 |
| 圆角 | `radius-xs` 4（复选框）· `radius-sm` 6 · `radius-md` 8（按钮、输入框）· `radius-lg` 12（卡片、面板、提示条）· `radius-full`（开关、徽标） |
| 层级与边框 | 卡片以 0.5–1 px 细描边为主几乎无投影；只有确认面板和提示条用 `shadow-sheet`；高对比下去掉全部阴影，改用 1 px `hc-outline` |
| 时长 | `duration-fast` 150 ms（选中、悬停、开关）· `duration-base` 250 ms 缓出（面板、提示条） |

## <a id="ui-layout"></a>21.3 窗口与布局

- **SHOULD** `UI-03` 窗口结构：侧边栏 232 px（导航与底部状态）→ 列表 320 px（列表 + 详情类页面）→ 详情或内容（其余宽度）。窗口窄于 1200 px 时侧边栏收为 64 px 图标栏。
- **SHOULD** `UI-05` 安全提示合并为工具栏下方的一条提示条，同时出现时按优先级只显示最高的一条并标出其余数量：待决定的请求 > 安全保护已关闭 > 控制或确认通道不可用 > 待确认的预填 > 短暂通知。
- **SHOULD** `UI-06` 每类功能只有一个主入口（待批请求、环境问题、日志与诊断、连接信息各一处）；其他页面只放链接到它的提示。
- **SHOULD** `UI-07` 最小窗口 1024 × 640 时全部功能可用（允许滚动）；声明 Per-Monitor V2 DPI 感知，在 100–200% 和跨屏混合缩放下不模糊、不截断。

## <a id="ui-type"></a>21.4 字体

正文：`"Segoe UI Variable Text", "Segoe UI", "Microsoft YaHei UI"`，其他平台为系统字体；等宽：`"Cascadia Mono", Consolas`，只用于工具名、路径、标识、日志、时间和数值。不加载网络字体。

| Token | 字号/行高 | 字重 | 用途 |
|---|---|---|---|
| `large-title` | 28/34 | 700 | 工具栏页面标题，每页一个 |
| `title-1` | 22/28 | 600 | 详情区标题，一句话说清要发生什么 |
| `title-2` | 17/24 | 600 | 确认面板、空状态、分区标题 |
| `headline` | 14/20 | 600 | 列表行主文字、按钮文字 |
| `body` | 14/21 | 400 | 正文 |
| `callout` | 13/18 | 400 | 副文字、分组标题、表头 |
| `footnote` | 12/17 | 400 | 注释、快捷键提示；最小的可读文字 |
| `mono` / `mono-small` | 13/18 · 12/17 | 400 | 技术标识 |

## <a id="ui-color-values"></a>21.5 颜色 Token

| Token | 浅色 | 深色 | 高对比 | 用途 |
|---|---|---|---|---|
| `bg-window` | #FFFFFF | #1E1E1E | Window | 主体底色 |
| `bg-sidebar` | #EBEBED | #2A2A2C | Window | 导航 |
| `fill-control` | #E5E5EA | #3A3A3C | ButtonFace | 非默认按钮底色 |
| `label` | #1D1D1F | #F5F5F7 | WindowText | 正文 |
| `label-secondary` | #636366 | #AEAEB2 | WindowText | 说明、表头（≥4.5:1） |
| `label-tertiary` | #8E8E93 | #8E8E93 | GrayText | 只用于禁用态和图标 |
| `accent` | #0071E3 | #0071E3 | Highlight | 默认按钮底、选中、开关、进度 |
| `label-on-accent` | #FFFFFF | #FFFFFF | HighlightText | accent 底上的文字（4.7:1） |
| `accent-text` | #0066CC | #409CFF | HotTrack | 链接、文字按钮 |
| `border-control` | #86868B | #8E8E93 | WindowText | 输入框、复选框边框（≥3:1） |
| `focus-ring` | #0071E3 | #409CFF | WindowText | 焦点环 2 px，外扩 2 px |
| `destructive` / `-text` | #D70015 | #D70015 / #FF6961 | WindowText + 图标 | 破坏性；带 `-text` 的才能放文字 |
| `warning-text` / `success-text` | #B25000 / #1A7431 | #FFB340 / #30D158 | WindowText + 图标 | 状态文字；无后缀的只用于图标和圆点 |

- **SHOULD** `UI-12` 主题“自动 / 浅色 / 深色”即时切换；Windows 高对比开启时自动使用高对比字典，每个值映射到 SystemColors，所有卡片、按钮、输入框加 1 px WindowText 描边，阴影为无，状态只靠图标形状和文字。

## <a id="ui-desktop-nav"></a>设置、导航与键盘

- **SHOULD** `UI-23` 一级页面不超过 8 个，<kbd>Ctrl</kbd>+<kbd>1</kbd>…<kbd>Ctrl</kbd>+<kbd>8</kbd> 与侧边栏视觉顺序一致；设置固定在侧边栏底部，<kbd>Ctrl</kbd>+<kbd>,</kbd> 打开；<kbd>F6</kbd> 在区域间切换；快捷键在代码、提示和文档中一致。
- **MUST** `UI-25` 对话框按钮和主要表单字段有访问键（`_Save`、`保存(_S)`）；审批的批准与拒绝按钮不设访问键。
  - 理由 · 单个按键不能批准写入。

## <a id="ui-desktop-test"></a>界面测试

- **SHOULD** `UI-36` [M+] 渲染测试覆盖 1024 × 640 与 1366 × 860、中英文、浅色/深色/高对比；自动化树测试检查名称和焦点顺序。

---

[桌面与本机软件](README.md) · [通用规范](../general/README.md)
