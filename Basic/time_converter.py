#!/usr/bin/env python3

# Convert from 12 hour (AM/PM) time representation to a 24-hour 
# representation

time_string = input().strip()
time_mode = time_string[-2:]
time_array = [int(x) for x in time_string[:-2].split(":")]

if time_mode == "AM":
        if time_array[0] == 12:
                time_array[0] -= 12
        else:
                pass
elif time_mode == "PM":
        if time_array[0] == 12:
                pass
        else:
                time_array[0] += 12
print("%02d:%02d:%02d" % (time_array[0], time_array[1], time_array[2]))
