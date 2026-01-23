#!/usr/bin/env python3
"""
Calculate training paces based on target race time and distance.
"""

import argparse
from datetime import timedelta


def parse_time(time_str):
    """Parse time string in format HH:MM:SS or MM:SS to seconds."""
    parts = time_str.split(':')
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        return hours * 3600 + minutes * 60 + seconds
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds
    else:
        raise ValueError("Time must be in format HH:MM:SS or MM:SS")


def seconds_to_pace(seconds):
    """Convert seconds to pace string (MM:SS)."""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}:{secs:02d}"


def calculate_paces(distance_km, time_seconds):
    """
    Calculate training paces based on race performance.

    Threshold pace is calculated using Riegel's formula to estimate a 60-minute effort pace
    (approximately 15K pace), which correctly places it:
    - Faster than race pace for longer races (marathon, half marathon)
    - Slower than race pace for shorter races (5K, 10K)

    Other paces are based on percentage adjustments:
    - Easy: 120-130% of race pace (slower)
    - Steady: 110-115% of race pace
    - VO₂max: Based on 5K pace prediction (faster)
    - Repetition: Based on 3K pace prediction (faster)
    - Race: 100% of race pace
    """
    # Calculate race pace per km
    race_pace_per_km = time_seconds / distance_km

    # Use Riegel's formula (T2 = T1 * (D2/D1)^1.06) to predict equivalent times
    riegel_factor = 1.06

    # Threshold: approximately 60 minutes or 15K pace
    threshold_distance_km = 15.0
    threshold_time = time_seconds * ((threshold_distance_km / distance_km) ** riegel_factor)
    threshold_pace = threshold_time / threshold_distance_km

    # VO2max: approximately 5K pace
    vo2max_distance_km = 5.0
    vo2max_time = time_seconds * ((vo2max_distance_km / distance_km) ** riegel_factor)
    vo2max_pace = vo2max_time / vo2max_distance_km

    # Repetition: approximately 3K pace (shorter than 5K, faster)
    rep_distance_km = 3.0
    rep_time = time_seconds * ((rep_distance_km / distance_km) ** riegel_factor)
    rep_pace = rep_time / rep_distance_km

    # Calculate training paces (in seconds per km)
    paces = {
        'Race': race_pace_per_km,
        'Easy': race_pace_per_km * 1.25,  # 125% (slower)
        'Steady': race_pace_per_km * 1.125,  # 112.5%
        'Threshold': threshold_pace,
        'VO₂max': vo2max_pace,
        'Repetition': rep_pace,
    }

    # Convert to pace ranges for variety
    # Threshold range: ±2% around calculated threshold
    # VO2max range: ±2% around calculated VO2max
    # Repetition range: ±2% around calculated repetition
    pace_ranges = {
        'Easy': (race_pace_per_km * 1.20, race_pace_per_km * 1.30),
        'Steady': (race_pace_per_km * 1.10, race_pace_per_km * 1.15),
        'Threshold': (threshold_pace * 0.98, threshold_pace * 1.02),
        'VO₂max': (vo2max_pace * 0.98, vo2max_pace * 1.02),
        'Repetition': (rep_pace * 0.98, rep_pace * 1.02),
        'Race': (race_pace_per_km, race_pace_per_km),
    }

    return paces, pace_ranges


def format_distance(distance_km):
    """Format distance for display."""
    if distance_km == 5:
        return "5K"
    elif distance_km == 10:
        return "10K"
    elif distance_km == 21.0975:
        return "Half Marathon"
    elif distance_km == 42.195:
        return "Marathon"
    else:
        return f"{distance_km}K"


def main():
    parser = argparse.ArgumentParser(
        description='Calculate training paces based on target race time and distance.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --distance 5 --time 20:00                    # Paces per mile (default)
  %(prog)s --distance 10 --time 45:30
  %(prog)s --distance 21.0975 --time 1:35:00
  %(prog)s --distance 42.195 --time 3:30:00
  %(prog)s -d 5 -t 20:00 --per-km                       # Paces per kilometer
        """
    )

    parser.add_argument(
        '-d', '--distance',
        type=float,
        required=True,
        help='Race distance in kilometers (e.g., 5, 10, 21.0975, 42.195)'
    )

    parser.add_argument(
        '-t', '--time',
        type=str,
        required=True,
        help='Target race time in format HH:MM:SS or MM:SS (e.g., 1:35:00 or 45:30)'
    )

    parser.add_argument(
        '--per-km',
        action='store_true',
        help='Display paces per kilometer instead of per mile (default: per mile)'
    )

    args = parser.parse_args()

    # Parse inputs
    distance_km = args.distance
    time_seconds = parse_time(args.time)

    # Calculate paces
    _, pace_ranges = calculate_paces(distance_km, time_seconds)

    # Convert to per mile by default (unless --per-km is specified)
    conversion_factor = 1.0 if args.per_km else 1.609344
    pace_unit = "km" if args.per_km else "mile"

    # Display results
    print(f"\n{'='*60}")
    print(f"Training Paces for {format_distance(distance_km)} in {timedelta(seconds=time_seconds)}")
    print(f"{'='*60}\n")

    pace_order = ['Easy', 'Steady', 'Threshold', 'VO₂max', 'Repetition', 'Race']

    for pace_type in pace_order:
        min_pace, max_pace = pace_ranges[pace_type]
        min_pace_converted = min_pace * conversion_factor
        max_pace_converted = max_pace * conversion_factor

        if min_pace == max_pace:
            # Race pace - no range
            print(f"{pace_type:12} {seconds_to_pace(min_pace_converted)}/{pace_unit}")
        else:
            print(f"{pace_type:12} {seconds_to_pace(min_pace_converted)} - {seconds_to_pace(max_pace_converted)}/{pace_unit}")

    print(f"\n{'='*60}\n")


if __name__ == '__main__':
    main()
