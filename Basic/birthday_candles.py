#!/usr/bin/env python3

# Birthday cake candles problem:
# There are n candles, and each one of them has an specific height.
# My niece can only blow the highest candles. How many candles can my
# niece blow out?

input()
candles_array = [int(x) for x in input().split(" ")]
candles_array.sort()
max_height = candles_array[-1]
candle_counter = 1
while candle_counter < len(candles_array) and \
candles_array[-candle_counter-1] == max_height:
        candle_counter += 1
print(candle_counter)
