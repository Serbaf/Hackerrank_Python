#!/usr/bin/env python3

def is_leap_year(year):
        if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
                return True
        else:
                return False

n = int(input())
print(is_leap_year(n))
