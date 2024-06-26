from sys import stdin
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__count = 0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        # Implement the getSize() function
        return self.__count

    def isEmpty(self):
        # Implement the isEmpty() function
        return self.getSize() == 0

    def push(self, data):
        # Implement the push(element) function
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__count += 1

    def pop(self):
        # Implement the pop() function
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def top(self):
        # Implement the top() function
        if self.isEmpty() is True:
            return -1
        data = self.__head.data
        return data


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1