---
title: "Introducing Anthropic Interviewer"
source: "https://www.anthropic.com/research/anthropic-interviewer"
language: "en"
description: "What 1,250 professionals told us about working with AI"
word_count: 5946
url: https://www.anthropic.com/research/anthropic-interviewer
date:
tags: ["research", "evals"]
---

Societal Impacts

## Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI

![Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI ](https://www-cdn.anthropic.com/images/4zrzovbb/website/710b64c2542329ce05316098b4e405bb1c11e4d4-1000x1000.svg)

*We're launching a new tool, Anthropic Interviewer, to help understand people's perspectives on AI. In this research post, we introduce the tool, describe a test of it on a sample of professionals, and discuss our early findings. We also discuss future work in this direction that we can now explore with the development of this tool and through partnerships with creatives, scientists, and teachers.*

## Introduction

Millions of people now use AI every day. As a company developing AI systems, we want to know how and why they're doing so, and how it affects them. In part, this is because we want to use people's feedback to develop better products—but it's also because understanding people's interactions with AI is one of the great sociological questions of our time.

We recently designed [a tool](https://www.anthropic.com/research/clio) to investigate patterns of AI use while protecting our users' privacy. It enabled us to analyze changing patterns of AI use [across the economy](https://www.anthropic.com/economic-index). But the tool only allowed us to understand what was happening within conversations with Claude. What about what comes afterwards? How are people actually *using* Claude's outputs? How do they feel about it? What do they imagine the role of AI to be in their future? If we want a comprehensive picture of AI's changing role in people's lives, and to center humans in the development of models, we need to *ask people directly*.

Such a project would require us to run many hundreds of interviews. Here, we enlisted AI to help us do so. We built an interview tool called Anthropic Interviewer. Powered by Claude, Anthropic Interviewer runs detailed interviews automatically at unprecedented scale, feeding its results back to human researchers for analysis. This is a new step in understanding the wants and needs of our users, as well as gathering data for the analysis of AI's societal and economic impacts.

To test Anthropic Interviewer, we had it run 1,250 interviews with professionals—the general workforce (N=1,000), scientists (N=125), and creatives (N=125)—about their views on AI. We're [publicly releasing](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer) all interview data from this initial test (with participant consent) for researchers to explore; we provide our own analysis below. Briefly, here are some examples of what we found:

- **In our sample, people are optimistic about the role AI plays in their work.** Positive sentiments characterized the majority of topics discussed. However, a small number of topics such as educational integration, artist displacement, and security concerns, came with more pessimistic outlooks.
- **People from the general workforce want to preserve tasks that define their professional identity while delegating routine work to AI.** They envision futures where routine tasks are automated and their role shifts to overseeing AI systems.
- **Creatives are using AI to increase their productivity despite peer judgement and anxiety about the future.** They are navigating both the immediate stigma of AI use in creative communities and deeper concerns about economic displacement and the erosion of human creative identity.
- **Scientists want AI partnership but can't yet trust it for core research.** Scientists uniformly expressed a desire for AI that could generate hypotheses and design experiments. But at present, they confined their actual use to other tasks like writing manuscripts or debugging analysis code.

![The different topics people discussed in their interviews with Anthropic Interviewer.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4ae319f2a488d12756eb79f9f0d4e4899bf8bcfe-2880x1950.jpg&w=3840&q=75)

The different topics people discussed in their interviews with Anthropic Interviewer. Across all three samples we studied—the general workforce, scientists, and creatives—participants expressed predominantly positive sentiments about AI's impact on their professional activities. Certain topics did introduce pause, particularly around questions of personal control, job displacement, and autonomy. In this diagram, topics are roughly ordered from more pessimistic to more optimistic.

**General workforce**

| Pessimistic | Optimistic |
| --- | --- |
| **Career adaptation.** Trucking dispatcher: "I'm always trying to figure out things that humans offer to the industry that can't be automated and really hone in on that aspect like the personalized human interactions. However, that is not something that I think will be necessary in the long run. I'm still trying to figure out what skills would be good to work on that AI can't 'take over.'" | **Societal perspectives**. Office assistant: "It's a tool to me like a computer was, or a type writer was in the day—computers didn't get rid of mathematicians, they just made them able to do more and that is where I see AI going in the best possible future." |
| **Writing independence.** Salesperson: "I hear from colleagues that they can tell when email correspondence is AI generated and they have a slightly negative regard for the sender. They feel slighted that the sender is 'too lazy' to send them a personal note and push it onto AI to do it." | **Educational integration.** Special education teacher: "I am hoping that AI will be a more collaborative partner that will help me better manage my time and help me expand creatively so I can offer my students a wide variety of activities and assignments that I may not have been able to come up with on my own." |

Example quotations from professionals in the general workforce, organized by topic. This research aims to both unpack the optimism and navigate the underlying anxieties to better understand how AI is actually reshaping work across different professional contexts.

**Creatives**

| Pessimistic | Optimistic |
| --- | --- |
| **Control boundaries.** Gamebook writer: "During these storytelling sessions, I would say that there's only the illusion of collaboration for the most part… there's rarely a point where I've really felt like the AI is driving the creative decision-making." | **Workflow automation.** Social media manager: "I'm less stressed, honestly. It has created a ton of efficiency for me so I can focus on my favorite aspects of the job (filming and editing)". |
| **Writer displacement.** Creative fiction writer: "A novel written by AI might have a great plot and be technically brilliant. But it won't have the deeper nuances that only a human can weave throughout the story." | **Music production.** Music producer: "Sometimes, when it comes time to add lyrics, I'll ask ChatGPT or Claude for lists of interesting word pairings. Just getting a long list to try out over the instrumental often leads to finding a hook or at least a seed for a song idea." |

Example quotations from creatives, organized by topic.

**Scientists**

| Pessimistic | Optimistic |
| --- | --- |
| **Security concerns.** Medical scientist: "Our confidence in AI just isn't high enough at the moment to trust it with our data. We're also a commercial entity so there's a bit of concern over confidentially with data that we might share with an AI system." | **Research assistance.** Molecular biologist: "If AI could integrate and normalize all this data in a single repository, it could be a very exciting thing for biological discovery. You could see how expression dynamics change across cell models, tissue types, disease states, and more." |
| **Content verification.** Economist: "What I would really like from an AI would be the ability to accurately grab information, summarise it and use it to write the core of a funding application. AI generally writes well; the problem now is that I just can't rely on it not hallucinating, or to put it bluntly, lying." | **Code development.** Food scientist: "Honestly I wouldn't have known how to help my student with her code if something was off without AI tools." |

Example quotations from scientists, organized by topic.

## Method

This initial test explored how workers integrate AI into their professional practice and how they feel about its role in their future. We ran interviews to produce qualitative data, and supplemented them with quantitative data from surveys where participants answered questions on their behavioral and occupational backgrounds. We also had [a separate AI analysis tool](https://www.anthropic.com/research/clio) read the interview transcripts and cluster together emergent, overarching themes from the unstructured data—for example, on the percentage of participants who mentioned a specific topic or expressed a specific view in their interview.

### Participants

We used Anthropic Interviewer to conduct interviews with 1,250 professionals. We intend for the tool to interview general [Claude.ai](http://claude.ai/redirect/website.v1.ae8e2433-ce9e-48a0-b609-5dc2ec208fe5) users, but for this initial test, we sought participants working across a range of professions and engaged them through crowdworker platforms (all participants had an occupation other than crowdworking that was their main job).

1,000 of our participants were recruited from a general sample of occupations (that is, we did not select participants from specific jobs). Of that group, the largest subgroups came from educational instruction (17%), computer and mathematical occupations (16%), and arts, design, entertainment, and media (14%).

We also recruited two specialist samples of 125 participants each. The first was from creative professions: predominantly writers and authors (48% of the sample), and visual artists (21%), with smaller groups of filmmakers, designers, musicians, and craft workers. The second was from science, which included physicists (9%), chemists (9%), chemical engineers (7%), and data scientists (6%), with representation across 50+ other distinct scientific disciplines.

We chose to add these two specialist subgroups because these represent professional domains where AI's role remains contested and is rapidly evolving. We hypothesized that creatives and scientists would reveal distinct patterns of AI adoption and professional concerns.

All participants provided informed consent for us to analyze their interview data for research purposes and for us to release the transcripts publicly.

### How Anthropic Interviewer works

Anthropic Interviewer operates in three stages: planning, interviewing, and analysis. Below, we describe each of them in turn.

![The three stages of Anthropic Interviewer's process.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcc1e5916d47f4217a6952c410db3ab118f5d2221-6624x2756.png&w=3840&q=75)

The three stages of Anthropic Interviewer's process.

#### Planning

In this phase, Anthropic Interviewer creates an interview rubric that allows it to focus on the same overall research questions across hundreds or thousands of interviews, but which is still flexible enough to accommodate variations and tangents that might occur in individual interviews.

We developed a system prompt—a set of overall instructions for how the AI model is to work—to give Anthropic Interviewer its methodology. This was where we included hypotheses regarding each sample, as well as best practices for creating an interview plan (this was established in collaboration with our user research team).

After putting the system prompt in place, Anthropic Interviewer used its knowledge of our research goal (see section below) to generate specific questions and a planned conversation flow. There was then a review phase where human researchers collaborated with Anthropic Interviewer to make any necessary edits to finalize the plan.

#### Interviewing

Anthropic Interviewer then conducted real-time, adaptive interviews following its interview plan. At this stage, we included a system prompt to instruct Anthropic Interviewer how to use best practices for interviews.

The interviews conducted by Anthropic Interviewer appeared on Claude.ai and lasted about 10-15 minutes with each participant.

![The interviews were conducted on an interface like this on claude.ai.](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe6678158f5572d1f9f6945c2fdcc02275d2a371f-2272x1600.png&w=3840&q=75)

The interviews were conducted on an interface like this on claude.ai (above is the module now live for users).

#### Analysis

Once interviews were complete, a human researcher collaborated with Anthropic Interviewer to analyze the transcripts. Anthropic Interviewer's analysis step takes as input the initial interview plan and outputs answers to the research questions alongside illustrative quotations. At this stage, we also used our [automated AI analysis tool](https://www.anthropic.com/research/clio) to identify emergent themes and quantify their prevalence across participants.

### Research goals

As described above, Anthropic Interviewer was made aware of the research goals through its system prompt, and ran its interviews in such a way as to address them. Note that, in this initial study, our main intention was to perform a practical test of Anthropic Interviewer; the goals below nonetheless provided interesting data which we analyze below.

The following were the main research goals for each subsample:

- **General workforce.** "Understand how individuals integrate AI tools into their professional workflows, exploring usage patterns, task preferences, and interaction styles to gain insights into the evolving relationship between humans and AI in workplace contexts."
- **Creatives.** "To understand how creative professionals currently integrate AI into their creative processes, their experiences with AI's impact on their work, and their vision for the future relationship between AI and human creativity."
- **Scientists.** "To understand how AI systems integrate into scientists' daily research workflows, examining their current usage patterns, perceived value, trust levels, and barriers to adoption across different stages of the scientific process."

## Results

Below we discuss what we discovered in our interviews and provide quantitative data from our survey and thematic analysis.

### AI's impact in the general workforce

Overall, the members of our general sample of professionals described AI as a boost to their productivity. In the survey, 86% of professionals reported that AI saves them time and 65% said they were satisfied with the role AI plays in their work.

One theme that surfaced is how workplace dynamics affect the adoption of AI. 69% of professionals mentioned the social stigma that can come with using AI tools at work—one fact-checker told Anthropic Interviewer: "A colleague recently said they hate AI and I just said nothing. I don't tell anyone my process because I know how a lot of people feel about AI."

Whereas 41% of interviewees said they felt secure in their work and believed human skills are irreplaceable, 55% expressed anxiety about AI's impact on their future. 25% of the group expressing anxiety said they set boundaries around AI use (e.g. an educator always creating lesson plans themselves), while 25% adapted their workplace roles, taking on additional responsibilities or pursuing more specialized tasks.