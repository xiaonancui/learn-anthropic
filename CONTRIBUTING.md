# Contributing to learn-anthropic

感谢你有兴趣贡献！

## 怎么贡献

### 最简单的：补充一句话摘要

每篇论文/文章都应该有一句话说明"这篇在讲什么"。如果你读过某篇，直接改对应的文件，加一句话就行。

### 发现缺失页面

运行 `scripts/fetch-sitemap.sh` 对比当前数据，如果发现新的页面，提交 PR 更新 `data/sitemap.json`。

### 写深度解读

如果你对某篇论文或某个系列有深入理解，欢迎写解读。格式参考 `research/interpretability/` 下的模板。

### 改进学习路径

你觉得学习路径的顺序不对？某个概念应该放在更前面？直接提 issue 讨论。

## 目录规范

- `research/` 下按主题分类，文件名用页面 slug
- `engineering/` 下按系列分文件，多个页面合并在一个 md 里
- `news/` 下只收录有学习价值的，纯商业公告不单独建文件
- 每个文件开头用 YAML frontmatter 标注元数据

## 文件模板

```markdown
---
title: 论文/文章标题
url: https://www.anthropic.com/research/xxx
date: YYYY-MM-DD
tags: [tag1, tag2]
---

## 一句话

这篇在讲什么——一句话版本。

## 要点

- 要点 1
- 要点 2

## 关联

- 相关论文/文章链接
```

## 不做什么

- ❌ 不复制 Anthropic 的原始内容
- ❌ 不做论文翻译（只做摘要和解读）
- ❌ 不收录非公开内容

## License

贡献采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可。
