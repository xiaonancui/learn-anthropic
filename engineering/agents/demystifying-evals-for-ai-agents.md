---
title: "Demystifying evals for AI agents"
url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
date:
tags: ["engineering", "agents"]
source: "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
language: "en"
description: "Demystifying evals for AI agents"
word_count: 5965
---

## Introduction

Good evaluations help teams ship AI agents more confidently. Without them, it's easy to get stuck in reactive loops—catching issues only in production, where fixing one failure creates others. Evals make problems and behavioral changes visible before they affect users, and their value compounds over the lifecycle of an agent.

As we described in [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), agents operate over many turns: calling tools, modifying state, and adapting based on intermediate results. These same capabilities that make AI agents useful—autonomy, intelligence, and flexibility—also make them harder to evaluate.

Through our internal work and with customers at the frontier of agent development, we've learned how to design more rigorous and useful evals for agents. Here's what's worked across a range of agent architectures and use cases in real-world deployment.

## The structure of an evaluation

An **evaluation** ("eval") is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success. In this post, we focus on **automated evals** that can be run during development without real users.

**Single-turn evaluations** are straightforward: a prompt, a response, and grading logic. For earlier LLMs, single-turn, non-agentic evals were the main evaluation method. As AI capabilities have advanced, **multi-turn evaluations** have become increasingly common.

**Agent evaluations** are even more complex. Agents use tools across many turns, modifying state in the environment and adapting as they go—which means mistakes can propagate and compound. Frontier models can also find creative solutions that surpass the limits of static evals.

When building agent evaluations, we use the following definitions:

- A **task** (a.k.a **problem** or **test case**) is a single test with defined inputs and success criteria.
- Each attempt at a task is a **trial**. Because model outputs vary between runs, we run multiple trials to produce more consistent results.
- A **grader** is logic that scores some aspect of the agent's performance. A task can have multiple graders, each containing multiple assertions.
- A **transcript** (also called a **trace** or **trajectory**) is the complete record of a trial, including outputs, tool calls, reasoning, intermediate results, and any other interactions.
- The **outcome** is the final state in the environment at the end of the trial.
- An **evaluation harness** is the infrastructure that runs evals end-to-end.
- An **agent harness** (or **scaffold**) is the system that enables a model to act as an agent.
- An **evaluation suite** is a collection of tasks designed to measure specific capabilities or behaviors.

## Why build evaluations?

When teams first start building agents, they can get surprisingly far through a combination of manual testing, dogfooding, and intuition. More rigorous evaluation may even seem like overhead that slows down shipping. But after the early prototyping stages, once an agent is in production and has started scaling, building without evals starts to break down.

The breaking point often comes when users report the agent feels worse after changes, and the team is "flying blind" with no way to verify except to guess and check. Absent evals, debugging is reactive: wait for complaints, reproduce manually, fix the bug, and hope nothing else regressed. Teams can't distinguish real regressions from noise, automatically test changes against hundreds of scenarios before shipping, or measure improvements.

Writing evals is useful at any stage in the agent lifecycle. Early on, evals force product teams to specify what success means for the agent, while later they help uphold a consistent quality bar.

Evals also shape how quickly you can adopt new models. When more powerful models come out, teams without evals face weeks of testing while competitors with evals can quickly determine the model's strengths, tune their prompts, and upgrade in days.

Once evals exist, you get baselines and regression tests for free: latency, token usage, cost per task, and error rates can be tracked on a static bank of tasks. Evals can also become the highest-bandwidth communication channel between product and research teams, defining metrics researchers can optimize against.

## How to evaluate AI agents

### Types of graders for agents

Agent evaluations typically combine three types of graders: code-based, model-based, and human.

**Code-based graders** include string match checks, binary tests, static analysis, outcome verification, tool calls verification, and transcript analysis. They're fast, cheap, objective, reproducible, and easy to debug.

**Model-based graders** include rubric-based scoring, natural language assertions, pairwise comparison, reference-based evaluation, and multi-judge consensus. They're flexible, scalable, capture nuance, and handle open-ended tasks.

**Human graders** include SME review, crowdsourced judgment, spot-check sampling, A/B testing, and inter-annotator agreement. They provide gold standard quality and match expert user judgment.

### Capability vs. regression evals

**Capability or "quality" evals** ask, "What can this agent do well?" They should start at a low pass rate, targeting tasks the agent struggles with and giving teams a hill to climb.

**Regression evals** ask, "Does the agent still handle all the tasks it used to?" They should have a nearly 100% pass rate and protect against backsliding.

### Evaluating coding agents

Coding agents write, test, and debug code. Effective evals rely on well-specified tasks, stable test environments, and thorough tests for the generated code. Two widely used benchmarks are [SWE-bench Verified](https://www.swebench.com/SWE-bench/) and [Terminal-Bench](https://www.tbench.ai/).

### Evaluating conversational agents

Conversational agents interact with users in domains like support, sales, or coaching. Effective evals rely on verifiable end-state outcomes and rubrics that capture both task completion and interaction quality. Benchmarks include [𝜏-Bench](https://arxiv.org/abs/2406.12045) and [τ2-Bench](https://arxiv.org/abs/2506.07982).

### Evaluating research agents

Research agents synthesize information from many sources. Effective evals test whether agents find the right information, reason about it correctly, and produce accurate summaries. Evals can use question-answer pairs graded by string match or LLM rubrics, or more complex tasks graded by expert review.

### Evaluating computer use agents

Computer use agents interact with GUIs. Evals can verify screenshots, check application state, and confirm task completion. These evals are complex because they require full desktop environments.

## Building your first eval suite

We recommend starting simple and iterating:

1. Start with your most common failure mode and write 10-20 test cases
2. Use code-based graders where possible
3. Run evals on every change and track metrics over time
4. Add complexity as needed

## Conclusion

Evals are essential for building reliable AI agents. They help teams ship confidently, debug effectively, and improve continuously. Start simple, iterate often, and let evals compound in value over time.