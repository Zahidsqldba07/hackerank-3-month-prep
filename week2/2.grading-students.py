#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# 83, 5 - 83%5 = 2 < 3 , grade = 83 + (2) = 5
# 82, 5- 82%5 = 3 >= 3, grade = 82
# 5 - abs(grade%5 < 3, grade += (5-grade))
# modify array to prevent creating new space

# check if fail, if fail dont change
# if not fail, round using methods above


def gradingStudents(grades: list[int]) -> list[int]:
    for i in range(len(grades)):
        if grades[i] >= 38:
            diff = 5 - abs(grades[i] % 5)
            if diff < 3:
                grades[i] += diff
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
