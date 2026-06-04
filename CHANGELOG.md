# CHANGELOG

## Unreleased

- Added `QUICKSTART.md` for installation, first-run usage and troubleshooting.
- Added `examples/` with five copy-ready compliance review prompts.
- Added `CONTRIBUTING.md`, `SECURITY.md` and `LEGAL_DISCLAIMER.md`.
- Added a GitHub Actions validation template for the Skill package.
- Added issue templates, a pull request template and a global install helper script.

## v4.0 — 架构升级版

本版本从“增强规则型 Skill”升级为“合规工作流系统雏形”。核心变化：

1. **多 Skill 架构**：新增 11 个专项子 Skill，覆盖产品、数据、AI、内容、广告、交易、游戏、支付、IP/开源、供应商和监管响应。
2. **命令入口**：新增 `commands/`，提供 launch review、quick triage、data PIA、AI review、OSS review、vendor review、regulatory response、cold-start interview 等稳定任务入口。
3. **公司化 Profile**：新增 `profiles/`，支持通过 cold-start interview 生成公司风险偏好、审批矩阵、数据分类、升级规则和输出口径。
4. **引用校验体系**：新增 `CITATION_GUARDRAILS.md`、`SOURCE_VERIFICATION_RULES.md`、`DUTY_TO_EVIDENCE_MATRIX.md`，要求重大结论绑定依据、证据和核验状态。
5. **连接器规范**：新增 `connectors/`，定义法规库、内部制度、PRD、SCA/SBOM、SDK清单、数据地图、模型登记台账、合同库等接入规范。
6. **Agent 设计**：新增 `agents/`，设计监管变化监控、开源依赖监控、SDK权限监控、AI备案缺口监控、供应商合同到期监控等 watcher/reviewer。
7. **评测体系**：新增 `evals/` 和 `scripts/evaluate_outputs.py`，用于对输出进行事实抽取、场景分类、法律依据、风险分级、整改动作、引用质量等维度评分。
8. **优秀样例扩展**：golden examples 从 23 个扩展到 30 个。
9. **校验脚本升级**：`validate_skill.py` 强制检查 v4.0 架构文件、专项 Skill、commands、profiles、connectors、agents、evals 和 golden examples。

## v3.0 — 全场景强化版

补充法条/义务级规则库、垂直行业专项手册、输入事实 Schema、开源决策树、法规更新机制和优秀输出样例。

## v2.0 — 全场景可用版

删除单一公司/电商 SaaS 定向假设，改为中国互联网公司全场景通用合规 Skill。

## v1.0 — 基础版

建立 repo-scoped Skill 结构、基础合规评审模板、风险分级和通用输出格式。

## v4.1 / v4.2 / v4.3 staged upgrade

### v4.1 Specialist Deepening
- Rewrote 11 specialist `SKILL.md` files with required inputs, decision trees, P0/P1 triggers, evidence requirements, cross-skill routing, and quality gates.
- Added specialist `PLAYBOOK.md` files and `SPECIALIST_SKILL_DEEPENING_INDEX.md`.

### v4.2 Executable Commands
- Rebuilt all 15 `/china-compliance:*` command files as command contracts with required inputs, missing-material handling, routing paths, output schemas, and quality thresholds.
- Added `COMMAND_EXECUTION_STANDARD.md`, `COMMAND_INPUT_CONTRACTS.json`, and `COMMAND_ROUTING_MATRIX.md`.

### v4.3 Evaluation Enhancement
- Added `expected_issues.json` and `EXPECTED_CASE_MATRIX.md` for 120 test cases.
- Added legal correctness and risk identification rubrics.
- Upgraded `evaluate_outputs.py` to check expected issue coverage and risk-level coverage.
- Added `SOURCE_INDEX.yaml` for official-source traceability and citation guardrails.
