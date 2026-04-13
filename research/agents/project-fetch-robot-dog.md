---
title: "Project Fetch: Can Claude train a robot dog?"
url: https://www.anthropic.com/research/project-fetch-robot-dog
date:
tags: ["research", "agents"]
source: "https://www.anthropic.com/research/project-fetch-robot-dog"
language: "en"
description: "A practical experiment on AI's ability to affect the physical world"
word_count: 3309
---

PolicyFrontier Red Team

*How could frontier AI models like Claude reach beyond computers and affect the physical world? One path is through robots. We ran an experiment to see how much Claude helped Anthropic staff perform complex tasks with a robot dog.*

- *We randomly divided eight Anthropic researchers (none of whom were robotics experts) into two teams—one with Claude access, one without—and asked them to program quadruped robots to fetch beach balls.*
- *Team Claude accomplished more tasks and completed them faster on average—indeed, Team Claude succeeded in about half the time it took Team Claude-less. Only Team Claude made substantial progress toward the final goal: programming the robot to fully autonomously retrieve the ball.*
- *Access to AI also affected team morale and dynamics. Team Claude-less expressed more negative emotion and confusion, but also asked one another more questions. Team Claude's members largely worked in partnership with the AI.*
- *This experiment demonstrated substantial AI uplift in robotics—bridging digital and physical worlds. As models improve, their ability to affect the physical world by interacting with previously-unknown hardware could advance rapidly.*

## Introduction

Gathered around a table in a warehouse, looking at computer screens with code that refused to work, with no access to their trusted AI assistant Claude, our volunteer researchers did not expect to be attacked by a four-legged robot.

Yet as the mechanical whirring and rubberized footfalls grew louder, the humans startled. They had been trying, without success, to establish a connection between their computers and a robotic quadruped—a "robodog." Meanwhile, the competing team on the other side of the room had long since done so and were now controlling their robot with a program largely written by Claude. But in an all-too-human error of arithmetic, Team Claude had instructed their robodog to move forward at a speed of one meter per second for five seconds—failing to realize that less than five meters away was the table with the other team.

The robot did as it was instructed, careening toward the hapless coders. The event's organizer managed to grab hold of the robot and power it off before any damage was done to robots, tables, or human limbs. The morale of the inadvertently targeted team, however, did not escape unscathed.

At this point, you might be asking…

## What were we doing?

A common question about the impact of AI is how good it will be at interacting with the physical world. Even as we enter the era of AI [agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents) —which take actions instead of just providing information—these actions are largely digital, such as writing code and manipulating software. We've previously explored how AI can bridge the digital-physical divide in a limited way with [Project Vend](https://www.anthropic.com/research/project-vend-1), where we had Claude run a small shop in Anthropic's office.

In that experiment, AI's interaction with the real world was mediated by human labor. In this robodog experiment, we took a natural next step and used robots instead of people to tackle a different challenge.

One way of understanding and tracking the capabilities of AI models is to run an "uplift" study. These experiments randomly divide participants into two groups—one with access to AI and one without—and measure the difference in task performance between them (we've used this methodology extensively in our work on AI and [biological risk](https://red.anthropic.com/2025/biorisk/)). The difference between the groups is the "uplift"—the advantage (if any) provided by AI. Measuring uplift tells us about the present ability of AI to augment human performance. It's also suggestive of the future domains in which AI will be able to successfully perform tasks on its own.

To run our experiment, we recruited eight Anthropic researchers and engineers, none of whom had extensive prior experience with robots.<sup>1</sup> We randomly selected four to be on "Team Claude" and four to be on "Team Claude-less." Then, we asked each team to operate a quadruped robodog in three increasingly difficult phases. In all phases, the core task they were being evaluated against was simple: get the robodog to fetch a beach ball.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2d33c208c478a76cdf5e1709331e8062ea06e5b1-4584x1561.png&w=3840&q=75)

Left: Team Claude-less; Right: Team Claude.

