# Codex Skills for China Internet Compliance

中国互联网合规审查 Codex 技能包

面向中国互联网业务场景的 Codex repo-scoped Skill 套件，用于辅助法务、隐私合规、产品、研发、安全、运营和商业化团队进行结构化合规初审、上线 gate 判断、风险清单整理和评审底稿生成。

本项目不替代正式法律意见。涉及重大监管、诉讼、刑事、金融、医疗、未成年人、数据出境、重要数据、算法备案、生成式 AI 备案、公安调证或重大知识产权争议等事项，应由企业法务、外部律师、安全、隐私或管理层复核。

## Features

- 主控路由 Skill：`china-internet-compliance`
- 11 个专项 Skill：产品上线、数据隐私、AI/算法、内容治理、广告营销、平台交易、游戏虚拟资产、支付/金融相邻、知识产权/开源、供应商合同、监管响应
- 固定 command 工作流：quick triage、launch review、data PIA、AI review、OSS review、vendor review、regulatory response 等
- 公司化 Profile 模板：风险偏好、审批矩阵、数据分类、升级规则和输出口径
- 规则与证据体系：引用校验、依据状态、证据矩阵、风险分级和整改责任方
- 连接器规范：法规库、内部制度、PRD、SCA/SBOM、SDK 清单、数据地图、模型登记台账、合同库
- 评测体系：测试用例、rubric、expected issues 和输出评分脚本

## Quick Start

第一次使用请从 `QUICKSTART.md` 开始。最短路径：

```bash
git clone https://github.com/Mark1017520/china-internet-compliance-codex-skills.git
cd china-internet-compliance-codex-skills
codex
```

在 Codex 中输入：

```text
$china-internet-compliance 请审查这个功能是否可以上线：
功能名称：AI 客服助手
业务类型：企业 SaaS 客服
上线地区：中国大陆
用户对象：企业商家、消费者
功能描述：根据商家知识库和订单状态自动回复售后问题
涉及数据：订单号、物流状态、用户咨询内容
第三方 SDK/API/模型：第三方大模型 API
是否涉及 AI/算法/AIGC：是
是否涉及 UGC/直播/评论/社交：否
是否涉及广告/营销/付费/交易：涉及售后交易信息
是否涉及未成年人：不确定
```

## Repository Structure

```text
.
├── AGENTS.md
├── CHANGELOG.md
├── CAPABILITIES.md
├── COMPANY_IMPLEMENTATION_GUIDE.md
├── CONTRIBUTING.md
├── FAQ.md
├── LEGAL_DISCLAIMER.md
├── LICENSE
├── QUICKSTART.md
├── README.md
├── SECURITY.md
├── SOURCE_MAINTENANCE.md
├── examples/
├── docs/
├── scripts/
├── .github/
├── .codex/
│   └── config.example.toml
└── .agents/
    └── skills/
        ├── china-internet-compliance/
        │   ├── SKILL.md
        │   ├── commands/
        │   ├── profiles/
        │   ├── references/
        │   ├── templates/
        │   ├── golden_examples/
        │   ├── connectors/
        │   ├── agents/
        │   ├── evals/
        │   ├── prompts/
        │   └── scripts/
        ├── china-product-compliance/
        ├── china-data-privacy-compliance/
        ├── china-ai-algorithm-compliance/
        ├── china-content-governance/
        ├── china-advertising-marketing/
        ├── china-platform-transaction/
        ├── china-game-virtual-assets/
        ├── china-payment-fintech-adjacent/
        ├── china-ip-open-source/
        ├── china-vendor-contract/
        └── china-regulatory-response/
```

## Installation

### Use as a repo-scoped Skill

Copy this package into the root of the repository where you want Codex to use the compliance workflow:

```bash
cp -R .agents AGENTS.md /path/to/your-repo/
```

Then start Codex from that repository root. Codex can read `AGENTS.md` and the repo-scoped skills under `.agents/skills`.

