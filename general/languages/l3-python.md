# <a id="lpy"></a>附录 L3：Python

| 方面 | 规则 |
|---|---|
| 命名 | PEP 8：函数与变量 snake_case，类 PascalCase，常量 UPPER_SNAKE，模块小写。 |
| 类型 | 全部函数标注类型，mypy `--strict` 或 pyright strict；不可变数据用 `@dataclass(frozen=True)`；边界数据用 schema 模型（如 pydantic）校验。 |
| 错误 | 抛具体异常；`raise NewError(...) from err` 保留原因；不写裸 `except:`，不用 `except Exception: pass`。 |
| 异步与进程 | asyncio 中不调用阻塞函数（放到执行器）；超时用 `asyncio.timeout`；子进程用参数列表、设置超时，不用 `shell=True`；路径用 `pathlib`；文件读写写明 `encoding="utf-8"`；不对外部数据用 `eval`、`pickle`。GIL 不保护复合操作，自由线程构建（3.13 起）可以没有 GIL；多线程共享状态用 `threading` 的锁或 `queue`（CODE-15）。`asyncio.Lock` 不是线程安全的；`await` 之后状态可能已经变了，要重新检查（CODE-17）。 |
| 打包 | `pyproject.toml`；锁文件（uv.lock 或 pip-tools 生成的 requirements）入库并精确固定；固定 Python 版本；在虚拟环境中运行。 |
| 检查与格式化 | Ruff 做 lint 与格式化（规则集至少 E、F、I、B、UP、S、D）；mypy 或 pyright 进入合并门。 |
| 安全 | 子进程用参数列表，不用 `shell=True`（SEC-12）；安全规则用 Ruff 的 S 规则集（SEC-29）；依赖扫描用 pip-audit，用 uv 时先导出 requirements（SEC-30）。 |
| 测试 | pytest；夹具用 fixture；时间经注入或冻结；禁止测试访问网络（例如 pytest-socket）。 |

---

[目录](../README.md)
