---
title: "Scaling Laws and Interpretability of Learning from Repeated Data"
url: https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data
date: 2022-05-21
tags: ["research", "alignment"]
---

## One-Liner

Finds strong double descent phenomenon where repeated data degrades performance—0.1% of data repeated 100 times can degrade an 800M model to perform like a 400M model.

## Key Points

- Repeated data causes double descent: test loss increases midway through training
- 0.1% of data repeated 100 times degrades 800M model performance to 2x smaller model level
- Suspects memorization of repeated data consumes large fraction of model's capacity
- Repeated data damages copying and internal structures like induction heads
- Provides mechanism for shift from generalization to memorization

## Related

- [Scaling Laws and Interpretability of Learning from Repeated Data](https://www.anthropic.com/research/scaling-laws-and-interpretability-of-learning-from-repeated-data)
- [Read Paper (arXiv)](https://arxiv.org/abs/2205.10487)
- [Superposition, Memorization, and Double Descent](https://www.anthropic.com/research/superposition-memorization-and-double-descent)
- [Toy Models of Superposition](https://www.anthropic.com/research/toy-models-of-superposition)
