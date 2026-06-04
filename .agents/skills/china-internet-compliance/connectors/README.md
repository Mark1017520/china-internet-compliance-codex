# Connectors — V1.0.3 连接器规范

本目录不是实际连接器代码，而是为后续接入企业系统、法规模块或 MCP 工具提供的数据契约。若企业已有相应工具，可按本规范输出结构化材料供 Skill 使用。

## 连接器分类

| 连接器 | 目的 |
|---|---|
| legal_research_connector | 查询官方法规、监管规则、国家标准、行政处罚、裁判文书 |
| internal_policy_connector | 查询公司内部制度、审批流程、历史合规口径 |
| product_requirement_connector | 读取 PRD、需求单、设计稿、上线计划、灰度策略 |
| code_dependency_connector | 读取依赖清单、包管理文件、代码分发方式 |
| sbom_sca_connector | 读取 SCA/SBOM、许可证、漏洞、组件来源 |
| sdk_inventory_connector | 读取 App/SDK 清单、权限、初始化时机、数据共享 |
| data_map_connector | 读取数据字段、数据流、存储、出境、接收方 |
| ai_model_registry_connector | 读取模型供应商、模型用途、备案、安全评估、AIGC标识 |
| contract_repository_connector | 读取供应商合同、DPA、SLA、审计权、退出条款 |
| incident_evidence_repository_connector | 读取监管/公安/诉讼证据材料、日志、导出记录、审批链路 |

## 输出原则

连接器输出应包含：

- 来源系统；
- 文件/记录名称；
- 版本或更新时间；
- 责任方；
- 摘要；
- 原文引用位置；
- 是否包含敏感信息；
- 是否允许纳入模型上下文。
