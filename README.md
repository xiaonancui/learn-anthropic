# learn-anthropic 📚

> A structured, community-driven guide to everything Anthropic publishes.

从研究论文到工程实践，从模型发布到安全政策——把 Anthropic 公开的 390+ 页面整理成你可以学完的知识体系。

## 为什么做这个

Anthropic 的公开内容质量极高，但散落在网站各处。研究论文、工程博客、新闻公告混在一起，没有学习路径，没有优先级，没有关联。你很可能读了一篇论文，却不知道它在工程中怎么落地。

这个项目解决的就是这个问题。

## 内容结构

```
learn-anthropic/
├── research/                      # 研究论文与技术报告 (111 篇)
│   ├── interpretability/          # 可解释性 — Transformer 电路、单义性、特征分析
│   ├── alignment/                 # 对齐 — Constitutional AI、潜伏代理、红队测试
│   ├── evals/                     # 评估 — 系统评估、统计方法、SWE-bench
│   ├── economics/                 # 经济研究 — 经济指数、劳动力影响
│   ├── agents/                    # Agent — 构建、评估、长运行
│   └── circuits/                  # Circuits 更新系列
├── engineering/                   # 工程博客 (23 篇)
│   ├── agents.md                  # Agent 构建系列
│   ├── claude-code.md             # Claude Code 系列
│   ├── tools.md                   # 工具与 MCP
│   └── infrastructure.md          # 基础设施
├── news/                          # 新闻公告 (198 篇)
│   ├── model-releases/            # 模型发布
│   ├── partnerships/              # 合作伙伴
│   ├── safety/                    # 安全与红队
│   ├── policy/                    # 政策与监管
│   ├── education/                 # 教育
│   ├── enterprise/                # 企业与行业
│   └── funding/                   # 融资与扩张
├── data/                          # 原始数据
│   ├── sitemap.json               # 完整 sitemap（含 lastmod）
│   └── categories.json            # 分类映射
└── scripts/                       # 工具脚本
    └── fetch-sitemap.sh           # 更新 sitemap
```

## 学习路径

### 入门（1-2 天）
1. [Claude 的宪法](https://www.anthropic.com/constitution) — 理解 Anthropic 的核心哲学
2. [AI 安全核心观点](https://www.anthropic.com/news/core-views-on-ai-safety) — 他们怎么看待 AI 风险
3. [负责任扩展政策](https://www.anthropic.com/responsible-scaling-policy) — 量化安全承诺

### 进阶（1-2 周）
4. [构建有效 Agent](https://www.anthropic.com/research/building-effective-agents) — Agent 设计模式
5. [Constitutional AI](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) — 对齐方法论
6. [Claude Code 最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices) — 工程实战

### 深入（持续）
7. [可解释性系列](research/interpretability/) — 从 Transformer 电路到单义性
8. [Agent 工程系列](engineering/agents.md) — 从工具设计到长运行架构
9. [安全与红队系列](news/safety/) — 从检测到防御

## 核心概念索引

| 概念 | 关键页面 | 一句话 |
|------|---------|--------|
| Constitutional AI | [论文](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) | 用 AI 反馈替代人类反馈来训练无害性 |
| MCP | [公告](https://www.anthropic.com/news/model-context-protocol) | 让 AI 连接外部工具和数据的开放协议 |
| Responsible Scaling | [政策](https://www.anthropic.com/responsible-scaling-policy) | 按能力等级逐步加强安全措施 |
| Sleeper Agents | [论文](https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) | 安全训练可能无法消除的潜在欺骗行为 |
| Interpretability | [系列](research/interpretability/) | 理解模型内部在"想"什么 |
| Computer Use | [公告](https://www.anthropic.com/news/developing-computer-use) | 让 Claude 操作电脑 |
| Many-shot Jailbreaking | [论文](https://www.anthropic.com/research/many-shot-jailbreaking) | 长上下文越狱攻击 |

## 快速统计

| 板块 | 数量 | 最后更新 |
|------|------|---------|
| 研究论文 | 111 | 2026-04-08 |
| 工程博客 | 23 | 2026-04-10 |
| 新闻公告 | 198 | 2026-04-10 |
| 法律条款 | 16 | 2026-04-10 |
| 活动 | 9 | 2026-04-11 |
| **总计** | **390** | |

## 贡献

欢迎贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**当前最需要帮助的：**
- 为每篇研究论文补充一句话摘要
- 为工程博客补充技术关键词标签
- 发现 sitemap 中缺失的页面

## 更新

运行 `scripts/fetch-sitemap.sh` 获取最新页面列表：

```bash
bash scripts/fetch-sitemap.sh
```

## License

本项目内容采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可。
原始内容版权归 Anthropic 所有。本项目仅整理链接和元数据，不复制原始内容。
