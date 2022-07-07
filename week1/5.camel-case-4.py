import sys

# Parse the data, strip (), split(;)
# operation = S(split), C(Combine)
# type  = M(method), C(class), V(variable)

# if split:
# make first char always lower
# loop char, if isUpper(), store into list of substring
# join(' ')

# if Combine
# split(' ') into array of substring
# append with first char make toUpper()
# if type == M, add () in the end
# if type == C, isUpper at first index
# if type == V, normal


def convert(operation: str, type: str, string: str) -> str:
    offset = 0
    if operation == 'S':
        result = []
        for i in range(len(string)):
            if i == 0:
                continue
            else:
                if i == len(string) - 1:  # end of string
                    result.append(string[offset:i+1].lower())
                if string[i].isupper():
                    result.append(string[offset:i].lower())
                    offset = i
        return ' '.join(result)
    else:  # operation combine
        substrings = string.split(' ')
        for i in range(len(substrings)):
            if i == 0:
                substrings[i] = (substrings[i][0].upper(
                ) + substrings[i][1:] if type == 'C' else substrings[i])
            else:
                substrings[i] = substrings[i][0].upper() + substrings[i][1:]
        res = ''.join(substrings) + ('()' if type == 'M' else '')
        return res


while(True):
    try:
        inp = input().rstrip().strip('()').split(';')
        operation, type, string = inp
        print(convert(operation, type, string))
    except:
        break
