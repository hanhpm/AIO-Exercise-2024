class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def enqueue(self, value):
        if len(self.__queue) < self.__capacity:
            self.__queue.append(value)
        else:
            print("Queue is full. Cannot enqueue more elements.")

    def dequeue(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            print("Queue is empty. Cannot dequeue elements.")
            return None

    def front(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            print("Queue is empty. No front element.")
            return None

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def is_empty(self):
        return len(self.__queue) == 0


# Example usage
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.dequeue())
print(queue1.is_empty())
print(queue1.front())