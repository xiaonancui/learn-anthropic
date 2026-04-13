---
title: "Privileged Bases in the Transformer Residual Stream"
url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
date: 2023-03-16
tags: ["research", "interpretability"]
---

## One-Liner

Investigates why individual coordinates in the transformer residual stream have special significance, attributing the effect to per-dimension normalizers in the Adam optimizer.

## Key Points

- Mathematical theories suggest basis directions in residual stream should be arbitrary
- In practice, individual coordinates have special significance and encode information preferentially
- Per-dimension normalizers in Adam optimizer are the likely cause
- Rules out Layer normalization and floating-point calculations as sources

## Related

- [Privileged Bases in the Transformer Residual Stream](https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream)
- [Read Paper](https://transformer-circuits.pub/2023/privileged-basis/index.html)