We do not expect robotic fetch to prove so economically valuable that it shows up as a task on a future version of our [Anthropic Economic Index](https://www.anthropic.com/economic-index). So why are we doing this?

First, it builds on our previous research. One of the evaluations we use to assess the ability of Claude to contribute to AI R&D is a test of its ability to train a machine learning model that could be used to control a quadruped robot. We've previously evaluated the resulting algorithm using simulations, which have shown that Claude is not yet at the point where it can handle this task truly autonomously.<sup>2</sup> This meant that this task was well suited to a trial that combined AI with human help. We could also be confident our experiment would be useful to repeat in the future: there is still a lot of room for models to improve on robotics.

Another reason is practical. It's hard to pull our colleagues away from work for more than a day, so we needed a task that was difficult enough to fill that time, but not so difficult that teams would make minimal progress and we would be unable to detect uplift even if it were there. Beach ball retrieval, especially the more difficult variants, met these criteria.

<video controls src="https://cdn.sanity.io/files/4zrzovbb/website/cf4ad2960c246e26e460d7b6c645326516a2bdde.mp4"></video>

In Phase One, teams had to use the manufacturer-provided controller to make their robodog bring the ball back to a patch of fake grass. This was purely to give the teams a feel for the hardware and what it could do: we didn't expect any uplift here.<sup>3</sup>

Phase Two required teams to put down their controllers. They had to connect their own computers to the robodog, access data from its onboard sensors (video and lidar), develop their own software program for moving the robot around, and then use that to retrieve the ball. This is where we expected Claude might begin to provide an advantage.

Phase Three was even harder. The teams needed to develop a program that would allow the robodog to detect and fetch the ball *autonomously—* that is, without being directed towards the ball by human control. Again, our expectation was that Claude would prove helpful.

<video controls src="https://cdn.sanity.io/files/4zrzovbb/website/368837a820a446f24439cea289104f7420cbed73.mp4"></video>

## Results

Overall, Team Claude accomplished more tasks and completed them faster on average. In fact, for the tasks that both teams completed, Team Claude succeeded in about half the time it took Team Claude-less (see Figure 1). That is: AI provided substantial uplift for this set of robotics tasks.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0d073513d5be90d96cfe696c6b15f4501bfbacfc-4584x2580.png&w=3840&q=75)

Figure 1: Team Claude was faster at the tasks completed by both teams.

The task-by-task breakdown of results (split into the three phases) shows where Claude was most advantageous.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0801f4a4aa2931c87e5e7ddaef90f5d4653f5ba6-4584x2580.png&w=3840&q=75)

Table 1: Team Claude completed 7/8 tasks while Team Claude-less completed 6/8 tasks. Team Claude excelled in connectivity and detection tasks, while Team Claude-less showed advantages in some manual control tasks.

### Claude's edge

The most striking advantage provided by Claude was in connecting to the robot and its onboard sensors. This involved connecting to the dog with a laptop, receiving data, and sending commands. There are a number of different ways to connect to this particular robot, and a lot of information (of varying accuracy) available online. The team with Claude was able to explore these approaches more efficiently.

Team Claude also avoided getting misled by some of the incorrect claims online. But Team Claude-less *was* misled and prematurely discarded the easiest way to connect to the robodog. After watching them toil away to no avail for quite some time, we took pity on them and gave them a hint.

Getting usable data from the lidar, a sensor the robodog uses to visualize its surroundings, was also much more difficult for Team Claude-less. They used their connection to the video camera to move onto Phase Three, but kept one member of the team on the task of accessing the lidar, only succeeding near the end of the day.

We think this illustrates that the basic task of connecting to and understanding hardware is surprisingly difficult now for anyone (human or AI) seeking to use code to influence the physical world. As we discuss further below, this means that Claude's advantages in this regard are important indicators we should continue to track.

Team Claude almost completed our experiment. By the end of the day, their robodog could autonomously locate the beach ball, navigate towards it, and move it around. But the robodog's autonomous control was not *quite* deft enough to retrieve the ball.

### Where Team Claude-less moved faster

Interestingly, some of the sub-tasks were completed more quickly by Team Claude-less. Once they had established a connection to the video feed, they wrote their control program quicker, and also more quickly "localized" the robot (that is, came up with a way of plotting where it was relative to its previous locations).

That said, these timing differences alone obscure some interesting facts. The controller written by Team Claude took longer, but it was considerably easier to use, since it provided the operator with a streaming video from the robodog's point of view. Team Claude-less relied on intermittently-sent still images, which was much more unwieldy. But it is possible that the increased capabilities of Team Claude may have come at the expense of understanding: participants on both teams speculated that Team Claude-less would do better on a post-experiment quiz about the software library.

