# <a id="enforce"></a>24 让规则可执行

> **要点** 能自动检查的就不写成说明文字；“仅评审”的规则是自动化候选。

- **SHOULD** `ENF-01` 每条 MUST 规则在下表中有执行方式；“仅评审”的规则是自动化候选，按出错频率排期自动化。
- **MUST** `ENF-02` 新检查引入时为存量建基线（棘轮），只拦新增，基线只减不增。
  - 理由 · 没有基线，新检查要么阻塞所有人，要么被关掉。
- **SHOULD** `ENF-03` [M+] 仓库有 PR 模板（勾选本节的评审项）和 CODEOWNERS（安全关键目录需要维护者评审）。

| 机制 | 覆盖的 MUST | 何时拦截 |
|---|---|---|
| 编译器、分析器、`.editorconfig` | CODE-04–07、CODE-10、Q-15、ERR-04、SEC-12；语言附录 | 构建 |
| 架构测试（工程或包依赖） | ARC-01、ARC-03、DEP-07、ENG-01、ENG-13 | 合并门 |
| 仓库检查（build-tools） | GIT-07、DEP-02、DEP-03、DEP-06、PKG-07、ENF-02、G-06（套件下限） | 合并门 |
| 密钥扫描 | SEC-22、DAT-07、AI-15 | 提交前与推送 |
| 契约快照 | P-25、MIG-01、MIG-02、PRO-05、TL-12、TL-14、WS-17、WS-02 | 合并门 |
| 失败路径与故障注入测试 | P-05、P-21、ERR-01、ERR-06–08、ERR-10、ERR-14、ERR-18、ERR-21、SEC-03–05、SEC-07、SEC-10、SEC-14、SEC-16、SEC-17、SEC-20、SEC-23、DAT-02、DAT-03、MIG-04、WS-04、WS-07、WS-13、ENG-11、WEB-14、WEB-17–20 | 合并门 |
| 测试基础设施（禁网、注入时钟、快照不自动接受） | TST-05、TST-06、TST-08 | 合并门 |
| 界面测试 | UI-10、UI-13、UI-16、UI-17、UI-19、UI-24、UI-25、UI-32 | 合并门 |
| 提交信息检查 | GIT-04 | 提交钩子、CI |
| 发布门 | P-03（生成“未验证”清单）、BLD-07、DEP-10、MIG-05、DOC-06、EOL-01 | 发布 |
| 硬件在环与实机清单 | IND-01–03、IND-05、IND-09、IND-14、IND-15、IND-17、IND-42、ENG-03、ENG-04、ENG-14、WEB-25 | 发布前 |
| 验收记录与上线清单（26.3） | ACC-01、ACC-02、ACC-04、ACC-06–08、OPS-01–03、OPS-05、OPS-12、OPS-17、IND-44–46 | 上线前 |
| 定期演练记录 | OPS-13、OPS-14 | 按周期 |
| 事故和变更记录 | OPS-07、OPS-09、OPS-18、OPS-21、OPS-23–25 | 事故后复盘、变更时 |
| 退役清单（26.4） | EOL-05、EOL-07–09 | 退役时 |
| 仅评审（自动化候选） | G-04、FAST-04、BLD-01、DAT-06、PKG-04、P-01、P-04、P-06、P-09、P-12–P-14、P-22、Q-03、Q-17、CMT-04、BUG-02、BUG-04、BUG-05、REV-01、REV-05、REV-07、TST-01、GIT-03、AI-10–13、AI-17、CFG-03、CFG-06、WIN-13–15、I18N-03、DIAG-01、DIAG-04、ARC-04、ARC-07、ARC-12、ARC-17、SEC-19、IND-26–28、IND-32、IND-36、ENG-16、DSK-02、DSK-09、WEB-08、WEB-13、WEB-26、MOB-07、MOB-08、MOB-10、MOB-15、EOL-04 | 评审；按出错频率排期自动化 |

[MCP 规范](../mcp/05-verification.md)其余 MUST 的验证方式见它的验证层。[视觉](../vision/README.md)和[大屏](../dashboard/README.md)的 MUST：运行行为按各自的发布清单核对，设计和流程类的在评审中核对。

---

[← 上一节：23 完成定义](23-definition-of-done.md) · [目录](README.md) · [下一节：25 在新项目中采用 →](25-adoption.md)
