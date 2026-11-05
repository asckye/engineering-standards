# <a id="pe"></a>Web 开发

> **要点** TypeScript strict、OpenAPI 为契约、OWASP 为安全基线；性能预算和可观测性按等级。

状态：2.1。

**同时采用：** [通用规范](../../general-engineering-standard/references/contents.md)。

## <a id="pe-front"></a>E.1 前端

- **SHOULD** `WEB-01` 组件小而单一：展示组件只接收数据和回调，数据获取放在页面或容器层；状态放在用到它的最近位置，服务端数据交给查询缓存库，全局存储只放真正全局的状态。
- **SHOULD** `WEB-02` TypeScript `strict`；外部数据（API 响应、URL 参数、本地存储）进入时按 schema 校验（L2 附录）。
- **MUST** `WEB-03` 语义化元素优先于 ARIA；全部键盘可用；焦点可见；对比度按 `UI-10`；表单控件有名称，错误与字段关联。面向公众或法规要求无障碍的产品满足 WCAG 2.2 AA；其他产品以它为默认目标，偏离写理由。
  - 理由 · 这些做不到，键盘和读屏用户就用不了；面向公众的产品在不少地区有法律要求。
- **SHOULD** `WEB-04` [M+] 性能预算按第 75 百分位：LCP ≤ 2.5 s、INP ≤ 200 ms、CLS ≤ 0.1；每个路由的首屏 JS 体积有上限，由 CI 检查。
- **SHOULD** `WEB-05` 响应式：从 320 px 宽度起没有横向滚动；颜色、字号、间距用 CSS 变量形式的设计 token；支持浅色与深色。
- **SHOULD** `WEB-06` 写明浏览器支持政策（例如主流常青浏览器的最近两个版本），按政策测试。
- **SHOULD** `WEB-07` 每个路由有错误边界，显示可恢复的错误界面并上报诊断编号；文字走 i18n 资源（[第 10 节](../../general-engineering-standard/references/10-i18n.md)）。
- **MUST NOT** `WEB-08` 在前端代码、构建产物或环境变量中放密钥：发到浏览器的一切都是公开的。
  - 理由 · 发到浏览器的密钥对所有人可见。

## <a id="pe-api"></a>E.2 后端与 API

- **SHOULD** `WEB-09` REST 按 Microsoft REST API Guidelines；选用 GraphQL 或 gRPC 时写 ADR。OpenAPI 是契约：入库、由代码生成或校验，差异按契约变化评审。
- **SHOULD** `WEB-10` API 有版本（`api-version` 参数或路径主版本）；列表分页（游标或 `nextLink`）且有上限；创建或扣费类 `POST` 接受 `Idempotency-Key`。
- **SHOULD** `WEB-11` 错误用 RFC 9457 problem details（`type`、`title`、`status`、`detail`、`instance`，加稳定的错误码和请求号）；不返回堆栈。
- **SHOULD** `WEB-12` 限流返回 429 和 `Retry-After`；对外调用都有超时和有上限的重试（只对幂等请求）。
- **MUST** `WEB-13` 认证用 OAuth 2.0 / OpenID Connect（浏览器用授权码 + PKCE）；访问令牌短期有效；授权在服务端按资源检查。
  - 理由 · 只在客户端检查权限会被绕过。
- **MUST** `WEB-14` 会话 Cookie 设 `Secure`、`HttpOnly`、`SameSite=Lax` 或 `Strict`；基于 Cookie 的状态变更请求有 CSRF 防护；CORS 使用显式白名单，带凭据时不用 `*`。
  - 理由 · 防止会话劫持、CSRF 和跨域滥用。

## <a id="pe-sec"></a>E.3 Web 安全

- **SHOULD** `WEB-16` 按 OWASP Top 10 建威胁清单；[M+] 选定 OWASP ASVS 等级（M 用 Level 1，L 用 Level 2）并逐项核对。
- **MUST** `WEB-17` SQL 只用参数化查询或 ORM，不拼接字符串；动态排序与列名走白名单。
  - 理由 · 防止 SQL 注入。
- **MUST** `WEB-18` XSS：依赖框架的自动转义；插入 HTML 前用净化库；设置 CSP（nonce 或 hash，不用 `unsafe-inline`）。
  - 理由 · 防止 XSS。
- **MUST** `WEB-19` SSRF：服务端发起的请求只访问白名单目标，拒绝内网地址段和云元数据地址，跟随重定向时重新校验。
  - 理由 · 防止 SSRF 访问内网和云元数据。
- **MUST** `WEB-20` 文件上传：大小上限；按内容判断类型；随机文件名；存放在 Web 根目录之外；下载用 `Content-Disposition: attachment`。
  - 理由 · 防止上传的文件被执行或覆盖。
- **SHOULD** `WEB-21` 安全响应头：`Strict-Transport-Security`、`Content-Security-Policy`（含 `frame-ancestors`）、`X-Content-Type-Options: nosniff`、`Referrer-Policy`。

## <a id="pe-data"></a>E.4 数据

- **MUST** `WEB-23` 数据库结构变更用入库的版本化迁移，由工具执行；每个迁移可回退，或写明只前进的计划；[M+] 零停机变更用“先扩展、后收缩”两步。
  - 理由 · 手工改库无法复现，也退不回去，出错时数据就没了。
- **SHOULD** `WEB-24` 跨多行的不变量放在事务中；索引按查询模式建立，并用执行计划核对慢查询。
- **MUST** `WEB-25` 备份自动执行，并定期做恢复演练（[L] 至少每季度一次），记录恢复所需时间。
  - 理由 · 没有恢复演练的备份往往恢复不了。
- **MUST** `WEB-26` 个人信息有清单：最少收集、传输与存储加密、保留期与删除；遵守 GDPR 与《个人信息保护法》的基本要求（合法依据或同意、访问与删除请求、跨境传输规则、泄露通知流程）。
  - 理由 · 违法收集或泄露个人信息。

## <a id="pe-ops"></a>E.5 运维

- **SHOULD** `WEB-27` 配置按十二要素经环境注入；同一个构建产物在 dev、staging、prod 之间晋升，不为环境重新构建。
- **SHOULD** `WEB-28` [M+] 容器用最小基础镜像、非 root 用户、按摘要固定版本（构建用的镜像按 `DEP-14`）；基础设施用代码（IaC）入库并经评审。
- **SHOULD** `WEB-30` [M+] 可观测性：结构化日志、指标、链路追踪（OpenTelemetry），全部带请求号；提供存活与就绪探针。
- **SHOULD** `WEB-31` [L] 为关键用户路径定义 SLO 和错误预算；按症状告警，每个告警链接到处置手册（runbook）。
- **SHOULD** `WEB-32` [M+] 零停机部署（滚动或蓝绿），一步回滚到上一个版本；数据库迁移与回滚兼容。

## <a id="pe-checklist"></a>E.6 Web 发布清单

- [ ] OpenAPI 差异已评审；破坏性变化升版本。
- [ ] Core Web Vitals 与体积预算通过；无障碍自动检查与键盘走查通过。
- [ ] 安全头、CSP、Cookie 属性、CORS 白名单已核对；依赖扫描无高危。
- [ ] 迁移在 staging 演练；回滚步骤可用；备份最近一次恢复演练成功。
- [ ] 仪表盘与告警覆盖新功能；功能开关有到期日。

---

[通用规范](../../general-engineering-standard/references/contents.md) · [仓库首页](../../../README.md)
