class Node():
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None
        
class AVL():
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insertNode(data, node.left)
        else:
            node.right = self.insertNode(data, node.right)

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        return self.settleViolation(data, node)
    
    def settleViolation(self, data, node):
        balance = self.calcBalance(node)
        if balance > 1 and data < node.left.data:
            print("Left left heavy situation...")
            return self.rotateRight(node)

        if balance < -1 and data > node.right.data:
            print("Right right heavy situation...")
            return self.rotateLeft(node)

        if balance > 1 and data > node.left.data:
            print("Left right heavy situation... ")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        
        if balance < -1 and data < node.right.data:
            print("Right left heavy situation... ")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    # If the value is greater than 1, left is greater than right and a right rotation must occur. 
    # If the value less then -1, right is greater than left and a left rotation must occur.
    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)
    
    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        
        print(f"{node.data} ")

        if node.right:
            self.traverseInOrder(node.right)

    def rotateRight(self, node):
        print("Rotating to the right on node", node.data)
        tempLeftChild = node.left
        t = tempLeftChild.right

        tempLeftChild.right = node
        node.left = t

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.left), self.calcHeight(tempLeftChild.right)) + 1

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating to the left on node", node.data)
        tempRightChild = node.right
        t = tempRightChild.left

        tempRightChild.left = node
        node.right = t

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.left), self.calcHeight(tempRightChild.right)) + 1

        return tempRightChild
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        else:
            if not node.left and not node.right:
                print("Removing a leaf node... ")
                del node
                return None
            if not node.left:
                print("Removing right child...")
                tempNode = node.right
                del node
                return tempNode
            elif not node.right:
                print("Removing left child...")
                tempNode = node.left
                del node
                return tempNode
            print("Removing node with two children... ")
            tempNode = self.getPredecessor(node.left)
            node.data = tempNode.data
            node.left = self.removeNode(node.data, node.left)
        
        
        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1

        balance = self.calcBalance(node)
        if balance > 1 and self.calcBalance(node.left) >= 0:
            print("Left left heavy situation...")
            return self.rotateRight(node)

        if balance > 1 and self.calcBalance(node.left) < 0:
            print("Left right heavy situation... ")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        

        if balance < -1 and self.calcBalance(node.right) <= 0:
            print("Right right heavy situation...")
            return self.rotateLeft(node)

        
        if balance < -1 and self.calcBalance(node.right) > 0:
            print("Right left heavy situation... ")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node


    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node
