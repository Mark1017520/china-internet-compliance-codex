# 代码依赖连接器

## 目的

为合规审查提供可追溯事实与依据。适用于：package.json、pom.xml、go.mod、requirements.txt、Dockerfile、镜像清单。

## 推荐输入字段

| 字段 | 说明 |
|---|---|
| source_system | 来源系统 |
| record_id | 记录ID或文件ID |
| title | 文件/记录名称 |
| version_or_modified_at | 版本或更新时间 |
| owner | 业务/系统责任方 |
| summary | 摘要 |
| extracted_facts | 结构化事实 |
| citations | 原文引用或定位 |
| sensitivity | 敏感级别 |
| access_scope | 允许访问范围 |

## 推荐输出给 Skill 的结构

```json
{
  "source_system": "",
  "title": "",
  "version_or_modified_at": "",
  "owner": "",
  "facts": [],
  "citations": [],
  "risk_flags": [],
  "open_questions": []
}
```

## 安全要求

- 不输出密钥、口令、token、完整身份证件号、银行卡号、未脱敏个人信息。
- 对公安、监管、诉讼证据类材料，应保留导出审批和交付链路。
- 若材料未经授权，不得纳入外部模型或不受控环境。
