#!/usr/bin/python3

import sys
import collections

def main():
    total_size = 0
    status_code_count = collections.defaultdict(int)

    for i, line in enumerate(sys.stdin, 1):
        if i % 10 == 1:
            print("Total file size: File size: %d" % total_size)
            print("Number of lines by status code:", end=" ")
            for status_code, count in sorted(status_code_count.items()):
                print("%s: %d" % (status_code, count), end=" ")
            print()

        fields = line.split()
        if len(fields) != 5:
            continue
        ip_address, _, _, status_code, file_size = fields
        if not all(x.isdigit() for x in (status_code, file_size)):
            continue
        status_code = int(status_code)
        file_size = int(file_size)

        total_size += file_size
        status_code_count[status_code] += 1

    print("Total file size: File size: %d" % total_size)
    print("Number of lines by status code:", end=" ")
    for status_code, count in sorted(status_code_count.items()):
        print("%s: %d" % (status_code, count), end=" ")
    print()

if __name__ == '__main__':
    main()
