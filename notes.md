# Development Notes

This is a collection of notes documenting my thoughts and learnings throughout the project.

## Should I Build This?

I was always going to build this for fun, but the question was worth considering. There are already apps for training plans, but they lack flexibility. What happens if I need to pivot training halfway through? They also lack genuine coaching, which makes this an ideal LLM application.

ChatGPT can already do this to some extent. If you ask for a typical plan (like a half marathon in 1:30), it nails it because it's already in the training dataset. However, I wanted something more specific: 83 minutes with 3 sessions per week. When I tried that, the plan looked good at a high level but had issues. The maths was wrong—weekly mileage didn't match the sessions—and more importantly, the pace zones were incorrect.

## Training Plan Skill

My first attempt was to prompt Claude with a few sentences to build the skills for me. The goal was to collect a few key metrics (plan duration, target time, race distance) and then build a plan.

While I got Claude to generate the skill, it wasn't entirely vibe-coded. I did review and tweak it.

After executing, the initial plans looked good. The question was how to test and validate them. I manually reviewed the plans and also asked ChatGPT. It looked good, but when I fed it to ChatGPT for critique, it reported that the plan felt a little generic.

### Coaches Guide

I asked ChatGPT to create a 'coaches guide' for creating training plans. It described the typical phased structure, pace zones, microcycles, and race length specific focus.

I updated the skill to use the coaches guide. ChatGPT was much happier with the result:

> This is very similar to:
> - Pfitzinger's HM plans (12/47 or 12/63): Same threshold emphasis, recovery week pattern, volume progression
> - Jack Daniels' approach: Similar intensity distribution and phase structure
> - Modern coaching consensus: Polarized training (~80% easy), threshold as HM driver, race-pace specificity

When creating my plan, I asked: "please create a half marathon training plan, 12 weeks, targeting a finish of 83 minutes." Claude responded: "Now I'll create your 12-week half marathon training plan. Given that you're training only 3 days per week with 20-30 miles as your base, I'll need to be strategic about making each session count while building toward your ambitious 83-minute goal."

### Claude Can't Do Maths

At this point, I spotted that weekly mileages were wrong (out by approximately 30%). Claude was thrown by the interval sessions, which require computing session distance based on repeated intervals. I vibe-coded a script that it can use and updated the skill to use this.

On the next iteration, I spotted that the paces were suspect. For the half marathon, it had "threshold < race pace," which is wrong. Threshold should be your 60-minute pace, while my half marathon time is approximately 1:30. I vibe-coded a pace calculator to fix this.

## Strava Sync Skill

The next step was to download actual sessions. This was very easy using Strava MCP. However, maths was an issue again. Rather than write a script, I added:

> **IMPORTANT**: Use Python to calculate all totals to ensure mathematical accuracy. Do NOT calculate totals manually.

This fixed the problem.

Given that this is a deterministic transform—download Strava data and format in markdown—the question arose: should I use an LLM for this, or should I just write a script?

## Coach Skill

This was surprisingly easy.
