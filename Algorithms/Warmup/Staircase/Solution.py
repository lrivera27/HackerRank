#!/bin/python3

import sys


n = int(input().strip())
spaces = n - 1


for i in range(n):
    for j in range(n):
        if j >= spaces:
            print('#', end="")
        else:
            print(' ', end="")

    spaces -= 1
    print('')