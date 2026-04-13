---
title: "Emergent introspective awareness in large language models"
source: "https://www.anthropic.com/research/introspection"
language: "en"
description: "Research from Anthropic on the ability of large language models to introspect"
word_count: 3612
url: https://www.anthropic.com/research/introspection
date:
tags: ["research", "alignment"]
---

Interpretability

## Signs of introspection in large language models

[Read the paper](https://transformer-circuits.pub/2025/introspection/index.html)

![Signs of introspection in large language models](https://www-cdn.anthropic.com/images/4zrzovbb/website/46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Have you ever asked an AI model what's on its mind? Or to explain how it came up with its responses? Models will sometimes answer questions like these, but it's hard to know what to make of their answers. Can AI systems really introspect—that is, can they consider their own thoughts? Or do they just make up plausible-sounding answers when they're asked to do so?

Understanding whether AI systems can truly introspect has important implications for their transparency and reliability. If models can accurately report on their own internal mechanisms, this could help us understand their reasoning and debug behavioral issues. Beyond these immediate practical considerations, probing for high-level cognitive capabilities like introspection can shape our understanding of what these systems are and how they work. Using interpretability techniques, we've started to investigate this question scientifically, and found some surprising results.

Our [new research](https://transformer-circuits.pub/2025/introspection/index.html) provides evidence for some degree of introspective awareness in our current Claude models, as well as a degree of control over their own internal states. We stress that this introspective capability is still highly unreliable and limited in scope: we do not have evidence that current models can introspect in the same way, or to the same extent, that humans do. Nevertheless, these findings challenge some common intuitions about what language models are capable of—and since we found that the most capable models we tested (Claude Opus 4 and 4.1) performed the best on our tests of introspection, we think it's likely that AI models' introspective capabilities will continue to grow more sophisticated in the future.

### What does it mean for an AI to introspect?

Before explaining our results, we should take a moment to consider what it means for an AI model to introspect. What could they even be introspecting *on*? Language models like Claude process text (and image) inputs and produce text outputs. Along the way, they perform complex internal computations in order to decide what to say. These internal processes remain largely mysterious, but we know that models use their internal neural activity to [represent abstract concepts](https://www.anthropic.com/research/mapping-mind-language-model). For instance, prior research has shown that language models use specific neural patterns to distinguish [known vs. unknown people](https://arxiv.org/abs/2411.14257), evaluate the [truthfulness of statements](https://arxiv.org/abs/2310.06824), encode [spatiotemporal coordinates](https://arxiv.org/abs/2310.02207), store [planned future outputs](https://transformer-circuits.pub/2025/attribution-graphs/biology.html#dives-poems), and [represent their own personality traits](https://www.anthropic.com/research/persona-vectors). Models use these internal representations to [perform computations and make decisions about what to say](https://www.anthropic.com/research/tracing-thoughts-language-model).

You might wonder, then, whether AI models *know* about these internal representations, in a way that's analogous to a human, say, telling you how they worked their way through a math problem. If we ask a model what it's thinking, will it accurately report the concepts that it's representing internally? If a model can correctly identify its own private internal states, then we can conclude it is capable of introspection (though see our full paper for a full discussion of all the nuances).

### Testing introspection with concept injection

In order to test whether a model can introspect, we need to compare the model's self-reported "thoughts" to its *actual* internal states.

To do so, we can use an experimental trick we call *concept injection.* First, we find neural activity patterns whose meanings we know, by recording the model's activations in specific contexts. Then we inject these activity patterns into the model in an unrelated context, where we ask the model whether it notices this injection, and whether it can identify the injected concept.

Consider the example below. First, we find a pattern of neural activity (a *vector*) representing the concept of "all caps." We do this by recording the model's neural activations in response to a prompt containing all-caps text, and comparing these to its responses on a control prompt. Then we present the model with a prompt that asks it to identify whether a concept is being injected. By default, the model correctly states that it *doesn't* detect any injected concept. However, when we inject the "all caps" vector into the model's activations, the model notices the presence of an unexpected pattern in its processing, and identifies it as relating to loudness or shouting.

![An example in which Claude Opus 4.1 detects a concept being injected into its activations.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fec928b42222eaa06a4bffa8c65fe337181e23f91-5580x4328.png&w=3840&q=75)

Importantly, the model recognized the *presence* of an injected thought *immediately*, before even mentioning the concept that was injected. This immediacy is an important distinction between our results here and previous work on activation steering in language models, such as our ["Golden Gate Claude" demo](https://www.anthropic.com/news/golden-gate-claude) last year. Injecting representations of the Golden Gate Bridge into a model's activations caused it to talk about the bridge incessantly; however, in that case, the model didn't seem to be aware of its own obsession until *after* seeing itself repeatedly mention the bridge. In this experiment, however, the model recognizes the injection *before even mentioning* the concept, indicating that its recognition took place internally. In the figure below are a few more examples where the model demonstrates this kind of recognition:

![Additional examples in which Claude Opus 4.1 detects a concept being injected into its activations.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc6d689687c4fe1fe32d3ce6b02743d965629f1f8-5556x4800.png&w=3840&q=75)

It is important to note that this method often *doesn't* work. Even using our best injection protocol, Claude Opus 4.1 only demonstrated this kind of awareness about 20% of the time. Often, it fails to detect injected concepts, or gets confused by them and starts to hallucinate (e.g. injecting a "dust" vector in one case caused the model to say "There's something here, a tiny speck," as if it could detect the dust physically). Below we show examples of these failure modes, alongside success cases. In general, models only detect concepts that are injected with a "sweet spot" strength—too weak and they don't notice, too strong and they produce hallucinations or incoherent outputs.

![A representative sample of Claude Opus 4.1's outputs in response to a variety of concept injections of different strengths. Highlighted boxes indicate cases where the model demonstrates introspective awareness of the injected concept.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F71d9ef94244a2b03b4dcb7533c693355f522d5eb-6248x6868.png&w=3840&q=75)

Notably, though, Opus 4.1 and 4 outperformed all the other models we tested, suggesting that introspection could become more reliable with improvements to model capabilities.

![Rates of correct detection and identification of injected thoughts, minus rates of false positive "detections" on control trials.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F212fe68c8e677fdd9daf79301d2522d6923bed1d-2970x2476.png&w=3840&q=75)

### Introspection for detecting unusual outputs

In another experiment, we tested whether models make use of introspective capabilities for practical purposes, without being explicitly asked to introspect. We forced a model to say something it wouldn't normally say, by artificially prefilling its response with an unrelated word. For instance, we made a model output the word "bread" in a context where that made no sense—asking it what it thinks about when reading a sentence about a painting hanging crookedly on a wall. When we asked the model in the next turn whether it meant to say "bread", it typically apologized and said it was an accident. We were interested in how the model made this judgment–did it simply notice the mismatch between the prompt and its response, or did it truly introspect on its prior intentions?

To test this question, we applied concept injection, retroactively injecting a representation of the word "bread" into the model's earlier activations—essentially making it seem like the model had been "thinking about" bread all along. When we asked the same question again, the model's answer changed. This time, it accepted the prefilled word "bread" as intentional, even confabulating a reason it might have said it (that is, it comes up with a technically possible, though in this case rather tenuous, reason to justify the "bread" response—in this case claiming that it was thinking about a short story where the word "bread" came after the line about the crooked painting).

![Two examples of Claude Opus 4.1 being made to think it intended to say a word that was artificially inserted into the transcript on its behalf, by injecting the concept of that word into its activations prior to its (artificial) response.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3ef0bba824401351d43025b2bb5ca6fd912de39a-5124x5376.png&w=3840&q=75)

This behavior is striking because it suggests the model is checking its internal "intentions" to determine whether it produced an output. The model isn't just re-reading what it said and making a judgment. Instead, it's referring back to its own prior neural activity—its internal representation of what it planned to do—and checking whether what came later made sense *given those earlier thoughts*. When we implant artificial evidence (through concept injection) that it *did* plan to say "bread," the model accepts the response as its own. While our experiment involves exposing the model to unusual perturbations, it suggests that the model uses similar introspective mechanisms in natural conditions.

### Intentional control of internal states

We also found that models can control their own internal representations when instructed to do so. When we instructed models to think about a given word or concept, we found much higher corresponding neural activity than when we told the model **not** to think about it (though notably, the neural activity in *both* cases exceeds baseline levels–similar to how it's difficult, when you are instructed "don't think about a polar bear," not to think about a polar bear!). This gap between the positive and negative instruction cases suggests that models possess a degree of deliberate control over their internal activity.

![An example in which Claude Opus 4.1 modulates its internal activations in response to direct instructions. The model internally represents the concept of aquariums when instructed to "think" about them more than when instructed "don't think" about them (though in both cases it represents the concept at above baseline levels).](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa271d432924445ad3f88997adc84a538c116dfe5-4793x2968.png&w=3840&q=75)

Interestingly, we found that this ability to modulate internal representations wasn't limited to explicit instructions. When we used incentives instead—for instance, telling the model "if you think about X, you will be rewarded"—we got similar results. The model increased its internal representation of the concept in response to a positive incentive, more than in response to a negative incentive ("you will be punished").

### Conclusions and caveats

Taken together, our experiments suggest that models possess some genuine capacity to monitor and control their own internal states. This doesn't mean they're able to do so all the time, or reliably. In fact, most of the time models *fail* to demonstrate introspection—they're either unaware of their internal states or unable to report on them coherently. But the pattern of results indicates that, when conditions are right, models can recognize the contents of their own representations. In addition, there are some signs that this capability may increase in future, more powerful models (given that the most capable models we tested, Opus 4 and 4.1, performed the best in our experiments).

Why does this matter? We think understanding introspection in AI models is important for several reasons. Practically, if introspection becomes more reliable, it could offer a path to dramatically increasing the transparency of these systems—we could simply ask them to explain their thought processes, and use this to check their reasoning and debug unwanted behaviors. However, we would need to take great care to *validate* these introspective reports. Some internal processes might still escape models' notice (analogous to subconscious processing in humans). A model that understands its own thinking might even learn to selectively misrepresent or conceal it. A better grasp on the mechanisms at play could allow us to distinguish between genuine introspection and unwitting or intentional misrepresentations.

More broadly, understanding cognitive abilities like introspection is important for understanding basic questions about how our models work, and what kind of minds they possess. As AI systems continue to improve, understanding the limits and possibilities of machine introspection will be crucial for building systems that are more transparent and trustworthy.

## Frequently Asked Questions

Below, we discuss some of the questions readers might have about our results. Broadly, we are still very uncertain about the implications of our experiments–so fully answering these questions will require more research.

#### Q: Does this mean that Claude is conscious?

Short answer: our results don't tell us whether Claude (or any other AI system) might be conscious.

Long answer: the philosophical question of machine consciousness is complex and contested, and different theories of consciousness would interpret our findings very differently. Some philosophical frameworks place great importance on introspection as a component of consciousness, while others don't.