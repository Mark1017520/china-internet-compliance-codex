# FAQ

## 这个项目下载后可以直接用吗？

可以。它是 Codex Skill 套件，不是 Web 服务或命令行程序。只要 Codex 启动目录里能看到 `AGENTS.md` 和 `.agents/skills`，就可以调用。

最短路径：

```bash
git clone https://github.com/Mark1017520/china-internet-compliance-codex-skills.git
cd china-internet-compliance-codex-skills
codex
```

## Codex 没有识别 Skill 怎么办？

确认当前目录存在：

```text
AGENTS.md
.agents/skills/china-internet-compliance/SKILL.md
```

如果你是在业务项目中使用，请把 `.agents` 和 `AGENTS.md` 复制到业务项目根目录，然后从业务项目根目录启动 Codex。

## 全局安装和项目级安装有什么区别？

项目级安装适合让 Codex 同时读取业务仓库和合规 Skill：

```bash
cp -R .agents AGENTS.md /path/to/your-project/
```

全局安装适合在多个项目里都能直接调用：

```bash
./scripts/install-global.sh
```

项目级安装更适合团队协作和固定版本；全局安装更适合个人日常使用。

## 如何确认安装成功？

运行：

```bash
./scripts/check-install.sh
```

也可以运行包校验：

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

## 常用调用方式是什么？

主控路由：

```text
$china-internet-compliance 请审查以下功能是否可以上线：...
```

专项审查：

```text
$china-data-privacy-compliance 请评估是否需要个人信息保护影响评估。
$china-ai-algorithm-compliance 请审查 AI、算法、AIGC 和模型供应商风险。
$china-ip-open-source 请分析这些开源依赖的许可证义务。
```

## 能不能把输出当正式法律意见？

不能。本项目用于合规初审、风险识别、工作底稿和评审流程辅助，不替代律师或企业法务的正式法律意见。

涉及重大监管、诉讼、刑事、金融、医疗、未成年人、数据出境、重要数据、算法备案、生成式 AI 备案、公安调证或重大知识产权争议等事项，应由企业法务、外部律师、安全、隐私或管理层复核。

## 为什么输出经常提示“需核验最新版官方规则”？

这是预期行为。合规规则会变化，尤其是 AI/AIGC、算法备案、数据出境、未成年人、金融、游戏、广告和平台治理领域。项目内置知识只能作为结构化初审基础，重大结论应核验最新官方文本和企业内部制度。

## 可以把真实合同、客户数据或监管材料贴给 Codex 吗？

不要在未经批准的外部环境中上传真实个人信息、客户数据、合同、监管文书、安全凭据或内部机密。公开 Issue、PR 和示例也必须脱敏。

## 怎么贡献新的场景？

优先新增或修改这些位置：

```text
examples/
.agents/skills/china-internet-compliance/prompts/test_cases.md
.agents/skills/china-internet-compliance/evals/expected_issues.json
.agents/skills/china-internet-compliance/golden_examples/
```

提交前运行：

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

更多规则见 `CONTRIBUTING.md`。

## 怎么启用 GitHub Actions？

当前 workflow 模板在：

```text
docs/github-actions/validate.yml
```

启用时复制到：

```text
.github/workflows/validate.yml
```

注意：通过 GitHub CLI 或 OAuth token 推送 `.github/workflows/*` 需要 `workflow` scope。
