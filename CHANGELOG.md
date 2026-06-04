# CHANGELOG

## Unreleased

- Added FAQ, source maintenance and architecture documentation.
- Added install check, uninstall and release packaging helper scripts.
- Added expected output examples for the public example prompts.

## V1.0.0 — Initial Public Release

首个公开发布版本，面向中国互联网业务场景的 Codex repo-scoped Skill 套件。

### Core Package

- Added the main router Skill `china-internet-compliance`.
- Added 11 specialist Skills covering product launch, data privacy, AI/algorithm, content governance, advertising/marketing, platform transactions, game/virtual assets, payment/fintech-adjacent features, IP/open source, vendor contracts and regulatory response.
- Added stable command workflows for quick triage, launch review, data PIA, AI review, OSS review, vendor review, regulatory response and cold-start interview.
- Added company profile templates for risk appetite, approval workflow, data classification, escalation matrix and output standards.

### Compliance Knowledge System

- Added reference libraries for scenario taxonomy, duty-level rules, article-level rules, risk matrix, citation guardrails, source verification and update policy.
- Added connector specifications for legal research, internal policies, product requirements, SBOM/SCA, SDK inventory, data map, model registry, contracts and incident evidence.
- Added watcher/reviewer agent specifications for regulatory change, open-source dependency, SDK permission, AI registry gap, vendor contract expiry, product launch and evidence response workflows.

### Evaluation Pack

- Added 120 full-scenario test cases.
- Added 30 golden examples.
- Added expected issue coverage data, legal correctness rubric, risk identification benchmark and output evaluator.
- Added `validate_skill.py` to verify the package structure and required files.

### Open Source Readiness

- Added `README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`, `SECURITY.md` and `LEGAL_DISCLAIMER.md`.
- Added copy-ready examples for AI customer service, App SDK permission review, marketing lottery review, OSS license review and regulatory evidence response.
- Added GitHub issue templates, pull request template, global install script and GitHub Actions validation template.
