# <a id="quality"></a>4 代码质量

> **要点** 小函数、单一职责、一个功能一个实现。数值是评审触发线，不是硬门禁；注释解释原因。

## <a id="quality-size"></a>4.1 规模与复杂度

数值是评审触发线：超过时拆分，或在 PR 中写一行理由（例如“厂商要求的固定调用序列”）。

| 度量 | 建议上限 | 超过时 |
|---|---|---|
| 方法或函数 | 约 40–60 行 | 提取命名清楚的函数 |
| 文件 | 约 400–600 行，一个类型 | 按职责拆类型，不靠 partial 变小 |
| 圈复杂度 | 约 10–15 | 表驱动、提前返回 |
| 嵌套深度 | 3 | 提前返回、提取函数 |
| 参数 | 约 5 个 | 参数对象 |

- **SHOULD** `Q-01` 新代码和改动的代码遵守上表；分析器的复杂度规则作提示，不机械拆分。

## <a id="quality-dup"></a>4.2 重复、死代码、杂物类型

- **MUST** `Q-03` 同一判断、转换或业务规则（约 5 行以上）出现第二次时合并为一个共享组件。目标版本间的 API 差异不算重复。
  - 理由 · 重复逻辑改一处漏一处。
- **SHOULD NOT** `Q-04` 死代码、注释掉的代码。
- **SHOULD NOT** `Q-05` 上帝类和杂物类型（`Helpers`、`Utils`、`Manager`、`Common`）；静态类只放无状态算法，名称说明用途。

## <a id="quality-design"></a>4.3 设计

- **SHOULD** `Q-08` 逻辑写成不可变数据加纯函数；副作用集中在应用层和适配层。
- **SHOULD** `Q-09` 依赖经构造函数注入；不用服务定位器和静态单例。
- **SHOULD** `Q-10` 名称说明“是什么”，不说明“怎么做”（`PendingApprovals`，不是 `DictionaryWrapperList`）；布尔用肯定式。

## <a id="quality-comments"></a>4.4 注释规范

- **SHOULD** `CMT-01` 代码中的注释用英文；给用户看的文字走资源文件，不写在注释或字面量里。只有项目在自己的代理说明中明确决定时，才允许中文注释。
- **SHOULD** `CMT-02` 注释写代码说不出来的“为什么”：不显而易见的决定；厂商 API 的怪癖和版本差异（附文档或记录出处）；不变量；单位和范围；线程或单元要求；某个检查为什么存在（安全原因）；绕过办法（附 Issue 或 ADR 链接）。
- **SHOULD NOT** `CMT-03` 复述代码；保留注释掉的代码；在注释中记修改历史（那属于 Git）；装饰性横幅；作者或日期文件头（只在许可证要求时加许可证头）。
- **MUST** `CMT-04` 与代码不符的注释是缺陷，在同一个改动中修正或删除。
  - 理由 · 过期注释误导后来的修改者。
- **SHOULD** `CMT-05` [M+] 公开类型和成员有文档注释（C# XML 文档注释、TS 的 TSDoc、Python docstring）：摘要、参数、返回值、异常、线程安全性。由代码生成的对外描述（OpenAPI、工具描述、schema）取自同一来源。
- **SHOULD** `CMT-06` `TODO`/`FIXME` 必须带负责人或 Issue 编号和原因，如 `// TODO(#123): remove after v2 migration`；发布涉及的代码路径中不留未关闭的 TODO，由检查列出。
- **SHOULD** `CMT-07` 密度与周围代码一致；优先用清楚的名称和小函数代替注释。测试的行为写在测试名里，只为不显而易见的夹具原因加注释。

**推荐：说明原因与出处**

```csharp
// The vendor API returns success but drops the value when the
// object is locked by another user (vendor doc 4.2, issue #212),
// so verify by reading it back before committing.
var actual = adapter.ReadValue(path);
```

**避免：复述、历史、无主 TODO**

```python
# read the value
value = adapter.read_value(path)  # changed by <author> 2026-03-01
# TODO fix later
```

> **执行** C# 开启 `GenerateDocumentationFile` 并把 CS1591 设为公开表面上的错误；TS 用 ESLint 的 jsdoc 规则，Python 用 Ruff 的 D 规则；仓库检查列出不带编号的 TODO；过期注释靠评审。

## <a id="quality-analysis"></a>4.5 静态分析

- **MUST** `Q-15` 启用语言的标准分析器和格式化工具，配置入库；新代码零新增警告：新项目警告即错误，老项目的存量记在只减不增的基线中。
  - 理由 · 警告一旦堆积就没人再看，新问题被淹没。

## <a id="quality-tests"></a>4.6 测试质量

- **SHOULD** `Q-13` 测试名说明行为（`WriteSetpoint_OutOfRange_IsRejectedBeforeSend`）；一个测试一个失败理由；测试中不写分支和循环。

## <a id="quality-refactor"></a>4.7 重构

- **SHOULD** `Q-16` 童子军规则只在本次改动触及的范围内执行。
- **MUST** `Q-17` 重构单独成批、单独提交，不与行为变化混合；行为不变由对等测试证明。
  - 理由 · 混在一起的重构与行为变化无法评审，也难以回退。
- **SHOULD NOT** `Q-18` 一次性重写；新旧路径并存，对等测试通过后再删旧路径。

## <a id="quality-smells"></a>4.8 拒绝的坏味道

| 坏味道 | 表现 | 改法 |
|---|---|---|
| 层层重复校验 | 入口、服务、适配器各查一遍，错误码还不一样 | 边界一次（1.3） |
| 捕获再包装链 | 每层 `catch (Exception e) { throw new X(e.Message); }` | 中间层不捕获，边界映射一次 |
| 标志参数穿层 | `skipCheck` 从入口穿过五层只为一个分支 | 在边界选策略，或拆成两个用例 |
| 热路径上重复初始化 | 每个请求都重新读配置、建连接、构建查找表 | 启动时一次，变化时增量更新 |
| 测试里的真实等待 | 测试等真实的宽限期或心跳 | 注入时钟（TST-05） |
| 按名称推断能力 | “名字以 Get 开头就是只读” | 显式登记（P-01） |

---

[← 上一节：3 代码规范](03-code.md) · [目录](contents.md) · [下一节：5 错误处理与健壮性 →](05-errors.md)
