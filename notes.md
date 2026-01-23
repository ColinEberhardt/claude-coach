## Development notes

Training plan
 - does this need a skill? at the very least it prompt for duration, pace etc ...
 - first step, asked claude to create a training plan skill - looked good, but feeding to ChatGPT to critique it was a little generic feeling
 - asked ChatGPT to create a 'coaches guide' for creating training plans
 - read the skill, this aint vibe coding
 - generated some typical plans, asked claude to evaluate

>   This is very similar to:
>  - Pfitzinger's HM plans (12/47 or 12/63): Same threshold emphasis, recovery week pattern, volume progression
>  - Jack Daniels' approach: Similar intensity distribution and phase structure
>  - Modern coaching consensus: Polarized training (~80% easy), threshold as HM driver, race-pace specificity

 - checked paces etc ...
 - Q: how good is claude at maths?!

 Creating my plan - "please create a half marathon training plan, 12 weeks, targeting a finish of 83 minutes"
 Now I'll create your 12-week half marathon training plan. Given that you're training only 3 days per week with
  20-30 miles as your base, I'll need to be strategic about making each session count while building toward your
  ambitious 83-minute goal.

  - weekly mileages were wrong, it cannot do complex maths (out by ~30%)
  - vibe coded script for maths

   - next iteration, paces were a bit suspect (threshold < race pace)
  - vibed a pace calculator

  > I notice you indicated 3 days per week for training. This is quite limited for an 83-minute half marathon goal
  (which is highly competitive). With only 3 running days per week, you'll need very focused, quality sessions.


  

## General Ponderings
 - If something is a deterministic and repeatable task? should I script it
 - When do you rely on LLM knowledge (e.g. training plans), when do you give examples?
 - Do you need to give it help it with maths?
