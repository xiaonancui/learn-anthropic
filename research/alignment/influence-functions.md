---
title: "Tracing Model Outputs to the Training Data"
url: https://www.anthropic.com/research/influence-functions
date: 2023-08
tags: ["research", "alignment"]
---

## One-Liner

Uses influence functions to trace which training examples contribute to model outputs, finding that generalization patterns become more abstract with model scale.

## Key Points

- Scaled influence functions up to 52B parameter models
- Patterns of generalization become more abstract with model scale
- Cross-lingual influence gets stronger with model size
- Model outputs don't result from pure memorization - influence follows power law
- Influence is distributed across layers but localized for specific queries

## Related

- [Tracing Model Outputs to the Training Data](https://www.anthropic.com/research/influence-functions)
- [Read Paper (arXiv)](https://arxiv.org/abs/2308.03296)
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
