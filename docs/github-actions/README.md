# GitHub Actions Templates

`validate.yml` 是本项目的 Skill 包校验 workflow 模板。

启用方式：

```bash
mkdir -p .github/workflows
cp docs/github-actions/validate.yml .github/workflows/validate.yml
git add .github/workflows/validate.yml
git commit -m "Enable skill package validation workflow"
git push
```

注意：通过 GitHub CLI 或 OAuth token 推送 `.github/workflows/*` 时，token 需要 `workflow` scope。没有该权限时，GitHub 会拒绝推送 workflow 文件。
