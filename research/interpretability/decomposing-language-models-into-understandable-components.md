---
title: "Decomposing Language Models Into Understandable Components"
url: https://www.anthropic.com/research/decomposing-language-models-into-understandable-components
date: 2023-10
tags: ["research", "interpretability"]
---

## One-Liner

Decomposes transformer layers into interpretable "features" using dictionary learning, finding features that represent specific concepts and are more interpretable than individual neurons.

## Key Points

- Individual neurons are uninterpretable—features (patterns of neuron activations) are better units of analysis
- Decomposed a 512-neuron layer into 4000+ interpretable features
- Features represent specific concepts: DNA sequences, legal language, HTTP requests, Hebrew text, etc.
- Features are more interpretable than neurons (validated by human evaluators)
- Can steer model behavior by artificially activating features
- Features are largely universal between different models

## Related

- [Decomposing Language Models Into Understandable Components](https://www.anthropic.com/research/decomposing-language-models-into-understandable-components)
- [Read Paper](https://transformer-circuits.pub/2023/monosemantic-features/index.html)
- [Towards Monosemanticity](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
