#!/usr/bin/python3

import sys
import signal

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")

def process_line(line):
    parts = line.split()
    if len(parts) < 9:
        return
    status_code = parts[8]
    try:
        status_code = int(status_code)
    except ValueError:
        return
    if status_code in status_codes:
        status_codes[status_code] += 1
    file_size = int(parts[7])
    global total_file_size
    total_file_size += file_size
    global line_count
    line_count += 1
    if line_count % 10 == 0:
        print_statistics()

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line.strip())
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
