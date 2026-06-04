# Capabilities

本文件说明本项目哪些能力已经实现，哪些只是规范、模板或未来接入点，避免使用者对自动化能力产生过度预期。

## 已实现能力

| 能力 | 状态 | 说明 |
|---|---|---|
| Repo-scoped Codex Skills | 已实现 | `.agents/skills/china-*` 可被 Codex 读取和调用 |
| 主控路由 Skill | 已实现 | `china-internet-compliance` 可进行事实抽取、场景分类和跨专项路由 |
| 11 个专项 Skill | 已实现 | 覆盖产品、数据、AI、内容、广告、交易、游戏、支付、IP/开源、供应商、监管响应 |
| 15 个 command 工作流 | 已实现 | 每个 command 有独立场景、输入、流程、输出和质量门槛 |
| 输出模板 | 已实现 | `templates/` 提供常见评审记录、PIA、上线 gate、供应商审查等结构 |
| 参考规则库 | 已实现 | `references/` 提供 taxonomy、risk matrix、source guardrails、source index 等 |
| 验证脚本 | 已实现 | `validate_skill.py` 检查目录、命令、样例、测试集和专项 Skill 结构 |
| 示例提示词和参考输出 | 已实现 | `examples/` 和 `examples/expected-outputs/` 可用于快速试用 |
| Golden Examples | 已实现 | 30 个样例已按真实法务/合规审查意见格式重写，包含事实矩阵、证据缺口、整改责任方和 gate |
| 开源项目文档 | 已实现 | README、Quickstart、FAQ、Security、Contributing、Legal Disclaimer 等已提供 |

## 部分实现能力

| 能力 | 状态 | 说明 |
|---|---|---|
| Evaluation scoring | 部分实现 | `evaluate_outputs.py` 可做覆盖检查，但还不是完整自动化测试平台 |
| Source maintenance | 部分实现 | `SOURCE_INDEX.yaml` 已扩展，但仍需定期核验和补充行业/地方/平台规则 |
| Company profile | 部分实现 | 提供模板和 cold-start command，但需要企业自行填入真实审批口径 |
| GitHub Actions | 模板已提供 | workflow 模板在 `docs/github-actions/`，需复制到 `.github/workflows/` 并使用带 `workflow` scope 的 token 推送 |

## 规范/接口，不是已运行能力

| 能力 | 状态 | 说明 |
|---|---|---|
| Connectors | 规范 | `connectors/` 只是数据契约，不会自动连接法规库、PRD、合同库、SDK 清单或数据地图 |
| Agents / Watchers | 设计规范 | `agents/` 只是 watcher/reviewer 的输出规范，不会自动后台运行或定时监控 |
| 自动法规更新 | 未实现 | 项目不会自动抓取法规变化；需人工或企业系统按 `SOURCE_MAINTENANCE.md` 更新 |
| 企业审批流集成 | 未实现 | 不会自动接入 Jira、飞书、钉钉、OA、法务系统或数据平台 |
| 正式法律意见 | 不提供 | 输出只能作为合规初审和工作底稿，不替代律师或企业法务意见 |

## 推荐上线边界

适合直接使用：

- PRD 初审
- 上线前风险分诊
- 合规工作底稿生成
- 法务/隐私/安全评审清单
- 历史案例复盘
- 公司合规流程搭建草案

需要人工复核后使用：

- 监管问询、公安调证、诉讼/仲裁证据响应
- 数据出境、重要数据、敏感个人信息大规模处理
- AI/AIGC 公共服务、算法备案、安全评估
- 金融、医疗、未成年人、游戏充值、直播电商等高监管事项
- 对外发布的法律结论、合同条款或正式合规意见