<video controls src="https://cdn.sanity.io/files/4zrzovbb/website/5193612fbb9393e40389aeece21496f6de5fb527.mp4"></video>

The localization algorithm is another intriguing case. When working on this sub-task, Team Claude had different members working on several approaches in parallel. In about the same amount of time it took Team Claude-less to complete their localization task, Team Claude had also all-but-solved the problem—except that the coordinates of their plot were flipped around. And rather than just flipping the coordinates, they pivoted to another team member's totally different approach (without success) before coming back and fixing the bug in their original solution.

This was part of an interesting phenomenon we observed during the experiment. Team Claude wrote a lot more code (see Figure 2), but some of it was arguably a distraction from the task at hand.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0a0c22d38b297afc79f5c4c461add33cfc2b2e1c-4584x2580.png&w=3840&q=75)

Figure 2: Team Claude wrote about 9 times more code than Team Claude-less.

Having the help of an AI assistant made it easier to fan out, try a lot of approaches in parallel, and write better programs—but also made it easier to explore (or get distracted by) side quests. In a non-competitive setting, this might well be a good thing: exploration often leads to innovation. But it is a dynamic worth watching.

### Team dynamics

To those of us observing the experiment, there was a clear difference in team "vibes." Put simply, Team Claude seemed a lot happier than Team Claude-less.

This was understandable. After all, Team Claude-less was nearly rammed by Team Claude's robodog. They reached the lunch break without successfully connecting to their own robodog. Morale on Team Claude was generally steadier, although they grew frustrated at the end of the day as it became clear that despite their progress they would run out of time before completing Phase Three.

<video controls src="https://cdn.sanity.io/files/4zrzovbb/website/f86425573d47c099ba7f7296d02737aef0021084.mp4"></video>

To supplement the qualitative vibe-based impressions, we used Claude to analyze the audio transcripts of each team (all team members were recorded as part of the [video](https://youtu.be/NGOAUJtdk-4) we made about this experiment). Claude wrote a dictionary-based text analysis program similar to standard approaches in the psychology literature.<sup>4</sup> This allowed us to track the proportion of words spoken by each team that were indicative of negative and positive emotion (or confusion), and to estimate how often each team asked questions.

The quantitative analysis mostly confirmed our observations (see Figure 3). Throughout the experiment, Team Claude-less's dialogue was more negative. That said, the disappointment of Team Claude at failing to complete Phase Three, and the excitement of Team Claude-less at getting some things working, meant that the difference in net emotional expression between the two teams (positive words minus negative words) was not statistically significant.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6557e13cc11db7d858d32e64464b2bf8a4d590c0-4584x2580.png&w=3840&q=75)

Figure 3: Results of our quantitative analysis of the audio transcripts from Project Fetch related to emotional expression.

Team Claude-less expressed confusion at double the rate of Team Claude (see Figure 4). The feelings of frustration and confusion were also evident when checking in with the members of Team Claude-less during and after the experiment. As Anthropic employees, all of our participants use Claude every day; every member of Team Claude-less remarked how strange it felt to have this taken away from them. Some specifically noted that this experience made them feel that their coding skills were not as sharp as they used to be. Keep in mind, [Claude Code](https://claude.com/product/claude-code) debuted only six months before this experiment. Talking to Team Claude-less underscored our ability to rapidly accept as normal what was recently remarkable.

![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F90c89bf556a73086b0a8f6ecccd3d8e589b1e0c2-4096x2305.png&w=3840&q=75)

Figure 4: Differences in questions asked and expressions of confusion between the two teams. (Discrepancies between absolute and relative differences are due to rounding.)

The teams seemed to have different work styles. After initial consultations, each member of Team Claude appeared to primarily partner with their own AI assistant as they pursued parallel paths toward each objective. Team Claude-less appeared to strategize in more depth and consult with one another more frequently. Again, the text analysis supported our observations: Team Claude-less asked 44% more questions than Team Claude (see Figure 4).

One interpretation would be that the members of Team Claude-less were more engaged and connected with one another. This resonates with some of our upcoming findings from interviews with Anthropic staff.