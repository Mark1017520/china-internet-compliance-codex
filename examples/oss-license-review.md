# Example: 开源许可证审查

## 适用 Skill

`$china-ip-open-source` 或 `/china-compliance:oss-review`

## 提示词

```text
$china-ip-open-source 请分析以下开源依赖在 SaaS、Docker 镜像和私有化部署场景下的许可证义务：
项目形态：企业 SaaS 平台，另向部分客户交付 Docker 镜像和私有化部署包
依赖清单：
- react: MIT
- fastapi: MIT
- postgresql: PostgreSQL License
- elasticsearch: SSPL 或 Elastic License，版本待确认
- agpl-example-lib: AGPL-3.0
是否修改源码：AGPL 组件未修改，Elasticsearch 配置有改动
是否对外交付代码或镜像：会向客户交付 Docker 镜像
希望输出：许可证风险等级、触发义务、替代方案、上线 gate
```

## 期望输出检查点

- 是否区分 SaaS、镜像分发、私有化部署的触发条件
- 是否识别 AGPL、SSPL、Elastic License 的高风险点
- 是否提示版本核验和许可证文本核验
- 是否给出替换、隔离、移除、商业授权或开源披露方案
- 是否提醒生成 SBOM、保留 notice 和源码修改记录

## 需人工补充

- 精确版本号和许可证文本
- 是否修改源码或静态/动态链接
- 镜像中是否包含对应组件
- 客户合同中是否承诺源码、授权或第三方软件清单
