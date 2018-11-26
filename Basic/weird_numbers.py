#!/usr/bin/env python3

def print_weird():
        print("Weird")

def print_noweird():
        print("Not Weird")

n = int(input())
if (n % 2) != 0:
        print_weird()
elif 2<=n<=5:
        print_noweird()
elif 6<=n<=20:
        print_weird()
elif 20<n:
        print_noweird()
