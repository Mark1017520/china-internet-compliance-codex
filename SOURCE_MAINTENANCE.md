# Source Maintenance

本项目涉及法规、监管规则、国家标准、行业规范、平台规则和企业合规流程。为了避免静态知识过期，维护者应按本文件管理来源、核验状态和更新节奏。

## 来源分级

| 等级 | 来源类型 | 使用方式 |
|---|---|---|
| S1 | 官方法律法规、部门规章、国家标准、监管机构公告 | 可作为高优先级依据，但仍需核验生效状态 |
| S2 | 官方指南、问答、备案系统说明、监管公开案例 | 可辅助解释规则，需标注适用边界 |
| S3 | 行业协会、平台规则、SDK/云服务商官方文档 | 用于平台或生态规则判断，需标注来源主体 |
| S4 | 企业内部制度、历史审批口径、合同模板 | 只能作为内部规则或风险偏好，不应写成外部法律要求 |
| S5 | 静态经验、二手资料、未核验材料 | 只能作为待核验线索 |

## 核验状态

输出和规则库中建议使用以下状态：

- `已核验依据`：已核对官方或可验证来源，并记录核验时间。
- `待核验依据`：来自静态 Skill 知识或二手线索，需要人工核对。
- `已过期/疑似过期`：来源被废止、替代，或存在较大变化迹象。
- `内部规则/风险偏好`：来自企业内部制度或管理要求。
- `事实假设`：用户材料不足时的条件性假设。

## 高变化领域

以下领域建议至少每季度复核一次；遇到监管更新时应立即复核：

- AI、算法、AIGC、深度合成、自动化决策、模型备案
- 数据出境、个人信息保护影响评估、重要数据、跨境供应商
- 未成年人保护、游戏、虚拟资产、概率玩法
- 金融、支付、分账、信贷/保险/理财导流
- 广告、直播带货、抽奖、价格、特殊行业营销
- App 权限、SDK、终端权限、个人信息清单
- 平台治理、网络交易、商家/达人/开发者生态规则

## 更新流程

1. 在 `SOURCE_INDEX.yaml` 中新增或更新来源条目。
2. 标注来源名称、发布主体、官方链接、发布日期、生效日期和核验日期。
3. 更新相关 reference、template、command 或 specialist Skill。
4. 如规则变化影响输出判断，补充或修改 test cases、expected issues 和 golden examples。
5. 运行校验脚本。
6. 在 `CHANGELOG.md` 中记录变更类型和影响范围。

## 文件位置

主要来源索引：

```text
.agents/skills/china-internet-compliance/references/SOURCE_INDEX.yaml
```

来源核验规则：

```text
.agents/skills/china-internet-compliance/references/SOURCE_VERIFICATION_RULES.md
.agents/skills/china-internet-compliance/references/CITATION_GUARDRAILS.md
.agents/skills/china-internet-compliance/references/UPDATE_POLICY.md
```

## 社区提交要求

提交来源更新时，请尽量提供：

- 官方或可验证链接
- 发布主体
- 生效或更新时间
- 影响的业务场景
- 建议修改的 Skill、command、template 或 eval 文件
- 是否存在过渡期、旧规则废止或新旧并行

不要提交付费数据库全文、保密法律意见、内部监管沟通记录或未经授权的第三方材料。
