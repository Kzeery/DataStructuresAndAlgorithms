class Node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) time complexity
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode

    # O(N) time complexity
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        node = self.head
        while(node.nextNode):
            node = node.nextNode
        node.nextNode = newNode

    def remove(self, data):
        if not self.head:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None
        while(currentNode.data != data):
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def traverseList(self):
        node = self.head
        while node:
            print(f"{node.data} ")
            node = node.nextNode

    # O(1) time complexity
    def getSize(self):
        return self.size

    def reverseList(self):
        if not self.head:
            return None
        root = self.head
        while(root.nextNode):
            node = root.nextNode
            root.nextNode = node.nextNode
            node.nextNode = self.head
            self.head = node
