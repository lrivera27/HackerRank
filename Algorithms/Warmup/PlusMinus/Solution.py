#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positiveCounter = 0
negativeCounter = 0
zeroCounter = 0

for elem in arr:
    if elem > 0:
        positiveCounter += 1
    elif elem < 0:
        negativeCounter += 1
    else:
        zeroCounter += 1

if positiveCounter > 0:
    print(positiveCounter / n)
else:
    print(0)

if negativeCounter > 0:
    print(negativeCounter / n)
else:
    print(0)

if zeroCounter > 0:
    print(zeroCounter / n)
else:
    print(0)
