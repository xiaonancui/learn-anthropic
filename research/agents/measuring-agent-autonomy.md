---
title: "Measuring AI agent autonomy in practice"
url: https://www.anthropic.com/research/measuring-agent-autonomy
date:
tags: ["research", "agents"]
source: "https://www.anthropic.com/research/measuring-agent-autonomy"
language: "en"
description: "Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems."
word_count: 5912
---

AI agents are here, and already they're being deployed across contexts that vary widely in consequence, from email triage to [cyber espionage](https://www.anthropic.com/news/disrupting-AI-espionage). Understanding this spectrum is critical for deploying AI safely, yet we know surprisingly little about how people actually use agents in the real world.

We analyzed millions of human-agent interactions across both Claude Code and our public API using our [privacy-preserving tool](https://www.anthropic.com/research/clio), to ask: How much autonomy do people grant agents? How does that change as people gain experience? Which domains are agents operating in? And are the actions taken by agents risky?

We found that:

- [**Claude Code is working autonomously for longer.**](https://anthropic.com/research/measuring-agent-autonomy#claude-code-is-working-autonomously-for-longer) Among the longest-running sessions, the length of time Claude Code works before stopping has nearly doubled in three months, from under 25 minutes to over 45 minutes. This increase is smooth across model releases, which suggests it isn't purely a result of increased capabilities, and that existing models are capable of more autonomy than they exercise in practice.
- [**Experienced users in Claude Code auto-approve more frequently, but interrupt more often.**](https://www.anthropic.com/research/measuring-agent-autonomy#experienced-users-in-claude-code-auto-approve-more-frequently-but-interrupt-more-often) As users gain experience with Claude Code, they tend to stop reviewing each action and instead let Claude run autonomously, intervening only when needed. Among new users, roughly 20% of sessions use full auto-approve, which increases to over 40% as users gain experience.
- [**Claude Code pauses for clarification more often than humans interrupt it.**](https://www.anthropic.com/research/measuring-agent-autonomy#claude-code-pauses-for-clarification-more-often-than-humans-interrupt-it) In addition to human-initiated stops, *agent* -initiated stops are also an important form of oversight in deployed systems. On the most complex tasks, Claude Code stops to ask for clarification more than twice as often as humans interrupt it.
- **[Agents are used in risky domains, but not yet at scale.](https://anthropic.com/research/measuring-agent-autonomy#agents-are-used-in-risky-domains-but-not-yet-at-scale)** Most agent actions on our public API are low-risk and reversible. Software engineering accounted for nearly 50% of agentic activity, but we saw emerging usage in healthcare, finance, and cybersecurity.

Below, we present our methodology and findings in more detail, and end with recommendations for model developers, product developers, and policymakers. Our central conclusion is that effective oversight of agents will require new forms of post-deployment monitoring infrastructure *and* new human-AI interaction paradigms that help both the human and the AI manage autonomy and risk together.

We view our research as a small but important first step towards empirically understanding how people deploy and use agents. We will continue to iterate on our methods and communicate our findings as agents are adopted more widely.

## Studying agents in the wild

Agents are difficult to study empirically. First, there is no agreed-upon definition of what an agent *is.* Second, agents are evolving quickly. Last year, many of the most sophisticated agents—including Claude Code—involved a single conversational thread, but today there are multi-agent systems that operate autonomously for hours. Finally, model providers have limited visibility into the architecture of their customers' agents. For example, we have no reliable way to associate independent requests to our API into "sessions" of agentic activity. (We discuss this challenge in more detail at the end of this post.)

In light of these challenges, how can we study agents empirically?

To start, for this study we adopted a definition of agents that is conceptually grounded and operationalizable: *an agent is an AI system equipped with tools that allow it to take actions*, like running code, calling external APIs, and sending messages to other agents.<sup>1</sup> Studying the tools that agents use tells us a great deal about what they are doing in the world.

Next, we developed a collection of metrics that draw on data from both agentic uses of our [public API](https://platform.claude.com/docs/en/api/overview) and [Claude Code](https://code.claude.com/docs/en/overview), our own coding agent. These offer a tradeoff between breadth and depth:

- Our **public API** gives us broad visibility into agentic deployments across thousands of different customers. Rather than attempting to infer our customers' agent architectures, we instead perform our analysis at the level of *individual tool calls*.<sup>2</sup> This simplifying assumption allows us to make grounded, consistent observations about real-world agents, even as the contexts in which those agents are deployed vary significantly. The limitation of this approach is that we must analyze actions in isolation, and cannot reconstruct how individual actions compose into longer sequences of behavior over time.
- **Claude Code** offers the opposite tradeoff. Because Claude Code is our own product, we can link requests across sessions and understand entire agent workflows from start to finish. This makes Claude Code especially useful for studying autonomy—for example, how long agents run without human intervention, what triggers interruptions, and how users maintain oversight over Claude as they develop experience. However, because Claude Code is only one product, it does not provide the same diversity of insight into agentic use as API traffic.

By drawing from both sources using our [privacy-preserving infrastructure](https://www.anthropic.com/research/clio), we can answer questions that neither could address alone.

## Claude Code is working autonomously for longer

How long do agents actually run without human involvement? In Claude Code, we can measure this directly by tracking how much time has elapsed between when Claude starts working and when it stops (because it finished the task, asked a question, or was interrupted by the user) on a turn-by-turn basis.<sup>3</sup>

Turn duration is an imperfect proxy for autonomy.<sup>4</sup> For example, more capable models could accomplish the same work faster, and subagents allow more work to happen at once, both of which push towards shorter turns.<sup>5</sup> At the same time, users may be attempting more ambitious tasks over time, which would push towards longer turns. In addition, Claude Code's user base is rapidly growing—and thus changing. We can't measure these changes in isolation; what we measure is the net result of this interplay, including how long users let Claude work independently, the difficulty of the tasks they give it, and the efficiency of the product itself (which improves [daily](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)).

Most Claude Code turns are short. The median turn lasts around 45 seconds, and this duration has fluctuated only slightly over the past few months (between 40 and 55 seconds). In fact, nearly every percentile below the 99th has remained relatively stable.<sup>6</sup> That stability is what we'd expect for a product experiencing rapid growth: when new users adopt Claude Code, they are comparatively inexperienced, and—as we show in the next section—less likely to grant Claude full latitude.

The more revealing signal is in the tail. The longest turns tell us the most about the most ambitious uses of Claude Code, and point to where autonomy is heading. Between October 2025 and January 2026, the 99.9th percentile turn duration nearly doubled, from under 25 minutes to over 45 minutes (Figure 1).

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa86a9559ec987a33340c265265463843846ad8c7-3840x2160.png&w=3840&q=75)

Figure 1. 99.9th percentile turn duration (how long Claude works on a per-turn basis) in interactive Claude Code sessions, 7-day rolling average. The 99.9th percentile has grown steadily from under 25 minutes in late September to over 45 minutes in early January. This analysis reflects all interactive Claude Code usage.


Notably, this increase is smooth across model releases. If autonomy were purely a function of model capability, we would expect sharp jumps with each new launch. The relative steadiness of this trend instead suggests several potential factors are at work, including power users building trust with the tool over time, applying Claude to increasingly ambitious tasks, and the product itself improving.

The extreme turn duration has declined somewhat since mid-January. We hypothesize a few reasons why. First, the Claude Code user base [doubled](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) between January and mid-February, and a larger and more diverse population of sessions could reshape the distribution. Second, as users returned from the holiday break, the projects they brought to Claude Code may have shifted from hobby projects to more tightly circumscribed work tasks. Most likely, it's a combination of these factors and others we haven't identified.

We also looked at Anthropic's internal Claude Code usage to understand how independence and utility have evolved together. From August to December, Claude Code's success rate on internal users' most challenging tasks doubled, at the same time that the average number of human interventions per session decreased from 5.4 to 3.3.<sup>7</sup> Users are granting Claude more autonomy and, at least internally, achieving better outcomes while needing to intervene less often.

Both measurements point to a significant deployment overhang, where the autonomy models are capable of handling exceeds what they exercise in practice.

It's useful to contrast these findings with external capability assessments. One of the most widely cited capability assessments is METR's "Measuring AI Ability to Complete Long Tasks," which [estimates](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) that Claude Opus 4.5 can complete tasks with a 50% success rate that would take a human nearly 5 *hours*. The 99.9th percentile turn duration in Claude Code, in contrast, is ~42 minutes, and the median is much shorter. However, the two metrics are not directly comparable. The METR evaluation captures what a model is capable of in an idealized setting with no human interaction and no real-world consequences. Our measurements capture what happens in practice, where Claude pauses to ask for feedback and users interrupt.<sup>8</sup> And METR's five-hour figure measures task difficulty—how long the task would take a human—not how long the model actually runs.

Neither capability evaluations nor our measurements alone give a complete picture of agent autonomy, but together they suggest that the latitude granted to models in practice lags behind what they can handle.

## Experienced users in Claude Code auto-approve more frequently, but interrupt more often

How do humans adapt how they work with agents over time? We found that people grant Claude Code more autonomy as they gain experience using it (Figure 2). Newer users (<50 sessions) employ full auto-approve roughly 20% of the time; by 750 sessions, this increases to over 40% of sessions.

This shift is gradual, suggesting a steady accumulation of trust. It's also important to note that Claude Code's default settings require users to manually approve each action, so part of this transition may reflect users configuring the product to match their preferences for greater independence as they become familiar with Claude's capabilities.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff1e687f19e4e87590b73dd9fa1cf5726184d7209-3840x2160.png&w=3840&q=75)

Figure 2. Auto-approve rate by account tenure. Experienced users increasingly let Claude run without any manual approval. Data reflects all interactive Claude Code usage for users who signed up after September 19, 2025. Line and CI bounds are LOWESS-smoothed (0.15 bandwidth). The x-axis is a log scale.

Approving actions is only one method of supervising Claude Code. Users can also interrupt Claude while it is working to provide feedback. We find that interrupt rates increase with experience. New users (those with around 10 sessions) interrupt Claude in 5% of turns, while more experienced users interrupt in around 9% of turns (Figure 3).

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fabcddadbbdc63751449a6a7fc5731a693c9654bb-3840x2160.png&w=3840&q=75)

Figure 3. Interrupt rates by account tenure on a turn-by-turn basis. Experienced users interrupt Claude more often, not less. Data reflects all interactive Claude Code usage for users who signed up after September 19, 2025. Shaded region shows 95% Wilson score confidence interval. Line and CI bounds are LOWESS-smoothed (0.15 bandwidth). The x-axis is a log scale.

Both interruptions *and* auto-approvals increase with experience. This apparent contradiction reflects a shift in users' oversight strategy. New users are more likely to approve each action before it's taken, and therefore rarely need to interrupt Claude mid-execution. Experienced users are more likely to let Claude work autonomously, stepping in when something goes wrong or needs redirection. The higher interrupt rate may also reflect active monitoring by users who have more honed instincts for when their intervention is needed. We expect the per-turn interrupt rate to eventually plateau as users settle into a stable oversight style, and indeed the curve may already be flattening among the most experienced users (though widening confidence intervals at higher session counts make this difficult to confirm).<sup>9</sup>

We saw a similar pattern on our public API: 87% of tool calls on minimal-complexity tasks (like editing a line of code) have some form of human involvement, compared to only 67% of tool calls for high-complexity tasks (like [autonomously finding zero-day exploits](https://red.anthropic.com/2026/zero-days/) or [writing a compiler](https://www.anthropic.com/engineering/building-c-compiler)).<sup>10</sup> This may seem counterintuitive, but there are two likely explanations. First, step-by-step approval becomes less practical as the number of steps grows, so it is structurally harder to supervise each action on complex tasks. Second, our Claude Code data suggests that experienced users tend to grant the tool more independence, and complex tasks may disproportionately come from experienced users. While we cannot directly measure user tenure on our public API, the overall pattern is consistent with what we observe in Claude Code.

Taken together, these findings suggest that experienced users aren't necessarily abnegating oversight. The fact that interrupt rates increase with experience alongside auto-approvals indicates some form of active monitoring. This reinforces a point we have made [previously](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents): effective oversight doesn't require approving every action but being in a position to intervene when it matters.

## Claude Code pauses for clarification more often than humans interrupt it

Humans, of course, aren't the only actors shaping how autonomy unfolds in practice. Claude is an active participant too, stopping to ask for clarification when it's unsure how to proceed. We found that as task complexity increases, Claude Code asks for clarification more often—and more frequently than humans choose to interrupt it (Figure 4).