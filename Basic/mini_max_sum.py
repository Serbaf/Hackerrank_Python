#!/usr/bin/env python3

# Print the minimum and maximum that can be obtained by summing
# all the elements of an array excepting one

number_array = [int(x) for x in input().split(" ")]
number_array.sort()
mini = sum(number_array[0:-1])
maxi = sum(number_array[1:])
print(str(mini)+" "+str(maxi))
