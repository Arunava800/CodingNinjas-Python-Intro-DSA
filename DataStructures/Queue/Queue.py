"""
---------------------Queue Implementation----------------------------------------
"""


class Queue:
    def __init__(self):
        self.__array = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, data):
        self.__array.append(data)
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            return -1
        element = self.__array[self.__front]
        self.__front += 1
        self.__count -= 1
        return element

    def front(self):
        if self.__count == 0:
            return -1
        return self.__array[self.__front]

    def size(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
while q.is_empty() is False:
    print(q.front())
    q.dequeue()
print(q.dequeue())
