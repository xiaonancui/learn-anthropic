---
title: "Measuring Faithfulness in Chain-of-Thought Reasoning"
url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
date:
tags: ["research", "alignment"]
source: "https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning"
language: "en"
description: "Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems."
word_count: 166
---

## Abstract

Large language models (LLMs) perform better when they produce step-by-step, "Chain-ofThought" (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model's actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. CoT's performance boost does not seem to come from CoT's added test-time compute alone or from information encoded via the particular phrasing of the CoT. As models become larger and more capable, they produce less faithful reasoning on most tasks we study. Overall, our results suggest that CoT can be faithful if the circumstances such as the model size and task are carefully chosen.