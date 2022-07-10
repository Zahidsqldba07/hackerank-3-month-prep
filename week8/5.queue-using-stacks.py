# Enter your code here. Read input from STDIN. Print output to STDOUT
# create two stack, input and output
# if enqueue (1), push to stack input
# if deq (2), check if length == 0, if yes pop input -> push output, then pop 1 output
# if print(3), check move element, print last element of input

class Queue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def shift_element(self):
        if len(self.output_stack) == 0:
            while len(self.input_stack) > 0:
                self.output_stack.append(self.input_stack.pop())

    def print_queue(self):
        self.shift_element()
        print(self.output_stack[len(self.output_stack) - 1])

    def enqueue(self, x: int):
        self.input_stack.append(x)

    def dequeue(self):
        self.shift_element()
        self.output_stack.pop()


if __name__ == '__main__':
    queue = Queue()
    q = int(input())
    for _ in range(q):
        queries = input().split(' ')
        query_type = queries[0]
        if query_type == '1':
            x = queries[1]
            queue.enqueue(x)
        elif query_type == '2':
            queue.dequeue()
        else:
            queue.print_queue()
