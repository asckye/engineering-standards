# <a id="templates"></a>附录 T：模板

复制后删去尖括号中的提示。各模板只给必需的段落。

## <a id="tpl-readme"></a>T.1 README

```markdown
# <Product>
<一句话：做什么，给谁用>

## 支持矩阵
| 目标版本 | 状态 |  已验证 / 已构建未验证 / 不支持
## 支持政策
<哪些版本还在支持，修什么，支持到什么时候（EOL-01）>
## 安装
<按用户安装的步骤；校验 SHA-256>
## 快速开始
<最短可用路径，命令可复制>
## 文档
<用户文档、故障排查、CHANGELOG 的链接>
## 工程规范
遵守《工程开发规范》<版本>；等级 <S|M|L>；项目类型 <根目录中适用的文件夹>；语言附录 <L1–L3>
## 许可
<许可证；THIRD-PARTY-NOTICES；商标与无隶属声明>
```

## <a id="tpl-adr"></a>T.2 ADR

```markdown
# NNNN <用陈述句写出决定>
- 状态：提议 | 已采纳 | 已拒绝 | 已被 NNNN 取代 | 已废弃
- 日期：YYYY-MM-DD · 决策者：<维护者> · 置信度：高 | 中 | 低
- 相关：<设计说明、Issue、被取代的 ADR>

## 背景与问题
## 考虑的选项
1. <选项>：<一行优缺点>
## 决定
采用选项 N，因为 <理由>。
## 后果
- 正面：
- 负面与取舍：
- 后续工作与验证方式：
```

## <a id="tpl-rfc"></a>T.3 设计说明

```markdown
# <标题>   状态：草稿 | 已批准 · 日期 · 关联需求
## 问题        要解决什么，为什么现在做
## 选项        2–3 个，各一行优缺点
## 决定        选哪个，为什么
## 影响        接口与契约 / 数据与格式 / 安全与设备安全（信任边界，STRIDE 每行一条）/ 个人数据（DAT-08）/ 兼容与迁移
## 测试计划    验收标准对应的测试；需要的实机验证
## 待决定      需要维护者回答的问题与推荐选项
```

## <a id="tpl-task"></a>T.4 任务说明（给实现代理）

```text
# 任务 <ID>：<标题>
目标          要达到的行为（一两句）
根因与证据    诊断结论、日志或复现步骤
涉及位置      文件与函数；允许修改的路径
设计          预期做法
扩展点        必须使用的登记表、共享组件或适配器
验收标准      Given/When/Then
测试          修改前失败、修改后通过的测试（名称与断言要点）
预先批准      需要改变的断言或基线（已获维护者批准）
约束          测试不等真实时间 >1 s；零新增警告；热路径附前后计时；不改范围外文件
验证命令      <命令>
时间预算      约 3 小时；到时收尾并列出剩余工作
待决定        需要维护者回答的问题
报告          改动文件；命令与通过/失败/阻塞数；与说明不一致处；未决事项
```

## <a id="tpl-pr"></a>T.5 PR 说明

```markdown
## 为什么
<问题与需求链接>
## 改了什么
<要点；契约或数据格式变化逐项列出>
## 怎么验证的
<命令与结果；实机核对（如有）>
## 风险与回退
## 检查
- [ ] 只在边界校验；无重复逻辑、单实现接口、无人要的配置
- [ ] 修改前失败、修改后通过的测试
- [ ] 零新增警告；生成文件由生成器产出
- [ ] CHANGELOG / 文档已更新；无密钥与客户数据
```

## <a id="tpl-bug"></a>T.6 缺陷报告

```text
标题        <现象，一句话>
版本        产品 <X.Y.Z> · 目标 <完整版本号> · 操作系统
步骤        1. … 2. … 3. …
期望 / 实际
诊断编号    <从界面“复制诊断信息”获得>；诊断包：<已附 / 未附>
影响        是否写入了目标或数据？是否可绕过？
清单编号    <预发布“未验证”清单中的编号（如有）>
```

## <a id="tpl-release"></a>T.7 发布说明

```markdown
# vX.Y.Z[-beta.N]
## Summary
## Changes
## Upgrade
<migration steps; how to go back to the previous version and what happens to data; breaking changes with the generated mapping table>
## Supported versions
<verified / built but not verified / unsupported>
## Support status
<support status of this release; link to the support policy in the README; any end-of-support notice>
## Known limits
## Not verified on a real target
1. <item generated from the ledger>
2. …
## Checksums
<file>  SHA-256 <hex>
```

## <a id="tpl-agents"></a>T.8 项目的 CLAUDE.md / AGENTS.md

```markdown
# 给 AI 编码代理
- 本项目遵守《工程开发规范》<版本>：等级 M；项目类型 mcp、desktop；语言附录 L1。规则冲突时以规范和本文件为准。
- 先读 docs/plan/progress.md；决定见 docs/adr/；术语见 docs/standards/glossary.md。
- 构建与合并门：<唯一入口命令>；修改示例或目录后先运行生成器。
- 项目特有：<只在 scratch 项目上写入目标；目标版本键表的位置；禁用 API 列表>。
- 不改系统设置；下载先问；只结束自己启动的进程。
- 允许用的 AI 服务：<服务和账号类型；是否用于训练、保留多久>（AI-19）。真实凭据、他人的个人数据和客户数据不发给外部模型服务（AI-18）。
- 显式 git add 路径；英文提交；不加 AI 署名；不做破坏性 Git 操作。
- 不删除、跳过或放宽检查；有疑问附证据报告。
```

---

[目录](../README.md)
