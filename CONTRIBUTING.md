# Contributing

欢迎贡献新的场景、规则、模板、测试用例和改进建议。这个项目的目标是成为可复用、可校验、可持续维护的中国互联网合规 Codex Skill 套件。

## 可以贡献什么

- 新增业务场景：例如在线教育、招聘、医疗健康、酒旅、本地生活、开发者平台等
- 更新法规或监管来源：补充官方来源、核验状态、适用边界和更新时间
- 改进 Skill 指令：让事实抽取、风险识别、上线 gate、整改建议更稳定
- 增加模板：评审记录、PIA、供应商审查、监管响应、开源审查等
- 增加测试用例和 golden examples：覆盖更多真实但脱敏的业务形态
- 修复文档、命令、安装脚本或校验脚本问题

## 贡献前请注意

- 不要提交真实个人信息、客户数据、合同、监管材料、密钥、内部系统截图或未公开业务资料。
- 不要提交未经授权的第三方版权材料、付费数据库内容或受保密义务约束的材料。
- 涉及法规、监管规则、国家标准、官方问答或执法口径时，请尽量提供官方来源和核验日期。
- 重大法律结论应标记适用条件和不确定性，避免写成无条件、永久有效的结论。

## 本地校验

提交前请运行：

```bash
python3 .agents/skills/china-internet-compliance/scripts/validate_skill.py
```

成功输出应包含：

```text
[OK] china-internet-compliance skill package is valid.
```

## 修改 Skill 的建议

修改 `.agents/skills/**/SKILL.md` 时，请尽量保持：

- 输入字段明确
- 事实不足时仍能给出条件性初判
- 风险结论包含依据、证据、责任方和上线 gate
- 高风险结论区分已核验依据、待核验依据、内部规则和事实假设
- 不鼓励规避监管、规避身份核验、隐藏证据、绕过安全控制或删除日志

## 新增法规或来源

优先更新以下位置：

```text
.agents/skills/china-internet-compliance/references/SOURCE_INDEX.yaml
.agents/skills/china-internet-compliance/references/SOURCE_VERIFICATION_RULES.md
.agents/skills/china-internet-compliance/references/UPDATE_POLICY.md
```

建议说明：

- 来源名称
- 发布机关或组织
- 官方链接或可核验来源
- 生效时间或更新时间
- 适用场景
- 是否需要人工复核

## 新增示例

示例放在 `examples/`，建议包含：

- 适用 Skill
- 可复制提示词
- 期望输出检查点
- 需人工补充或核验的信息

示例必须脱敏，不应包含真实用户、公司、客户、合同、监管文书或系统信息。

## Pull Request 检查清单

提交 PR 前请确认：

- 已运行本地校验脚本
- README 或 QUICKSTART 已按需更新
- 新增规则有来源或适用边界说明
- 新增高风险结论没有被写成绝对法律意见
- 没有提交敏感信息、密钥或内部材料

## License

提交贡献即表示你同意贡献内容按本项目 MIT License 发布。
