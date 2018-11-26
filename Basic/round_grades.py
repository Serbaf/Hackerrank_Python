#!/usr/bin/env python3

# A program that given an array of grades rounds them according to 
# some stated rules

n = int(input())
grade_array = [int(input()) for _ in range(n)]
rounded_grades = []

for grade in grade_array:
        if (grade < 38) or ((grade % 5) < 3):
                rounded_grades.append(grade)
        else:
                remainder = grade % 5
                rounded_grades.append(grade + (5-remainder))

for rounded_grade in rounded_grades:
        print(str(rounded_grade))
