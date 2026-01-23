---
name: strava-sync
description: Downloads and syncs training data from Strava. Stores the last week's worth of activities in the training-log folder as markdown summaries, including lap details for workout runs.
---

# Strava Training Log Sync

## Overview

This skill downloads training data from Strava and creates weekly markdown summaries in the `training-log` folder. Each week is stored as a single markdown file with detailed activity summaries, including lap details for runs marked as workouts.

## Workflow

### 1. Check Strava Connection

First, verify that Strava is connected:

```bash
# Check connection status
```

Use the `mcp__strava__check-strava-connection` tool to verify the connection. If not connected, use `mcp__strava__connect-strava` to authenticate.

### 2. Fetch Recent Activities

Retrieve the last 7 days of activities from Strava:

1. Use `mcp__strava__get-recent-activities` to fetch recent activities (default 30 activities)
2. Filter activities to only those from the last 7 days
3. Calculate the week date range (e.g., "2024-01-15 to 2024-01-21")

### 3. Process Each Activity

For each activity in the last week:

1. Extract key information:
   - Activity name
   - Date and time
   - Activity type (Run, Ride, Swim, etc.)
   - Distance (convert to miles or km)
   - Duration (format as HH:MM:SS)
   - Elevation gain
   - Average pace/speed
   - Average heart rate (if available)
   - Description/notes

2. Check if the activity is marked as a workout:
   - Look for the `workout_type` field in the activity data
   - For runs: workout_type 0 = default run, 1 = race, 2 = long run, 3 = workout

3. For workout or long runs, fetch lap details:
   - Use `mcp__strava__get-activity-laps` with the activity ID
   - Extract lap information:
     - Lap number
     - Distance
     - Duration
     - Average pace
     - Average heart rate
     - Elevation gain

### 4. Format as Markdown

Create a markdown file with the following structure:

```markdown
# Training Log: [Start Date] to [End Date]

## Week Summary

- **Total Activities**: [count]
- **Total Distance**: [distance] miles/km
- **Total Time**: [duration]
- **Total Elevation**: [elevation] ft/m

## Activities

### [Date] - [Activity Name]

**Type**: [Run/Ride/Swim/etc.]
**Distance**: [distance] mi
**Duration**: [HH:MM:SS]
**Pace**: [pace per mile/km]
**Elevation**: [elevation] ft
**Heart Rate**: [avg bpm] (max: [max bpm])

[Activity description/notes if available]

#### Lap Details

| Lap | Distance | Time | Pace | HR | Elevation |
|-----|----------|------|------|-----|-----------|
| 1   | [dist]   | [time] | [pace] | [hr] | [elev] |
| 2   | [dist]   | [time] | [pace] | [hr] | [elev] |

---

[Continue for each activity...]
```

### 5. Save to training-log Folder

1. Create the `training-log` folder if it doesn't exist:
   ```bash
   mkdir -p training-log
   ```

2. Generate filename based on week dates:
   - Format: `week-YYYY-MM-DD.md` (using the Monday of that week)
   - Example: `week-2024-01-15.md`

3. Write the markdown content to the file

### 6. Provide Summary

After syncing, provide a brief summary:
- Number of activities synced
- Date range covered
- File location
- Any activities that are workouts with lap details

## MCP Tools Used

- `mcp__strava__check-strava-connection`: Verify Strava authentication
- `mcp__strava__connect-strava`: Connect to Strava if needed
- `mcp__strava__get-recent-activities`: Fetch recent activities
- `mcp__strava__get-activity-details`: Get detailed info for specific activities (if needed)
- `mcp__strava__get-activity-laps`: Fetch lap details for workout runs

## Error Handling

- If Strava is not connected, prompt user to authenticate
- If no activities found in the last week, inform the user
- If lap details are unavailable, note this in the markdown
- Handle API rate limits gracefully

## Notes

- The skill focuses on the last 7 days of data
- Workout detection is specific to runs (workout_type field)
- Lap details are only fetched for activities marked as workouts
- Distance and pace units should match user preference (miles vs km)
- All times should be in local time zone
