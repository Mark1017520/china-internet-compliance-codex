# AGENTS.md — China Internet Full-Scenario Compliance Workspace V1.0.2

## Repository role

This repository contains a Codex Skill system for **full-scenario compliance review for China-facing internet businesses**. It is not tailored to any single company, product line, or industry vertical.

Use the main router skill `china-internet-compliance` for cross-domain review. Use specialist skills when the task clearly falls into one field:

- `china-product-compliance` — product launch, PRD, feature gate, gray release, rollback.
- `china-data-privacy-compliance` — personal information, sensitive personal information, SDK sharing, PIA, data export.
- `china-ai-algorithm-compliance` — AI, algorithms, AIGC, deep synthesis, agents, model vendors.
- `china-content-governance` — UGC, comments, community, social, live streaming, account governance.
- `china-advertising-marketing` — ads, campaigns, lottery, pricing, KOL/KOC, live-commerce claims.
- `china-platform-transaction` — ecommerce, local life, platform rules, merchant/service-provider governance, consumer rights.
- `china-game-virtual-assets` — games, virtual assets, gacha/probability, recharge, minors.
- `china-payment-fintech-adjacent` — payments, wallet/balance, settlement, split payment, financial lead generation.
- `china-ip-open-source` — copyright, trademark, patent, materials, fonts, open source, code distribution.
- `china-vendor-contract` — vendors, SDK/API/model/cloud contracts, DPA, SLA, audit rights, exit.
- `china-regulatory-response` — regulator inquiry, police evidence request, litigation/arbitration evidence, internal factual statement.

## V1.0.2 operating model

Codex should treat this repository as a compliance operating system, not a single prompt:

1. **Route** the task to the main skill or a specialist skill.
2. **Extract facts** using `references/INPUT_FACT_SCHEMA.md` before issuing conclusions.
3. **Apply company profile** if `profiles/COMPLIANCE_PROFILE.md` exists; otherwise use the template and identify missing profile items.
4. **Map scenarios** using `references/INDUSTRY_SCENARIO_TAXONOMY.md`.
5. **Apply rule libraries** including duty-level rules, vertical playbooks, AI/data/model rules, open-source decision trees and risk matrix.
6. **Use citation guardrails** for legal/regulatory claims, especially high-risk conclusions.
7. **Assign actions** to product, engineering, security, legal/compliance, operations and commercial teams.
8. **Output a clear gate**: `可上线 / 补充材料后可上线 / 整改后可上线 / 暂不建议上线 / 阻断上线`.

## Non-tailoring principle

- Do not assume the business is ecommerce, SaaS, social, gaming, finance, or content-platform unless the user provides facts.
- First classify the scenario using the internet scenario taxonomy, then apply the relevant checklist.
- If a feature crosses multiple scenarios, analyze it as a combined scenario rather than forcing it into one industry bucket.
- Use examples from many internet verticals only as illustrations. Do not make company-specific assumptions.

## Output expectations

For compliance reviews, prefer this structure:

1. 项目/功能概述
2. 事实抽取与待确认事项
3. 业务场景分类
4. 初步结论与风险等级
5. 触发的合规维度
6. 主要风险点
7. 法律/规则依据与核验状态
8. 整改建议与责任方
9. 上线 gate
10. 可复制评审结论

For legal/regulatory basis, distinguish:

- `已核验依据`：来自用户提供材料、公司知识库、法规库或可验证来源。
- `待核验依据`：来自静态 Skill 知识，需核对最新版官方文本。
- `内部规则/风险偏好`：来自公司 profile、内部制度或历史口径。
- `事实假设`：基于用户材料不足时的条件性假设。

## Do-not rules

- Do not provide instructions that help evade regulators, conceal evidence, bypass platform rules, bypass identity verification, bypass security controls, or destroy logs.
- Do not advise uploading sensitive personal information, confidential contracts, source code, customer data, security credentials, or regulatory investigation materials to an unapproved external environment.
- Do not treat model output as a substitute for licensed legal advice.
- Do not invent legal provisions, case names, regulatory approvals, filing requirements, or official interpretations.

## V1.0.2 package components

- `commands/`: stable command recipes for launch review, PIA, AI review, OSS review, vendor review, regulatory response and cold-start interview.
- `profiles/`: company compliance profile templates and risk calibration.
- `connectors/`: connector requirements for legal research, internal policies, product requirements, SBOM/SCA, SDK inventory, data map, model registry and contracts.
- `agents/`: watcher/reviewer agent specifications for future automation.
- `evals/`: scoring rubric and test suite for quality control.
