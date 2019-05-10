class Node():
    def __init__(self, data):
        self.data = data
        self.color = True
        self.right = None
        self.left = None

class LLRB():
    def __init__(self):
        self.root = None
        self.RED = True
        self.BLACK = False
    
    def insert(self, data):
        self.root = self.insertData(self.root, data)
        self.root.color = self.BLACK
    
    def isRed(self, node):
        if not node:
            return False
        return node.color == self.RED

    def insertData(self, node, data):
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insertData(node.left, data)
        elif data > node.data:
            node.right = self.insertData(node.right, data)
        
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.colorflip(node)
        return node



    def colorflip(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x
