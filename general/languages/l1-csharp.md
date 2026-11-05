# <a id="lcs"></a>附录 L1：C#/.NET

| 方面 | 规则 |
|---|---|
| 命名 | 按 Framework Design Guidelines：类型与成员 PascalCase，参数与局部变量 camelCase，接口 `I` 前缀，私有字段 `_camelCase`，可变静态 `s_camelCase`；两字母缩写全大写（`IO`），三字母以上按单词（`Xml`）；异步方法 `Async` 后缀；file-scoped 命名空间；类型默认 `internal sealed`。 |
| 类型 | `<Nullable>enable</Nullable>`；`!` 只用于已证明非空处；闭集用枚举，开放集用字符串或值对象；值对象不可变（只读属性 + 构造时校验）；公开 API 返回 `IReadOnlyList<T>` 等只读集合，不返回 `null` 集合。 |
| 错误 | 参数错误抛 `ArgumentException` 族并设 `ParamName`；状态错误 `InvalidOperationException`；不抛 `Exception`/`ApplicationException`；重新抛出用 `throw;`；`finally`、`Dispose`、`Equals`、`ToString` 中不抛异常；需要区分时才定义自定义异常（`sealed`，以 `Exception` 结尾）。 |
| 异步与线程 | 不用 `async void`（事件处理器除外）；不在界面线程或同步上下文中 `.Result`/`.Wait()`；库代码 `ConfigureAwait(false)`；`CancellationToken cancellationToken` 放最后并传下去；锁用 `private readonly object` 或 `Lock`，跨 `await` 用 `SemaphoreSlim`；时间用 `TimeProvider`。`ConcurrentDictionary` 的单次读写线程安全，但 `GetOrAdd`、`AddOrUpdate` 的工厂委托在锁外运行，可能运行多次，不能有副作用；复合操作仍要加锁（CODE-15–17）。`SemaphoreSlim` 不可重入，不记所有者，用 `try/finally` 释放。 |
| 资源与字符串 | `using` 声明；`Dispose` 幂等；`StringComparison` 与 `CultureInfo.InvariantCulture` 显式指定；字符串键字典指定比较器；System.Text.Json，选项缓存复用；XML 用 `DtdProcessing.Prohibit`、`XmlResolver = null`。 |
| 打包 | SDK 风格工程；`global.json` 固定 SDK；`Directory.Packages.props` 中央版本；`packages.lock.json` 入库，CI 用 `RestoreLockedMode`；面向 net48 的工程不用需要运行时支持的语言特性。 |
| 检查与格式化 | `AnalysisLevel=latest-recommended`、`EnforceCodeStyleInBuild=true`、新工程 `TreatWarningsAsErrors=true`；`.editorconfig` 定义命名与格式（IDE1006、IDE0055）；`GenerateDocumentationFile` + CS1591；`BannedApiAnalyzers`；`dotnet format --verify-no-changes`。 |
| 安全 | 子进程用 `ProcessStartInfo.ArgumentList`（.NET Framework 没有这个属性，用集中的函数按 Windows 命令行规则转义后写入 `Arguments`），`UseShellExecute=false`（.NET Framework 默认是 true）（SEC-12）；本机凭据用 DPAPI CurrentUser 或 Windows 凭据管理器（SEC-19）；安全分析规则 CA2100、CA2300–CA2330、CA3001–CA3012、CA3075、CA3077、CA5350–CA5403 等设为警告（SEC-29）；依赖扫描用 `dotnet list package --vulnerable --include-transitive`，.NET 10 起也可以写 `dotnet package list`（SEC-30）。 |
| 测试 | xUnit；快照用 Verify 一类工具（注意新版本的许可条款）；替身优先手写 fake；`FakeTimeProvider` 控制时间；测试名 `Method_Condition_Expected`。 |

---

[目录](../README.md)
