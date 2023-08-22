#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    cnt_total, cnt_bounded = 0, 0
    window, remaining = n // len(s), n % len(s)

    for idx, ch in enumerate(s):
        if ch == 'a':
            if idx < remaining:
                cnt_bounded += 1

            cnt_total += 1

    return cnt_total * window + cnt_bounded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
