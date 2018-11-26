#!/usr/bin/env python3

n = int(input())

for row in range(n):
        for column in range(n-row-1):
                print(" ", end="")
        for column in range(row+1):
                print("#", end="")
        print()
