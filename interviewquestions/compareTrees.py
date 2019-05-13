class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    #  O(logN) only if the tree is balanced. Can be reduced to O(N) if the tree is unbalanced.
    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)
    
    # O(logN)
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
                print("Removing a node with a single right child... ")
                newNode = node.right
                del node
                return newNode
            elif not node.right:
                print("Removing a node with a single left child... ")
                newNode = node.left
                del node
                return newNode
            print("Removing node with two children... ")
            newNode = self.getPredecessor(node.left)
            node.data = newNode.data
            node.left = self.removeNode(node.data, node.left)
        return node

    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        return None

    # O(logN)
    def getMin(self, node):
        if node.left:
            return self.getMin(node.left)
        return node.data
        
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        return None

    #  O(logN)
    def getMax(self, node):
        if node.right:
            return self.getMax(node.right)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    # O(N)
    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print(f"{node.data} ")
        if node.right:
            self.traverseInOrder(node.right)
    
    def compare(self, other):
        return self.compareTrees(self.root, other.root)
    
    def compareTrees(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if node1.data != node2.data:
            return False
        return self.compareTrees(node1.left, node2.left) and self.compareTrees(node1.right, node2.right)
        

T1 = BinarySearchTree()
T2 = BinarySearchTree()
T2.insert(45)
T2.insert(53)
T2.insert(43)
T2.insert(46)
T1.insert(45)
T1.insert(53)
T1.insert(43)
T1.insert(56)
print(T1.compare(T2))
        
