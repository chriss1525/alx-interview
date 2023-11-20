#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" script that reads stdin line by line and computes metrics"""
import sys
import signal

# Dictionary to store file sizes and status codes
file_sizes = {}
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Variables to keep track of total file size and line count
total_size = 0
line_count = 0

# Function to print statistics


def print_statistics():
    print(f'Total file size: File size: {total_size}')
    for code in sorted(status_codes):
        if code in file_sizes:
            print(f'{code}: {file_sizes[code]}')

# Function to handle keyboard interruption (CTRL + C)


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Parse the line using a simple approach
        parts = line.split()
        if len(parts) >= 10 and parts[8].isdigit():
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes:
                file_sizes[status_code] = file_sizes.get(status_code, 0) + 1

            # Update line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)
