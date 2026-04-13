---
title: "Mapping the Mind of a Large Language Model"
url: https://www.anthropic.com/research/mapping-mind-language-model
date: 2024-05-21
tags: ["research", "interpretability"]
---

## One-Liner

First detailed look inside a production-grade LLM, extracting millions of interpretable features from Claude Sonnet that correspond to concepts from cities to safety concerns.

## Key Points

- Extracted millions of features from Claude 3.0 Sonnet using dictionary learning
- Features range from concrete entities (Golden Gate Bridge, cities) to abstract concepts (gender bias, secrets)
- Features are multimodal and multilingual—respond to images and text in many languages
- Can manipulate features to change behavior (e.g., making Claude obsessed with Golden Gate Bridge)
- Found safety-relevant features: scam emails, bias, sycophancy, power-seeking
- Internal concept organization corresponds to human notions of similarity

## Related

- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model)
- [Read the paper](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)
- [Policy Memo (PDF)](https://cdn.sanity.io/files/4zrzovbb/website/e2ae0c997653dfd8a7cf23d06f5f06fd84ccfd58.pdf)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
