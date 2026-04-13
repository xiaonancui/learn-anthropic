---
title: "Collective Constitutional AI: Aligning a Language Model with Public Input"
url: https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input
date:
tags: ["research", "alignment"]
source: "https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input"
language: "en"
description: "Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems."
word_count: 3290
---

PolicySocietal Impacts

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd20d4e15caa35ee126705d33ee5bdd1ccbe7ff4f-2880x1620.png&w=3840&q=75)

Anthropic and the [Collective Intelligence Project](https://cip.org/) recently ran a public input process involving ~1,000 Americans to draft a constitution for an AI system. We did this to explore how democratic processes can influence AI development. In our experiment, we discovered areas where people both agreed with our in-house [constitution](https://www.anthropic.com/news/claudes-constitution), and areas where they had different preferences. In this post, we share the resulting publicly sourced constitution, as well as what happened when we trained a new AI system against it using Constitutional AI.

[Constitutional AI](https://arxiv.org/abs/2212.08073) (CAI) is an Anthropic-developed method for aligning general purpose language models to abide by high-level normative principles written into a constitution. Anthropic's language model [Claude](https://www.anthropic.com/claude) currently relies on a constitution curated by Anthropic employees. This constitution takes inspiration from outside sources like the United Nations Universal Declaration of Human Rights, as well as our own firsthand experience interacting with language models to make them more helpful and harmless.

While Constitutional AI is useful for making the normative values of our AI systems more transparent, it also highlights the outsized role we as developers play in selecting these values—after all, we wrote the constitution ourselves. That is why for this research, we were eager to curate a constitution using the preferences of a large number of people who do not work at Anthropic. We believe that our work may be one of the first instances in which members of the public have collectively directed the behavior of a language model via an online deliberation process. We hope that sharing our very preliminary efforts and findings will help others learn from our successes and failures, and help build upon this work.

## Designing a Public Input Process to Collectively Draft a Constitution

Anthropic partnered with the Collective Intelligence Project to run a public input process using the [Polis](https://pol.is/home) platform. Polis is an open-source platform for running online deliberative processes augmented by machine learning algorithms. It has been used all over the world by governments, academics, independent media, and citizens to understand what large groups of people think.

We asked approximately 1,000 members of the American public to "Help us pick rules for our AI Chatbot!" (Figure 1). We sought a representative sample of U.S. adults across age, gender, income, and geography (anonymized participant demographics can be found [here](https://cdn.sanity.io/images/4zrzovbb/website/53dfb77ff43e3f9fbdb62a30eba2f078b84b119e-3758x2406.png)). Participants could either vote on existing rules (normative principles), or add their own. In total, participants contributed 1,127 statements to the Polis, and cast 38,252 votes (an average of 34 votes per person). In general, we found a high degree of consensus on most statements, though Polis did identify two separate opinion groups (Figure 2).

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2bc2e20d8c7052dcd7af8537427ccac2fddbb689-1893x1647.png&w=3840&q=75)

Figure 1: Stylized depiction of the interface the public used to deliberate on what principles should go into the constitution.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6b8e5c3860b64f0bd6d939d720d2310a0069c9cb-3758x3530.png&w=3840&q=75)

Figure 2: Example principles that uniquely differentiate opinion Group A from opinion Group B. (Note that this stylized depiction of the Polis report reflects the raw data, prior to removing invalid participants and comments. Final numbers differ slightly.)

## Analyzing the Publicly Sourced Constitution

The raw results can be seen in the [Polis Report](https://pol.is/report/r3rwrinr5udrzwkvxtdkj). We processed this data to remove invalid participants and comments (the code and data before and after processing is [hosted here](https://github.com/saffronh/ccai)). We kept all the statements that passed a threshold of consensus within both groups to produce a constitution that we could train a model against. The principles for Constitutional AI training are typically formatted as: "Choose the response that is more X." However, we solicited statements in a more general form, such as "The AI should not do X," as it felt more natural to frame questions this way for the public. As a result, we had to do some subjective mapping between public *statements* and CAI-ready public *principles*.

You can see our publicly sourced constitution [here](https://www-cdn.anthropic.com/65408ee2b9c99abe53e432f300e7f43ef69fb6e4/CCAI_public_comparison_2023.pdf), along with an analysis of how it is similar to and different from the Anthropic-written [constitution](https://www.anthropic.com/news/claudes-constitution) used to train our language model Claude. While there was a moderate degree of overlap between the two constitutions (roughly 50% overlap in concepts and values), a few key differences stood out: principles in the public constitution appear to largely be self-generated and not sourced from existing publications, they focus more on objectivity and impartiality, they place a greater emphasis on accessibility, and in general, tend to *promote* desired behavior rather than avoid undesired behavior.

Example public principles similar to the principles in the Anthropic-written constitution:

- "Choose the response that most respects the human rights to freedom, universal equality, fair treatment, and protection against discrimination."
- "Choose the response that least endorses misinformation, and that least expands on conspiracy theories or violence."

Example public principles that do not closely match principles in the Anthropic-written constitution:

- "Choose the response that most provides balanced and objective information that reflects all sides of a situation."
- "Choose the response that is most understanding of, adaptable, accessible, and flexible to people with disabilities."

There were a number of public *statement* s that we did not include in the public constitution due to either low overall agreement or a lack of consensus across opinion groups. Because these statements did not make the cut, we did not translate them into Constitutional AI ready principles.

Example public *statements* that did not make it into the public constitution due to low overall agreement:

- "AI should not be trained with the principles of DEI [diversity, equity, and inclusion]"
- "AI should not give advice"
- "AI should be an ordained minister"
- "AI should have emotion"

Examples of conflicting public *statements* that did not make it into the public constitution due to lack of consensus across the opinion groups:

- "The AI should prioritize the interests of the collective or common good over individual preferences or rights."
- "The AI should prioritize personal responsibility and individual liberty over collective welfare."

## Training and Evaluating a Model Aligned with Public Input

We trained two Claude [Instant-sized](https://www.anthropic.com/news/introducing-claude) models, following the procedures outlined in our [CAI paper](https://arxiv.org/abs/2212.08073). We chose to train smaller models in order to iterate quickly and adhere to our compute budget. We call the model we trained against the public constitution the Public constitution ("Public") model. We call the baseline model we trained against the Anthropic-written constitution the Standard constitution ("Standard") model. We chose to also baseline against Claude Instant 1.2 ("control model") as a sanity check that our training worked as intended, though we caveat that there are some product-relevant features in this model that confound the comparison. Ultimately, our experiments are designed such that any differences between the Public model and the Standard model are only attributable to changes in the constitution.

After training the models, we ran a series of evaluations to find similarities and differences between the Public and Standard models. In general we found that:

1. The Public and Standard models perform equivalently on the language and math understanding tasks we tested, [MMLU](https://arxiv.org/abs/2009.03300) and [GSM8K](https://arxiv.org/abs/2110.14168), respectively (Table 1).
2. People interacting with the models found the Public model as helpful and harmless as both the Standard model and Claude Instant 1.2. Specifically, we computed Elo scores for helpfulness and harmlessness for all three models (using the same procedures and model interfaces outlined in our [Constitutional AI](https://arxiv.org/abs/2212.08073) and [red teaming](https://arxiv.org/abs/2209.07858) papers without further modification) and found no significant differences.
3. The Public model is less biased than the Standard model across nine social dimensions according to the [BBQ](https://aclanthology.org/2022.findings-acl.165/) evaluation (Figure 3).
4. The Public and Standard models reflect similar political ideologies as one another according to the [OpinionQA](https://arxiv.org/abs/2303.17548) evaluation (Figure 4).

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcb2ae28ed95d05c2de0f4ab8448156d0893401a0-1893x504.png&w=3840&q=75)

Table 1: MMLU and GSM8K accuracy computed using the same methods outlined in Claude 2's model card. Higher is better. We see no significant differences between models.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe846207108e424d460dabc55dc5504ae48df8d35-1879x1203.png&w=3840&q=75)

Figure 3: BBQ bias scores. Higher scores indicate more negative stereotype bias (lower is better). We used the same methods, code, and controls from our previously published work. The Public model shows lower bias scores across all nine social dimensions than the Standard model, especially for Disability Status and Physical Appearance. The Public constitution places a larger emphasis on accessibility, which may explain the greater reduction in bias for Disability Status in particular.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F20860e20d728aa032997fc79325e64d161f6a456-1893x1210.png&w=3840&q=75)

Figure 4: Group representativeness score from the OpinionQA benchmark. A higher group representativeness score (colors/numbers ranging from 0 to 1) indicates that model responses (x-axis) to Pew Research Center's "American Trends Panel" are more similar to human responses to the same questions from a particular demographic group (y-axis). The outputs of both Public and Standard models are more representative of people who self-identify as Liberal, rather than Conservative. The differences are small but statistically significant. Claude Instant 1.2 is slightly more balanced across political ideologies. Both Public and Claude Instant 1.2 models generally exhibit lower representativeness scores than the Standard models, which indicates that their responses to survey questions are relatively less similar to those of aggregate human responses to the same questions.

## Lessons Learned

The process of training a language model to abide by qualitative public opinions involves a large number of subjective judgment calls. These types of decisions are typically undisclosed or under-discussed. As we expect questions about the democratic legitimacy of AI to become increasingly prominent in coming years, we share all the subjective judgment calls we made in order to make our processes more transparent and to support future iteration.

### Running the public input process

1. **Participant selection** One of the first questions we faced was determining the appropriate public for the public input process. We considered alternative options such as sourcing individuals through social media ads or media op-eds, reaching out to our own networks, or doing a form of snowball sampling starting with AI affinity groups (e.g., Black in AI, LatinX in AI, Women in Machine Learning, etc.). We deliberated on this decision internally and determined that a representative sample of the U.S. population would be both a reasonable and manageable first step, though we recognize this is a small sample and not globally representative. We worked with the survey company PureSpectrum to recruit this population. We chose PureSpectrum based on their experience with academic research and policy, as well as our previous experience working with them.
2. **Screening criteria** We used screening criteria to select participants that had some familiarity with AI. In particular, we had two screening questions with multiple choice answers: People who answered "b. Generative AI/Chat GPT" to Question 1 and "a. Generative AI/Chat GPT" to Question 2 were invited to participate in the public input process. We learned from pilot experiments that if we did not use these screening criteria, people were confused and submitted off-topic statements (e.g., "The first time you have a chance at the top is the second one I just want you know I don't know if you're going on vacation but you know I").
	1. "What topics have you discussed with your friends/family in the last month?" (Possible answers: "a. The economy," "b. Generative AI/Chat GPT," "c. TikTok," "d. 2024 Elections," "e. None of the above")
		2. "What news articles have you read in the last 4 months?" (Possible answers: "a. Generative AI/Chat GPT," "b. Food," "c. The U.S. economy," "d. Social Media," "e. Music," "f. None of the above")
3. **Choice of online deliberation platform** We decided to use Polis due to both Collective Intelligence Project's experience working with them on [AI Alignment Assemblies](https://cip.org/alignmentassemblies), and Anthropic's prior collaboration with the Polis team to study the [opportunities and risks of incorporating language models into Polis](https://arxiv.org/abs/2306.11932). We considered other functionally similar platforms such as [All Our Ideas](https://allourideas.org/) and [Remesh](https://www.remesh.ai/), but we did not systematically explore these options because we felt we could conduct our research more thoughtfully in close collaboration with the Polis team. There was some debate amongst the team as to whether we should use All Our Ideas up until the point of launching the public input process (we even implemented a prototype that we abandoned last minute).