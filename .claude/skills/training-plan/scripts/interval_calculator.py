#!/usr/bin/env python3
"""
Interval Workout Calculator

Calculates total distance and time for an interval training session.
"""

import sys
import argparse


def parse_pace(pace_str):
    """
    Parse pace string in format 'MM:SS' or 'M:SS' and return seconds per unit.
    Example: '6:30' returns 390 seconds
    """
    try:
        parts = pace_str.split(':')
        if len(parts) != 2:
            raise ValueError
        minutes = int(parts[0])
        seconds = int(parts[1])
        return minutes * 60 + seconds
    except (ValueError, IndexError):
        print(f"Error: Invalid pace format '{pace_str}'. Use MM:SS format (e.g., '6:30')")
        sys.exit(1)


def format_time(seconds):
    """Convert seconds to HH:MM:SS or MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"


def parse_distance(dist_str):
    """
    Parse distance string like '1km', '1.5km', '1mi', '400m'.
    Returns distance in kilometers.
    """
    dist_str = dist_str.lower().strip()

    try:
        if dist_str.endswith('km'):
            return float(dist_str[:-2])
        elif dist_str.endswith('mi') or dist_str.endswith('mile') or dist_str.endswith('miles'):
            # Convert miles to km
            miles = float(dist_str.replace('mi', '').replace('mile', '').replace('miles', '').strip())
            return miles * 1.60934
        elif dist_str.endswith('m'):
            # Convert meters to km
            meters = float(dist_str[:-1])
            return meters / 1000
        else:
            # Assume km if no unit
            return float(dist_str)
    except ValueError:
        print(f"Error: Invalid distance format '{dist_str}'")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Calculate total distance and time for interval workouts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # 5 x 1 mile workout with distance-based recovery (default: miles)
  %(prog)s --warmup 1mi --warmup-pace 8:00 \\
           --intervals 5 --interval-dist 1mi --interval-pace 6:15 \\
           --recovery 0.25mi --recovery-pace 8:00 \\
           --cooldown 1mi --cooldown-pace 8:00

  # 6 x 800m with time-based recovery
  %(prog)s --warmup 1mi --warmup-pace 8:30 \\
           --intervals 6 --interval-dist 800m --interval-pace 6:20 \\
           --recovery-time 2:30 \\
           --cooldown 1mi --cooldown-pace 8:30

  # Using kilometers instead of miles
  %(prog)s --unit km --warmup 2km --intervals 5 --interval-dist 1km --interval-pace 6:15 \\
           --recovery 400m --cooldown 1.5km --easy-pace 8:00
        """
    )

    # Unit preference
    parser.add_argument('--unit', choices=['km', 'mi'], default='mi',
                        help='Preferred unit for pace display (default: mi)')

    # Easy pace (applies to warmup, recovery, and cooldown if their specific paces aren't set)
    parser.add_argument('--easy-pace', type=str,
                        help='Easy pace in MM:SS format (applies to warmup/recovery/cooldown if not specified)')

    # Warm-up
    parser.add_argument('--warmup', required=True,
                        help='Warm-up distance (e.g., 2km, 1.5mi, 1600m)')
    parser.add_argument('--warmup-pace', type=str,
                        help='Warm-up pace in MM:SS per unit (default: uses --easy-pace)')

    # Intervals
    parser.add_argument('--intervals', type=int, required=True,
                        help='Number of intervals')
    parser.add_argument('--interval-dist', required=True,
                        help='Interval distance (e.g., 1km, 800m, 1mi)')
    parser.add_argument('--interval-pace', type=str, required=True,
                        help='Interval pace in MM:SS per unit')

    # Recovery (mutually exclusive: distance-based or time-based)
    recovery_group = parser.add_mutually_exclusive_group(required=True)
    recovery_group.add_argument('--recovery', type=str,
                                help='Recovery distance between intervals (e.g., 400m, 0.25mi)')
    recovery_group.add_argument('--recovery-time', type=str,
                                help='Recovery time between intervals (MM:SS format)')

    parser.add_argument('--recovery-pace', type=str,
                        help='Recovery pace in MM:SS per unit (for distance-based recovery, default: uses --easy-pace)')

    # Cool-down
    parser.add_argument('--cooldown', required=True,
                        help='Cool-down distance (e.g., 1.5km, 1mi)')
    parser.add_argument('--cooldown-pace', type=str,
                        help='Cool-down pace in MM:SS per unit (default: uses --easy-pace)')

    args = parser.parse_args()

    # Validate easy-pace if specific paces aren't provided
    if not args.easy_pace:
        if not args.warmup_pace or not args.cooldown_pace:
            parser.error("--easy-pace is required when --warmup-pace or --cooldown-pace is not specified")
        if args.recovery and not args.recovery_pace:
            parser.error("--easy-pace is required when using --recovery without --recovery-pace")

    # Determine unit settings
    use_km = args.unit == 'km'
    unit = args.unit

    # Parse easy pace if provided
    easy_pace_str = args.easy_pace

    # Warm-up calculations
    warmup_dist_km = parse_distance(args.warmup)
    warmup_pace_str = args.warmup_pace if args.warmup_pace else easy_pace_str
    warmup_pace_sec = parse_pace(warmup_pace_str)
    warmup_time = warmup_dist_km * warmup_pace_sec / (1 if use_km else 1.60934)

    # Interval calculations
    num_intervals = args.intervals
    interval_dist_km = parse_distance(args.interval_dist)
    interval_pace_str = args.interval_pace
    interval_pace_sec = parse_pace(interval_pace_str)
    total_interval_dist = num_intervals * interval_dist_km
    total_interval_time = total_interval_dist * interval_pace_sec / (1 if use_km else 1.60934)

    # Recovery calculations
    if args.recovery:
        # Distance-based recovery
        recovery_dist_km = parse_distance(args.recovery)
        recovery_pace_str = args.recovery_pace if args.recovery_pace else easy_pace_str
        recovery_pace_sec = parse_pace(recovery_pace_str)
        total_recovery_dist = (num_intervals - 1) * recovery_dist_km
        total_recovery_time = total_recovery_dist * recovery_pace_sec / (1 if use_km else 1.60934)
        recovery_type = "distance"
    else:
        # Time-based recovery
        recovery_time_sec = parse_pace(args.recovery_time)
        total_recovery_time = (num_intervals - 1) * recovery_time_sec
        total_recovery_dist = 0
        recovery_type = "time"

    # Cool-down calculations
    cooldown_dist_km = parse_distance(args.cooldown)
    cooldown_pace_str = args.cooldown_pace if args.cooldown_pace else easy_pace_str
    cooldown_pace_sec = parse_pace(cooldown_pace_str)
    cooldown_time = cooldown_dist_km * cooldown_pace_sec / (1 if use_km else 1.60934)

    # Calculate totals
    total_dist_km = warmup_dist_km + total_interval_dist + total_recovery_dist + cooldown_dist_km
    total_time = warmup_time + total_interval_time + total_recovery_time + cooldown_time

    # Convert to display units
    display_factor = 1 if use_km else 0.621371

    # Print output
    print()
    print("=" * 60)
    print("WORKOUT SUMMARY")
    print("=" * 60)

    print("\nBREAKDOWN:")
    print(f"  Warm-up:     {warmup_dist_km * display_factor:.2f} {unit} @ {warmup_pace_str}/{unit} = {format_time(warmup_time)}")
    print(f"  Intervals:   {num_intervals} x {interval_dist_km * display_factor:.2f} {unit} @ {interval_pace_str}/{unit}")
    print(f"               = {total_interval_dist * display_factor:.2f} {unit} total in {format_time(total_interval_time)}")

    if recovery_type == "distance":
        print(f"  Recovery:    {num_intervals - 1} x {recovery_dist_km * display_factor:.2f} {unit} @ {recovery_pace_str}/{unit}")
        print(f"               = {total_recovery_dist * display_factor:.2f} {unit} total in {format_time(total_recovery_time)}")
    else:
        print(f"  Recovery:    {num_intervals - 1} x {format_time(recovery_time_sec)}")
        print(f"               = {format_time(total_recovery_time)} total")

    print(f"  Cool-down:   {cooldown_dist_km * display_factor:.2f} {unit} @ {cooldown_pace_str}/{unit} = {format_time(cooldown_time)}")

    print()
    print("-" * 60)
    print(f"TOTAL DISTANCE: {total_dist_km * display_factor:.2f} {unit}")
    print(f"TOTAL TIME:     {format_time(total_time)}")
    print(f"AVERAGE PACE:   {format_time(total_time / (total_dist_km * display_factor))}/{unit}")
    print("-" * 60)

    # Generate workout description
    print("\nWORKOUT DESCRIPTION:")
    if recovery_type == "distance":
        recovery_desc = f"{recovery_dist_km * display_factor:.2f}{unit} jog recovery"
    else:
        recovery_desc = f"{format_time(recovery_time_sec)} jog"

    print(f"{warmup_dist_km * display_factor:.1f}{unit} easy warm-up, " +
          f"{num_intervals} x {interval_dist_km * display_factor:.1f}{unit} @ {interval_pace_str}/{unit} " +
          f"({recovery_desc}), " +
          f"{cooldown_dist_km * display_factor:.1f}{unit} easy cool-down")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
