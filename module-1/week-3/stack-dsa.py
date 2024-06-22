class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        # My code is here
        if len(self.__stack) < self.__capacity:
            self.__stack.append(value)
        else:
            print("Stack is full.")

    def pop(self):
        # My code is here
        if not self.is_empty():
            return self.__stack.pop
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def top(self):
        # My code is here
        if not self.is_empty():
            return self.__stack[-1]
        else:
            print("Stack is empty. No top element.")
            return None

# Test Case
stack1 = MyStack(capacity=5)

stack1.push(1)
print(stack1.is_full())
stack1.push(2)
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())



