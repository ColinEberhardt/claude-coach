# Claude Coach

An experimental AI-powered running coach built with [Claude Code](https://code.claude.com/) and the [Skills framework](https://code.claude.com/docs/skills). This project demonstrates how to combine Claude's capabilities with specialized training knowledge and real-time Strava data to provide personalized running coaching assistance.

**This is an educational project to explore the intersection of AI, endurance training, and developer tools.**

## Features

- **Training Plan Generation**: Create personalized 5K, 10K, Half Marathon, and Marathon training plans with scientifically-backed progression and pacing
- **Strava Integration**: Automatically sync and analyze your training data from Strava
- **Weekly Training Logs**: Generate detailed markdown summaries of your workouts, including lap-by-lap analysis for interval sessions
- **Weekly Coaching Sessions**: Compare actual training against planned workouts, analyze performance metrics, and receive personalized coaching feedback
- **Pace Calculation**: Scientific training pace zones calculated from your race goals
- **Evidence-Based Coaching**: Built on established training principles and progressive overload strategies

## Requirements

- [Claude Code CLI](https://code.claude.com/)
- Python 3.8+ (for pace calculation and interval distance scripts)
- A [Strava account](https://www.strava.com/) with activities to analyze
- Strava MCP server configured in Claude Code

## Setup

### 1. Install Claude Code

Follow the [official installation guide](https://code.claude.com/docs/getting-started).

### 2. Clone This Repository

```bash
git clone https://github.com/yourusername/claude-coach.git
cd claude-coach
```

### 3. Configure Strava MCP Server

Add the Strava MCP server to your Claude Code configuration (`~/.claude/config.json`):

```json
{
  "mcpServers": {
    "strava": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-server-strava"]
    }
  }
}
```

### 4. Connect Your Strava Account

When you first use the strava-sync skill, Claude will prompt you to authenticate with Strava. Follow the authorization flow in your browser.

## Usage

### Generate a Training Plan

Ask Claude to create a training plan:

```
Create a 12-week half marathon training plan. My race is on March 15th,
I'm currently running 25 miles per week, and my goal is to finish in 1:35:00.
```

Claude will use the `training-plan` skill to generate a comprehensive markdown training plan with:
- Calculated training pace zones
- Phase-by-phase progression
- Week-by-week workout schedules
- Distance-based interval workouts
- Tapering strategy

### Sync Your Training Data

Download and summarize your recent Strava activities:

```
Sync my last week of training from Strava
```

The `strava-sync` skill will:
- Fetch your recent activities
- Generate a markdown summary with weekly totals
- Include detailed lap analysis for workout runs
- Save to the `training-log/` directory

### Get Weekly Coaching

After syncing your training data, request a coaching session:

```
Coach me on this week
```

The `running-coach` skill will:
- Compare your actual training against the planned workouts
- Analyze pacing, heart rate, and workout execution
- Assess your progress toward your race goal
- Provide actionable recommendations and adjustments
- Generate coaching notes saved to `coaching-log/`

### Ask Training Questions

Get evidence-based coaching advice:

```
How should I pace my long runs during marathon training?
What should my heart rate zones be for easy runs?
Should I do my threshold workout if my legs are tired?
```

## Project Structure

```
claude-coach/
├── .claude/
│   └── skills/
│       ├── training-plan/      # Training plan generation skill
│       │   ├── SKILL.md        # Skill definition and workflow
│       │   ├── references/     # Coaching guides and principles
│       │   └── scripts/        # Pace and distance calculators
│       ├── strava-sync/        # Strava data synchronization skill
│       │   └── SKILL.md        # Sync workflow and formatting
│       └── running-coach/      # Weekly coaching analysis skill
│           └── SKILL.md        # Coaching workflow and principles
├── training-log/               # Generated weekly training summaries
│   └── week-n.md              # Example: Weekly activity log
├── coaching-log/               # Coaching session notes
│   └── week-n-coaching-notes.md  # Session analysis and recommendations
├── training-plan.md           # Generated training plans
└── README.md                  # This file
```

## Skills

### training-plan

Creates comprehensive, evidence-based training plans for various race distances.

**Capabilities:**
- Supports 5K, 10K, Half Marathon, and Marathon distances
- Calculates six training pace zones (Easy, Steady, Threshold, VO₂max, Repetition, Race)
- Structures plans into progressive phases (Base, Build, Peak, Taper)
- Generates week-by-week schedules with specific workouts
- Includes warm-up, intervals, and cool-down structure for all quality sessions

**Tools:**
- `calculate_paces.py`: Generates training paces from target race time
- `interval_calculator.py`: Calculates total distance for interval workouts

### strava-sync

Downloads training data from Strava and generates markdown training logs.

**Capabilities:**
- Fetches the last 7 days of activities
- Generates weekly summary with totals (distance, time, elevation)
- Creates detailed activity cards with metrics (pace, heart rate, power, cadence)
- Includes lap-by-lap breakdowns for workout runs
- Formats output as readable markdown

**Requirements:**
- Strava MCP server configured
- Authenticated Strava account

### running-coach

Provides weekly coaching sessions that analyze your training execution against your plan.

**Capabilities:**
- Compares actual workouts to planned sessions
- Analyzes pacing accuracy (easy runs, threshold, intervals, race pace)
- Reviews heart rate data and effort levels
- Identifies training patterns and potential issues
- Assesses progress toward race goals (on track, ahead, behind)
- Provides specific, actionable recommendations
- Generates coaching notes with session-by-session analysis

**Workflow:**
1. Loads your training plan and weekly training log
2. Gathers your subjective feedback on the week
3. Analyzes each session (pacing, heart rate, execution quality)
4. Evaluates overall progress and fitness trends
5. Provides recommendations and plan adjustments if needed
6. Documents the coaching session in `coaching-log/`

## How It Works

Claude Coach leverages Claude Code's [Skills framework](https://code.claude.com/docs/skills), which allows Claude to follow structured workflows for specific domains. Each skill is defined by:

1. **SKILL.md**: A markdown file that teaches Claude the workflow, principles, and best practices
2. **references/**: In-depth documentation loaded into Claude's context
3. **scripts/**: Executable tools for calculations and data processing
4. **assets/**: Templates or resources used in outputs

When you ask a training-related question, Claude:
1. Identifies which skill to invoke
2. Loads the skill's knowledge and workflows
3. Executes the appropriate steps (fetching data, running calculations, analyzing performance)
4. Produces structured, evidence-based results

For weekly coaching sessions, Claude:
1. Reads your training plan and training log
2. Asks about your subjective experience
3. Compares planned vs. actual execution for each workout
4. Analyzes pacing, heart rate, and performance patterns
5. Provides specific feedback and recommendations
6. Documents the session in markdown coaching notes

## Educational Goals

This project explores:
- **Domain-specific AI**: How to teach Claude specialized knowledge (endurance training principles and coaching methodologies)
- **Structured workflows**: Using skills to ensure consistent, high-quality outputs
- **Tool integration**: Combining Claude with external APIs (Strava) and scripts
- **Data synthesis**: Transforming raw training data into actionable insights
- **Comparative analysis**: Teaching Claude to compare planned vs. actual execution and identify patterns
- **Conversational coaching**: Gathering subjective feedback and providing personalized guidance

## Limitations

- **Not a substitute for professional coaching**: This is an experimental tool for educational purposes. Always consult qualified coaches and medical professionals for personalized advice.
- **Individual variability**: Training plans may not account for individual physiology, injury history, life circumstances, or recovery capacity
- **Strava dependency**: Training log and coaching features require Strava data
- **Evolving technology**: Claude Code and the Skills framework are actively being developed
- **Data quality**: Coaching analysis depends on accurate heart rate, pace, and GPS data from your activities

## License

MIT License - see [LICENSE](LICENSE) for details.

This project is provided as-is for educational and experimental purposes. Always consult with qualified professionals for personalized training advice.

## Contributing

This is an experimental project, but suggestions and improvements are welcome! Feel free to:
- Open issues for bugs or feature ideas
- Submit PRs for skill improvements
- Share your training plan results
- Suggest additional coaching resources

## Acknowledgments

- Built with [Claude Code](https://code.claude.com/) by Anthropic
- Training principles based on established coaching literature and periodization frameworks
- Powered by [Strava API](https://developers.strava.com/) via the [MCP Strava server](https://github.com/modelcontextprotocol/servers/tree/main/src/strava)
- Inspired by evidence-based coaching from Jack Daniels, Pete Pfitzinger, and other endurance training experts

## Resources

- [Claude Code Documentation](https://code.claude.com/docs)
- [Skills Framework Guide](https://code.claude.com/docs/skills)
- [Strava API Documentation](https://developers.strava.com/docs/reference/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---

**Disclaimer**: This is an experimental educational project. Always listen to your body, consult with medical professionals before starting a new training program, and adjust plans based on your individual needs and circumstances.
