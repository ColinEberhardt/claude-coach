# Claude Running Race Coach

An AI-powered running coach built for [Claude Code](https://code.claude.com/) and [Claude Desktop](https://claude.ai/download) using the [Skills framework](https://code.claude.com/docs/skills). This project demonstrates how to combine Claude's capabilities with specialized training knowledge and training data to provide personalized running coaching assistance. Distributed as a plugin for easy installation.

**For usage instructions, see [running-race-coach/README.md](running-race-coach/README.md).**

## Overview

Claude Running Race Coach uses Claude Code's Skills framework to provide intelligent running coaching that includes:
- Evidence-based training plan generation
- Multi-platform training data integration (Strava, Garmin, manual entry, conversational)
- Weekly training analysis and coaching feedback
- Scientific pace calculation and workout planning

## Project Structure

```
claude-coach/
├── running-race-coach/         # Main plugin package
│   ├── README.md              # User-facing documentation
│   └── skills/                # Skill definitions
│       ├── training-plan/     # Training plan generation skill
│       │   ├── SKILL.md       # Skill definition and workflow
│       │   ├── references/    # Coaching guides and principles
│       │   │   └── coaches-guide.md
│       │   └── scripts/       # Pace and distance calculators
│       │       ├── calculate_paces.py
│       │       └── interval_calculator.py
│       ├── strava-sync/       # Strava data synchronization skill
│       │   └── SKILL.md       # Sync workflow and formatting
│       ├── training-dashboard/ # Training progress visualization
│       │   └── SKILL.md       # Dashboard generation workflow
│       └── running-coach/     # Weekly coaching analysis skill
│           └── SKILL.md       # Coaching workflow and principles
├── training-log/              # Generated weekly training summaries
├── coaching-log/              # Coaching session notes
├── training-plan.md          # Generated training plans
├── package.py                # Plugin packaging script
└── README.md                 # This file
```

## Skills Architecture

This project leverages Claude Code's [Skills framework](https://code.claude.com/docs/skills), which allows Claude to follow structured workflows for specific domains. Each skill is a combination of:

### 1. Skill Definition (`SKILL.md`)

Each `SKILL.md` file defines:
- **Invocation patterns**: Keywords and phrases that trigger the skill
- **Workflow steps**: Structured process Claude follows
- **Best practices**: Domain-specific knowledge and principles
- **Tool usage**: When to use Python scripts or MCP servers
- **Output format**: How to structure the results

### 2. Reference Documentation

The `references/` directory contains in-depth knowledge that Claude loads into context when needed. For example:
- **coaches-guide.md**: Comprehensive training principles, periodization strategies, and workout guidelines

### 3. Executable Tools

Python scripts in the `scripts/` directories provide:
- **calculate_paces.py**: Calculates training pace zones from race goal times
- **interval_calculator.py**: Computes total distances for interval workouts

These are executed via Claude Code's terminal integration.

### 4. Integration with MCP Servers

Skills can leverage Model Context Protocol (MCP) servers for external data:
- **Strava MCP server**: Fetches activity data, athlete info, and statistics
- Extensible to other platforms (Garmin, Apple Health, etc.)

## How It Works

### Training Plan Generation

When a user requests a training plan:
1. **training-plan** skill is invoked
2. Claude gathers requirements (race distance, goal time, current mileage, race date)
3. Executes `calculate_paces.py` to determine training zones
4. Applies periodization principles from `coaches-guide.md`
5. Generates structured markdown training plan
6. Uses `interval_calculator.py` to calculate workout distances
7. Saves plan to `training-plan.md`

### Training Data Synchronization

The **strava-sync** skill:
1. Connects to Strava MCP server
2. Fetches recent activities (configurable time range)
3. Extracts detailed metrics (pace, heart rate, power, cadence, elevation)
4. Parses lap data for interval workouts
5. Formats data as structured markdown
6. Saves to `training-log/week-n.md`

The system is flexible and also supports:
- Manual markdown file creation
- Data import from other platforms (Garmin, Apple Health, Polar Flow)
- Conversational data input (describe workouts verbally)

### Weekly Coaching Analysis

The **running-coach** skill:
1. Loads the user's training plan
2. Retrieves training log (from any source)
3. Asks for subjective feedback (energy, fatigue, challenges)
4. Compares planned vs. actual execution for each workout
5. Analyzes:
   - Pace accuracy (easy, threshold, intervals, race pace)
   - Heart rate zones and effort levels
   - Workout execution quality
   - Weekly volume and progression
6. Assesses progress toward race goal
7. Provides specific recommendations
8. Documents session in `coaching-log/week-n-coaching-notes.md`

## Development Setup

### Prerequisites

- [Claude Code](https://code.claude.com/)
- Python 3.8+ (for pace calculation scripts)
- (Optional) Node.js 18+ (for Strava MCP server)

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ColinEberhardt/claude-running-coach.git
   cd claude-running-coach
   ```

2. **Open in Claude Code**:
   ```bash
   code . --profile claude
   ```

3. **(Optional) Configure Strava MCP Server**:
   
   Add to `~/.claude/config.json`:
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

4. **Test skills**:
   - Open Claude Code chat
   - Ask: "Create a 10-week 10K training plan for a 45:00 goal"
   - Verify the training-plan skill executes correctly

## License

MIT License - see [LICENSE](LICENSE) for details.

This project is provided as-is for educational purposes. Always consult qualified professionals for personalized training advice.
