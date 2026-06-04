# 输入事实 Schema 与追问策略

> 目标：让 Codex 在信息不完整时也能稳定输出“基于现有事实的初判 + 待确认问题”，避免遗漏关键合规触发点。

## 1. 通用输入字段

每次审查优先抽取以下字段：

```yaml
project:
  name: ""
  business_type: ""
  scenario_summary: ""
  launch_region: "中国大陆/港澳台/海外/跨境"
  target_users: ["C端用户", "企业客户", "未成年人", "商家", "开发者", "主播/达人", "内部员工"]
  external_facing: true/false/unknown
  launch_stage: "PRD/灰度/正式上线/下线/回滚/监管响应"
  rollback_available: true/false/unknown

data:
  personal_info: []
  sensitive_personal_info: []
  minors_data: true/false/unknown
  important_data_possible: true/false/unknown
  data_source: ["用户提交", "系统日志", "第三方", "公开抓取", "企业客户上传", "模型生成"]
  data_sharing: []
  cross_border: true/false/unknown
  retention_period: ""
  deletion_mechanism: ""

third_parties:
  sdk_api_model_cloud_vendor: []
  role: "委托处理/共同处理/独立处理/对外提供/技术支持/不明"
  contract_or_dpa: true/false/unknown
  subprocessor: true/false/unknown

ai_algorithm:
  involved: true/false/unknown
  type: ["推荐", "排序", "搜索", "生成式AI", "深度合成", "自动化决策", "Agent", "RAG"]
  public_opinion_or_social_mobilization: true/false/unknown
  aigc_label: true/false/unknown
  human_review: true/false/unknown

content_platform:
  ugc: true/false/unknown
  comments_live_chat_social: []
  moderation: true/false/unknown
  report_appeal: true/false/unknown
  log_retention: true/false/unknown

commercial:
  ads_marketing: true/false/unknown
  transaction_payment: true/false/unknown
  virtual_assets: true/false/unknown
  lottery_probability: true/false/unknown
  pricing_or_discount: true/false/unknown

ip_open_source:
  third_party_content_code_material: []
  competitor_reference: true/false/unknown
  open_source_components: []
  distribution: ["不分发", "源码", "二进制", "SDK", "App", "Docker镜像", "插件", "私有化部署"]
  license_scan_done: true/false/unknown

regulatory_response:
  authority: ""
  document_type: ""
  requested_scope: ""
  materials_to_provide: []
  sensitive_internal_info: []
```

## 2. 信息不足时的默认处理

- 不因信息不足而停止分析。
- 输出应包含：
  1. 已知事实；
  2. 关键假设；
  3. 可能触发的合规场景；
  4. 基于现有事实的初判；
  5. 必须确认的问题；
  6. 在确认前不得上线/不得对外提供/不得承诺低风险的事项。

## 3. 高优先级追问清单

### 数据/隐私
1. 是否收集个人信息、敏感个人信息或未成年人信息？
2. 数据来源是什么？用户提交、企业客户上传、第三方购买/接口、公开抓取、系统日志？
3. 是否向第三方提供、委托处理、共同处理或跨境传输？
4. 是否已更新隐私政策、个人信息清单、SDK清单？
5. 是否完成 PIA 或数据出境路径判断？

### AI/算法
1. 是否直接面向公众提供生成式AI或深度合成功能？
2. 是否具有舆论属性或社会动员能力？
3. 是否对生成内容设置显式/隐式标识？
4. 模型供应商、部署地区、训练/输入/输出数据处理方式是什么？
5. 是否有人工复核、投诉纠错、违规内容拦截？

### 内容/社区/直播
1. 用户是否可发布、评论、私信、直播或上传音视频？
2. 是否有内容审核、举报、申诉、账号处罚和日志留存？
3. 是否涉及未成年人、主播、达人、群聊、打赏、同城或陌生人社交？
4. 是否存在违法有害信息、诈骗、赌博、色情低俗、侵权、虚假宣传风险？

### 广告/营销/交易
1. 是否构成广告或商业推广？是否显著标明广告？
2. 是否涉及抽奖、返利、充值、会员、虚拟道具、概率玩法？
3. 是否涉及特殊行业广告、未成年人广告或价格优惠承诺？
4. 是否有完整活动规则、奖品、概率、限制条件、退款规则？

### 开源/IP
1. 第三方代码、素材、字体、图片、模型、数据集来源是什么？
2. 许可证是什么？是否允许商业使用、修改、分发、SaaS使用？
3. 是否复制竞品页面、主题、文案、接口文档或测试数据？
4. 是否对外分发源码、二进制、SDK、App、Docker镜像、私有化包？
5. 是否做过 SCA/SBOM/secret scan？

### 监管/公安/诉讼
1. 文书主体、案由、范围、时间、字段是否明确？
2. 拟提供材料是否超范围、含无关客户或内部敏感信息？
3. 原始日志、整理表、订单/金额、账号/域名是否口径一致？
4. 是否需要脱敏、字段解释、流程图、盖章、审批留痕？

## 4. 输出时的信息完整度评级

| 评级 | 判断标准 | 输出处理 |
|---|---|---|
| A | 事实充分，字段完整，有文档/截图/表格/技术方案 | 可给明确风险等级和上线 gate |
| B | 核心事实具备，但缺合同/数据流/第三方/上线地区等 | 给初判 + 待确认问题 + 条件性结论 |
| C | 仅有一句功能描述或截图 | 不给低风险结论；列出可能场景和最小必问问题 |
| D | 监管/调证/事故场景但缺原文文书或材料清单 | 原则上 P1 以上，要求补充原文文书和拟提供材料 |
