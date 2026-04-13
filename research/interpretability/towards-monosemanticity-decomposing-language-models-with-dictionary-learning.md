---
title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
url: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
date:
tags: ["research", "interpretability"]
---

## One-Liner

Decomposes transformer neurons into interpretable "features" using dictionary learning, finding 4000+ features in a 512-neuron layer that represent concepts like DNA sequences and legal language.

## Key Points

- Individual neurons are poor units of analysis—features (linear combinations of neuron activations) are better
- Decomposed a 512-neuron layer into 4000+ interpretable features
- Features represent specific concepts: DNA sequences, legal language, HTTP requests, Hebrew text, etc.
- Most model properties are invisible when examining individual neurons in isolation

## Related

- [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
