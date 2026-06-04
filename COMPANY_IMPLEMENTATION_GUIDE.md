# Company Implementation Guide

本指南说明如何把通用的 China Internet Compliance Codex 变成企业内部可用的合规审查助手。

## 目标状态

落地后的企业版本应具备：

- 公司业务画像和高频合规场景
- 风险等级和上线 gate 口径
- 法务、隐私、安全、产品、研发、运营责任矩阵
- 数据分类和敏感材料处理规则
- 公司内部制度、历史审查口径和法规来源维护机制
- PRD、SDK 清单、SBOM、合同库、模型台账、数据地图等资料入口

## Step 1：确定使用边界

先明确本工具在公司内部的定位：

| 事项 | 建议定位 |
|---|---|
| PRD 初审 | 可作为一线合规助手 |
| 上线 gate | 可生成建议，最终由审批人确认 |
| 法规依据 | 可提示来源和核验状态，重大结论需人工核验 |
| 合同/监管/诉讼 | 只做底稿和材料清单，不替代律师 |
| 自动化监控 | 需要额外接入系统，本项目仅提供规范 |

## Step 2：运行冷启动访谈

使用：

```text
/china-compliance:cold_start_interview
```

访谈输出应沉淀为：

```text
.agents/skills/china-internet-compliance/profiles/COMPLIANCE_PROFILE.md
.agents/skills/china-internet-compliance/profiles/APPROVAL_WORKFLOW.md
.agents/skills/china-internet-compliance/profiles/DATA_CLASSIFICATION.md
.agents/skills/china-internet-compliance/profiles/ESCALATION_MATRIX.md
.agents/skills/china-internet-compliance/profiles/RISK_CALIBRATION.md
```

不要直接修改 `.template.md`；建议复制模板并生成公司实际文件。

## Step 3：建立风险分级

建议从以下默认口径开始：

| 等级 | 含义 | 上线策略 |
|---|---|---|
| P0 | 违法违规、监管阻断、重大数据/安全/资质缺口 | 阻断上线 |
| P1 | 上线前必须整改或审批的高风险 | 整改后上线 |
| P2 | 可灰度上线但需监控和补证据 | 灰度上线 |
| P3 | 低风险记录项 | 可上线并记录 |

企业应补充：

- 谁可以确认 P0/P1 关闭
- 哪些事项必须管理层审批
- 哪些事项必须外部律师复核
- 哪些事项允许灰度后补材料

## Step 4：接入资料源

本项目不会自动连接企业系统。你可以按 `connectors/` 的数据契约接入：

| 资料源 | 作用 | 优先级 |
|---|---|---|
| PRD/需求系统 | 事实抽取、用户路径、上线计划 | P0 |
| SDK 清单/App 权限 | App 隐私和终端权限审查 | P0 |
| 数据地图 | PIA、数据出境、第三方共享 | P0 |
| 合同库/DPA | 供应商和数据处理责任 | P1 |
| SBOM/SCA | 开源许可证和安全漏洞 | P1 |
| 模型台账 | AI、算法、AIGC、供应商 | P1 |
| 法规库/内部制度 | 依据核验和公司口径 | P1 |

## Step 5：校准历史案例

建议选取 10-20 个脱敏历史项目：

- 已上线且无重大问题的低风险项目
- 曾被法务阻断或整改的 P1/P0 项目
- 数据/AI/广告/交易/SDK/供应商/监管响应各类典型项目

用本项目重新跑审查，比较：

- 风险等级是否一致
- 事实缺口是否准确
- 整改建议是否可执行
- 上线 gate 是否符合公司实际审批口径

将差异沉淀到 `profiles/RISK_CALIBRATION.md`。

## Step 6：建立来源维护机制

按 `SOURCE_MAINTENANCE.md` 执行：

- 高变化领域至少每季度复核
- 重大法规发布时即时更新
- 每次更新记录来源、核验日期、影响场景和修改文件
- 不使用未核验二手材料作为最终依据

## Step 7：上线内部使用流程

推荐流程：

1. 产品提交 PRD 或需求摘要。
2. Codex 使用 quick triage 判断审查路径。
3. 高风险场景进入专项 command。
4. 输出风险台账和整改项。
5. 责任方补材料或整改。
6. 法务/隐私/安全复核 P0/P1 关闭。
7. 形成可留痕的上线 gate。

## Step 8：持续治理

建议每月检查：

- 是否有新法规或监管口径
- 是否有误判或漏判案例
- 是否有新的业务场景
- command 和 golden examples 是否需要补强
- connectors 是否需要接入更多系统

## 最小落地清单

企业内部首次上线前至少完成：

- `COMPLIANCE_PROFILE.md`
- 风险分级和审批矩阵
- 数据分类规则
- 10 个历史案例校准
- 高变化来源复核
- 明确“Codex 输出不替代最终法律意见”
