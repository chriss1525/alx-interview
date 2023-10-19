#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" script that reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict

# Define a dictionary to store status code counts
status_code_counts = defaultdict(int)

# Initialize total file size
total_size = 0

try:
    for line in sys.stdin:
        # Extract relevant data using regex
        match = re.match(
            r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', 
            line)
        if match:
            ip, status_code, file_size = match.groups()
            # Increment status code count
            status_code_counts[int(status_code)] += 1
            # Update total file size
            total_size += int(file_size)

        # Check if 10 lines have been processed, and if so, print the statistics
        if len(status_code_counts) >= 8:
            print(f'Total file size: File size: {total_size}')
            for code in sorted(status_code_counts.keys()):
                print(f'{code}: {status_code_counts[code]}')
            print('---')
            # Reset the status code counts and total size
            status_code_counts = defaultdict(int)
            total_size = 0

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully and print the current statistics
    print(f'Total file size: File size: {total_size}')
    for code in sorted(status_code_counts.keys()):
        print(f'{code}: {status_code_counts[code]}')
