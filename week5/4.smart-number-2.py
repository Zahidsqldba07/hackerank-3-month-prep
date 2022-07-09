import math

# factor always come in pair,
# if there's square factor, then there' pair that has the same number(only counted as 1)
# thus the total factor will be odd and is a magic number

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



