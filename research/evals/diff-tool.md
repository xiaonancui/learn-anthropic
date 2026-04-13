---
title: "A ""diff"" tool for AI: Finding behavioral differences in new models"
source: "https://www.anthropic.com/research/diff-tool"
language: "en"
description: "Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems."
word_count: 2061
url: https://www.anthropic.com/research/diff-tool
date:
tags: ["research", "evals"]
---

Interpretability

[Read the paper](https://arxiv.org/abs/2602.11729)

Every time a new AI model is released, its developers run a suite of evaluations to measure its performance and safety. These tests are essential, but they are somewhat limited. Because these benchmarks are human-authored, they can only test for risks we have already conceptualized and learned to measure.

This approach to safety is inherently *reactive*. It's effective at catching known problems, but by definition, it's incapable of discovering "unknown unknowns"—the novel, emergent behaviors that pose some of the most subtle risks in new models. Auditing a new model from scratch is like being handed a million lines of code and told to "find the security flaws." It's an almost impossible task when you don't know what you're looking for.

In software engineering, whenever a program is updated, developers face this exact problem of identifying a small, critical change within a vast sea of code. This is why "[diff](https://en.wikipedia.org/wiki/Diff)" tools were invented. No programmer would ever audit a million lines from scratch to approve an update; instead, they review only the 50 lines that have actually changed, as directed by their diff tool.

We think a similar approach can be applied to AI safety. When a new version of a model is released, we don't need to re-audit it from scratch. We can instead use a "diff" tool to identify the specific behavioral changes between the old and new versions, and then focus our auditing efforts on those changes.

In a [new paper](https://arxiv.org/abs/2602.11729), we describe our work on building such a "diff" tool for AI models. Our approach is based on comparing the distributions of model behaviors across a large number of prompts, and identifying statistically significant differences between two versions of a model.

## How it works

Our diff tool works by comparing the outputs of two versions of a model on the same set of prompts. We use a variety of statistical methods to identify behavioral differences, including:

1. **Output distribution comparison**: We compare the probability distributions over tokens for the two models, and identify tokens where the distributions differ significantly.
2. **Behavioral clustering**: We cluster model behaviors based on their outputs, and identify clusters that appear or disappear between versions.
3. **Feature-level analysis**: We use sparse autoencoders to identify features that activate differently between the two model versions.

Our tool is designed to be general-purpose: it can be applied to any pair of models, and it can detect a wide range of behavioral differences, from subtle shifts in tone to dramatic changes in capabilities.

## Results

We tested our diff tool on several pairs of models, including different versions of Claude. We found that our tool was able to identify a wide range of behavioral differences, including:

- Changes in helpfulness and harmlessness
- Shifts in political bias
- Differences in factual accuracy
- Changes in code generation quality
- Shifts in creative writing style

Our tool was also able to identify "unknown unknowns"—novel behaviors that we hadn't anticipated. For example, when comparing two versions of a model, we found that one version was significantly more likely to express uncertainty about its own knowledge, while the other was more likely to assert false claims with confidence.

## Implications for AI safety

We believe that diff tools like this one could be an important addition to the AI safety toolkit. By focusing auditing efforts on the specific behavioral differences between model versions, we can:

1. **Discover novel risks**: By comparing two versions of a model, we can identify emergent behaviors that weren't present in the original version.
2. **Improve auditing efficiency**: By focusing on the changes, we can audit models more efficiently than by starting from scratch.
3. **Enable continuous monitoring**: By running diff tools regularly, we can track how model behaviors change over time and identify potential issues early.

We believe that this approach is complementary to existing safety evaluations. While traditional benchmarks test for known risks, diff tools can help us discover unknown risks.

## Limitations

Our diff tool has several limitations:

1. **Coverage**: Our tool can only detect differences that are present in the prompts we test. If a behavioral difference only appears on prompts we haven't tested, we won't detect it.
2. **Interpretability**: While our tool can identify behavioral differences, it doesn't always explain why those differences occur.
3. **False positives**: Some detected differences may be spurious, especially when comparing models that are very similar.

Despite these limitations, we believe that diff tools are a valuable addition to the AI safety toolkit, and we plan to continue developing and improving our approach.

Read the [full paper](https://arxiv.org/abs/2602.11729) for more details.

## Acknowledgements

This research was conducted by members of Anthropic's Alignment Science and Interpretability teams.