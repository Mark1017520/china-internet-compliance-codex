# Quick Start

这个项目是 Codex Skill 套件，不是需要部署的 Web 服务。只要让 Codex 在能读取 `.agents/skills` 和 `AGENTS.md` 的位置启动，就可以调用这些合规评审能力。

## 方式一：直接在本仓库使用

```bash
git clone https://github.com/Mark1017520/china-internet-compliance-codex.git
cd china-internet-compliance-codex
codex
```

在 Codex 中输入：

```text
$china-internet-compliance 请审查以下功能是否可以上线：
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

## 方式二：复制到你的业务项目

如果你希望 Codex 在某个业务仓库里使用这些 Skill：

```bash
cp -R .agents AGENTS.md /path/to/your-project/
cd /path/to/your-project
codex
```

适合场景：你要让 Codex 同时读取业务代码、PRD、配置文件和本合规 Skill。

## 方式三：安装为全局 Skill

```bash
./scripts/install-global.sh
```

等价于：

```bash
mkdir -p ~/.agents/skills
cp -R .agents/skills/china-* ~/.agents/skills/
```

适合场景：你希望在多个项目中都能直接调用这些 Skill。

## 常用调用

主控路由：

```text
$china-internet-compliance 请按中国互联网公司全场景合规标准，审查以下功能是否可以上线：...
```

专项审查：

```text
$china-data-privacy-compliance 请评估这个功能是否需要个人信息保护影响评估、单独同意或数据出境评估。
$china-ai-algorithm-compliance 请审查这个 AI Agent 功能的算法、AIGC 标识、模型供应商和工具调用风险。
$china-ip-open-source 请分析这些依赖和开源许可证在 SaaS、Docker 镜像、私有化部署场景下的义务。
```

Command 风格：

```text
/china-compliance:quick-triage
/china-compliance:launch-review
/china-compliance:data-pia
/china-compliance:ai-algorithm-review
/china-compliance:oss-review
/china-compliance:regulatory-response
/china-compliance:cold-start-interview
```

## 校验安装包

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

成功时应看到：

```text
[OK] china-internet-compliance skill package is valid.
```

## 常见问题

### Codex 没有识别 Skill

确认启动目录下存在：

```text
AGENTS.md
.agents/skills/china-internet-compliance/SKILL.md
```

如果你使用全局安装，确认文件已复制到：

```text
~/.agents/skills/china-internet-compliance/SKILL.md
```

### `python` 命令不存在

使用 `python3`：

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

### 输出中出现“需核验最新版官方规则”

这是预期行为。监管规则、备案要求、数据出境、AI/AIGC、金融、游戏、未成年人等领域变化较快，重大结论应核对官方最新文本和企业内部制度。

### 是否可以直接当法律意见使用

不可以。本项目用于合规初审、工作底稿和风险识别，不替代律师或企业法务的正式法律意见。
