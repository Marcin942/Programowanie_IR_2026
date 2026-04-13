import sys

'''
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

Stack is a data type that serves as a collection of elements with two main operations:

Push, which adds an element to the collection, and
Pop, which removes the most recently added element.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack: #jeśli w stosie są elementy
            last = self.stack[-1]
            self.stack = self.stack[:-1]
            return last
        else:
            return None
    
s = Stack()

for arg in sys.argv[1:]:
    s.push(float(arg))

while s.stack: #dopóki stos nie jest pusty
    print(s.pop())