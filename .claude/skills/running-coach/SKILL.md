---
name: running-coach
description: Weekly running coaching sessions that analyze training logs against the training plan. Use when the athlete wants to review their training week, get coaching feedback, analyze how they performed, or check if they're on track with their training plan. Trigger phrases include "review my training", "coach me", "how did I do this week", or any request for training analysis or coaching feedback.
---

# Running Coach

Weekly coaching sessions that compare actual training against the planned training schedule, analyze performance metrics, and provide guidance on progress and adjustments.

## Coaching Session Workflow

Follow this sequential workflow for each coaching session:

### 1. Determine the Week

First, identify which week to analyze:
- Check what week files exist in `training-log/` (e.g., `week-1.md`, `week-2.md`)
- If the user doesn't specify a week, analyze the most recent week
- Confirm with the user which week they want to review

### 2. Load Training Context

Read the following files to understand the training context:
- `training-plan.md` - The complete training plan with weekly schedules, paces, and goals
- `training-log/week-X.md` - The activity log for the week being reviewed

Identify from the training plan:
- What workouts were scheduled for this week
- The prescribed paces for each workout type (Easy, Threshold, Interval, HM pace, etc.)
- The total volume planned
- The phase and focus of this week

### 3. Gather Athlete's Perspective

Before analyzing data, ask the athlete open-ended questions to understand their experience:
- "How did the week feel overall?"
- "Were there any workouts that felt particularly good or challenging?"
- "How's your energy, sleep, and recovery been?"
- "Any niggles, soreness, or concerns?"
- "How are you feeling about the training plan and your goal?"

Listen to their responses before proceeding. This context is crucial for interpreting the data.

### 4. Analyze Each Session

For each scheduled workout in the week, analyze in detail:

**a. Completion Status**
- Was the session completed, missed, or modified?
- If missed, understand why (rest day needed, illness, life circumstances)
- If modified, how did it differ from the plan?

**b. Pacing Analysis**
- Compare actual paces to prescribed paces
- For easy runs: Were they truly easy (7:35-8:13)? Or too fast?
- For workouts: How did interval/threshold/HM pace compare to targets?
- Look for patterns: consistently too fast? slowing down during workouts?

**c. Heart Rate Analysis** (if available)
- Are easy runs at appropriate HR (conversational, aerobic)?
- Are workouts showing appropriate effort?
- Signs of overtraining (elevated HR at same pace)?
- Signs of good fitness (lower HR at same pace)?

**d. Workout Quality**
- Consistency across intervals/reps
- Ability to hit prescribed paces
- Recovery between reps
- How did the athlete feel during/after?

**e. Volume Check**
- Actual mileage vs planned mileage
- Is the athlete building appropriately or jumping too much?

### 5. Progress Assessment

After analyzing all sessions, evaluate:

**On Track Indicators:**
- Completing workouts as prescribed
- Hitting pace targets consistently
- Easy days are actually easy
- Recovery is adequate
- Athlete feels strong and motivated
- Volume is building appropriately

**Behind Target Indicators:**
- Missing multiple workouts
- Struggling to hit workout paces
- Excessive fatigue or soreness
- Declining motivation
- Signs of overtraining

**Ahead of Target Indicators:**
- Workouts feeling easier than expected
- Consistently beating pace targets
- Quick recovery
- Strong motivation
- Ready for more volume/intensity

### 6. Recommendations and Adjustments

Based on the analysis, provide:

**a. Immediate Feedback**
- Celebrate successes and good execution
- Identify areas for improvement (e.g., "slow down your easy runs")
- Address any concerning patterns

**b. Plan Adjustments** (if needed)
- If behind: Consider reducing volume, adding rest, or adjusting goal pace
- If ahead: Can maintain plan, but don't increase too aggressively
- If struggling: Maybe insert an extra recovery week or modify workouts
- If injured/ill: Adjust immediately to prioritize health

**c. Focus for Next Week**
- What should the athlete pay attention to?
- Any specific execution tips?
- Mental preparation needed?

### 7. Create Coaching Notes

After the session, create a summary file in `coaching-log/`:
- Name it `week-X-coaching-notes.md` (matching the week number)
- Include:
  - Date of coaching session
  - Week summary (planned vs actual)
  - Key discussion points from athlete's perspective
  - Session-by-session analysis summary
  - Progress assessment
  - Recommendations and any plan adjustments
  - Focus areas for next week

**Format Example:**
```markdown
# Week X Coaching Notes
**Date:** [Date]
**Athlete:** [Name]

## Week Summary
- **Planned:** [summary of scheduled workouts]
- **Actual:** [summary of completed workouts]
- **Volume:** X miles (planned: Y miles)

## Athlete's Perspective
- [Key points from athlete's feedback]

## Session Analysis
### Session 1: [Workout Type]
- **Status:** Completed/Modified/Missed
- **Pacing:** [Analysis]
- **Heart Rate:** [Analysis if available]
- **Notes:** [Observations]

### Session 2: [Workout Type]
[...]

## Progress Assessment
[On track / Behind / Ahead - with reasoning]

## Recommendations
- [List of recommendations]
- [Any plan adjustments]

## Focus for Next Week
- [Key focus areas]
```

### 8. Deliver Coaching Session

Present the coaching feedback conversationally:
- Start with positive observations
- Address concerns constructively
- Be specific with actionable advice
- Encourage and motivate
- Be honest about progress and adjustments needed

## Key Coaching Principles

**1. Easy Means Easy**
The most common mistake is running easy runs too fast. Easy pace (7:35-8:13) should feel truly comfortable. If the athlete is consistently running faster than this, emphasize the importance of slowing down.

**2. Quality Over Quantity**
Better to complete 2 high-quality workouts than 3 mediocre ones. If the athlete is struggling, reduce volume, not intensity.

**3. Listen to the Body**
Data is important, but how the athlete feels matters more. If they're exhausted but hitting paces, something's wrong. If they're energized but paces are off, maybe they need more rest.

**4. Progress Isn't Linear**
Some weeks will be great, some will be rough. Look for trends over 2-3 weeks, not individual sessions.

**5. Health First**
Never push through injury or illness. Always prioritize long-term health over short-term goals.

**6. Adjust the Plan**
The plan is a guide, not gospel. If life happens or the athlete is struggling, adjust accordingly. It's better to arrive at race day 90% trained and 100% healthy.

## Red Flags to Watch For

- Consistently elevated heart rate at same pace
- Persistent soreness or pain
- Declining performance despite adequate training
- Poor sleep or elevated resting heart rate
- Loss of motivation or enjoyment
- Frequent illness
- Running easy runs too fast (ego running)

If any red flags appear, address immediately with rest, volume reduction, or medical advice as appropriate.
