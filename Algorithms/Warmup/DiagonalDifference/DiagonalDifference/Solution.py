#!/bin/python3

import sys


n = int(input().strip())
a = []
fDiagonalIndex = 0
fDiagonalTotal = 0
sDiagonalIndex = n - 1
sDiagonalTotal = 0

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    fDiagonalTotal += a_t[fDiagonalIndex]
    sDiagonalTotal += a_t[sDiagonalIndex]

    fDiagonalIndex += 1
    sDiagonalIndex -= 1

total = abs(fDiagonalTotal - sDiagonalTotal)   
print(total)