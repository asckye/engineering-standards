# <a id="lts"></a>附录 L2：TypeScript/JavaScript

| 方面 | 规则 |
|---|---|
| 命名 | 变量与函数 camelCase，类型、类和组件 PascalCase，常量 UPPER_SNAKE；文件名按框架约定统一一种（组件文件 PascalCase 或全部 kebab-case）。 |
| 类型 | `strict: true`、`noUncheckedIndexedAccess`、`exactOptionalPropertyTypes`；不用 `any`，边界上用 `unknown` 加 schema 校验（例如 zod）得到类型；非空断言 `!` 只用于已证明处。 |
| 错误 | 只抛 `Error` 及其子类，不抛字符串；用 `cause` 保留原因；可预期的失败用结果类型或判别联合返回。 |
| 异步 | 不留悬空的 Promise（lint 规则 `no-floating-promises`）；用 `AbortController` 实现取消和超时；并发用有上限的批量，不无限 `Promise.all`。单线程不等于没有竞态：`await` 之后状态可能已经变了，要重新检查（CODE-17）。 |
| 打包 | 只用一种包管理器；锁文件入库；精确版本（`save-exact`）；CI 用 `npm ci` 或 `pnpm install --frozen-lockfile`；`engines` 写明 Node 版本。 |
| 检查与格式化 | ESLint + typescript-eslint（`strict-type-checked`）；Prettier 统一格式；公开 API 用 TSDoc，并用 jsdoc 规则检查。 |
| 测试 | Vitest 或 Jest；组件用 Testing Library 按行为测试；端到端用 Playwright；网络用 MSW 一类的模拟，不访问真实服务；假定时器控制时间。 |

---

[目录](../README.md)