### Use as global Skills

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/china-* ~/.agents/skills/
```

Or use the helper script:

```bash
./scripts/install-global.sh
```

## Usage

Main router example:

```text
$china-internet-compliance 请按中国互联网公司全场景合规标准，审查以下功能是否可以上线：
功能名称：
业务类型：
上线地区：
用户对象：
功能描述：
涉及数据：
第三方 SDK/API/模型：
是否涉及 AI/算法/AIGC：
是否涉及 UGC/直播/评论/社交：
是否涉及广告/营销/付费/交易：
是否涉及未成年人：
是否涉及开源组件、第三方素材、竞品内容或对外分发代码：
```

Specialist examples:

```text
$china-data-privacy-compliance 请评估这个功能是否需要个人信息保护影响评估、单独同意或数据出境评估。
$china-ai-algorithm-compliance 请审查这个 AI Agent 功能的算法、AIGC 标识、模型供应商和工具调用风险。
$china-ip-open-source 请分析这些依赖和开源许可证在 SaaS、Docker 镜像、私有化部署场景下的义务。
```

Command-style examples:

```text
/china-compliance:quick_triage
/china-compliance:launch_review
/china-compliance:data_pia
/china-compliance:ai_algorithm_review
/china-compliance:oss_review
/china-compliance:regulatory_response
/china-compliance:cold_start_interview
```

## Recommended Workflow

1. 初次接入公司环境时，先运行 `commands/cold_start_interview.md`，再基于 `profiles/*.template.md` 形成公司风险偏好与审批口径。
2. 对重大结论，使用 `references/CITATION_GUARDRAILS.md` 和 `references/SOURCE_VERIFICATION_RULES.md` 标记依据核验状态。
3. 对 PRD、代码依赖、SDK 清单、合同库、数据地图等资料，按 `connectors/` 中的规范接入或手动提供。
4. 对高风险事项，输出应包含 `结论 - 依据 - 证据 - 责任方 - 上线 gate`。
5. 对法规和监管规则高度变化的事项，按 `references/UPDATE_POLICY.md` 标记需要核对最新版官方规则。

## Validation

Run the built-in validator:

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

Expected result:

```text
[OK] china-internet-compliance skill package is valid.
```

## Version Notes

Current package version: `V1.0.3`.

`V1.0.3` is the project naming and slug alignment release. `V1.0.2` was the release tag alignment version, `V1.0.1` was the public release polish version, and `V1.0.0` was the initial public release. The current package includes:

- Specialist deepening: each specialist Skill includes judgment trees, required inputs, P0/P1 triggers and evidence requirements.
- Command execution: each command has a stable workflow contract and quality threshold.
- Evaluation pack: expected issues for 120 test cases, legal correctness rubric, benchmark and output evaluator. The evaluator is an auxiliary structure/coverage checker, not an automated legal-correctness judge.

See `CHANGELOG.md` for details.

## Project Docs

- `QUICKSTART.md`：下载、安装、首次调用和常见问题
- `CAPABILITIES.md`：已实现能力、部分实现能力和仅为规范的能力边界
- `COMPANY_IMPLEMENTATION_GUIDE.md`：从通用包落地为公司合规助手的实施指南
- `FAQ.md`：安装、调用、全局使用、法律边界和排错问答
- `examples/`：可复制的典型场景提示词
- `CONTRIBUTING.md`：贡献规则、模板、测试用例和法规来源的流程
- `SECURITY.md`：敏感信息和安全问题报告规则
- `LEGAL_DISCLAIMER.md`：法律意见边界、来源核验和数据处理提醒
- `SOURCE_MAINTENANCE.md`：法规、监管规则、标准和平台规则的维护机制
- `docs/architecture.md`：Skill 套件架构、路由模型和评测模型
- `docs/github-actions/validate.yml`：可复制到 `.github/workflows/` 的 GitHub Actions 校验模板
- `docs/releases/V1.0.3.md`：当前版本 Release Notes
- `docs/releases/V1.0.2.md`：发布 tag 对齐版本 Release Notes
- `docs/releases/V1.0.1.md`：发布打磨版本 Release Notes
- `docs/releases/V1.0.0.md`：首个公开版本 Release Notes

## Utility Scripts

- `scripts/install-global.sh`：安装所有 `china-*` Skills 到 `~/.agents/skills`
- `scripts/check-install.sh`：检查全局 Skill 是否安装完整
- `scripts/uninstall-global.sh`：从全局目录卸载本项目 Skills
- `scripts/package-release.sh`：基于当前 Git HEAD 生成发布 zip 包

## License

MIT License. Copyright (c) 2026 Mark.
