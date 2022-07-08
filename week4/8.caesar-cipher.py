import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# asci table : a-97 z-122
# 0 - 26
# ord(char) - 97 (to make a = 0 and z = 25)
# then (char_int + k)% 26 all char,
# build back using chr()


def caesarCipher(s: str, k: int):
    newCipher = []
    for i in range(len(s)):
        char = chr(97 + ((ord(s[i].lower()) - 97 + k) % 26)
                   ) if s[i].isalpha() else s[i]
        # print(char)
        if char.isalpha():
            newCipher.append(char.upper() if s[i].isupper() else char.lower())
        else:
            newCipher.append(char)
    return ''.join(newCipher)


if __name__ == '__main__':
    # print(caesarCipher('Hello_World!', 4))
    # exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
