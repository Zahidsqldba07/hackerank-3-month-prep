# Enter your code here. Read input from STDIN. Print output to STDOUT


# 1 -> append W 
# 2 -> del last k element
# 3 -> print(k-1)
# 4 -> undo to last state

# strategy 
# create stack 
# before every ops, store previous state 
# append W, push one by one 
# del last K element, pop k time
# print -> print idx k-1
# undo () -> stack = pre_stack

if __name__ == '__main__':
    Q =  int(input())
    stack, prev_stack = [] , [] 
    for _ in range(Q):
        queries = input().split(' ')
        query_type = queries[0]
        if query_type != '4' and query_type != '3':
            prev_stack.append(list(stack))           
        if query_type == '1':
            w = list(str(queries[1]))
            for char in w:
                stack.append(char)
        elif query_type == '2':
            k = int(queries[1])
            for i in range(k):
                stack.pop()
        elif query_type == '3':
            k = int(queries[1])
            print(stack[k-1])
        else:
            stack = list(prev_stack[-1])
            prev_stack.pop()
