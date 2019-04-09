class treenode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:

    
    
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if node == None:
            self.root = treenode(value)
        else:
            if value < node.value:
                if node.left == None:
                    node.left = treenode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if node.right == None:
                    node.right = treenode(value)
                else:
                    self.addNode(node.right, value)
                    

    def printPreorder(self, node):
        if node!= None:
            print(node.value)
            self.printPreorder(node.left)
            self.printPreorder(node.right)

    def printInorder(self, node):
        if node!=None:
            print(node.value, '1')
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)

    def printPostorder(self, node):
        if node!=None:
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print(node.value)

    def heightoftree(self, node):
        if node == None:
            return 0
        else:
            return max(self.heightoftree(node.left), self.heightoftree(node.right)) + 1

    def levelorder(self, node, l):
        if node != None:
            l.append(node.value)
        if node.left != None:
            #l.append(node.left.value)
            self.levelorder(node.left, l)
        if node.right!= None:
            #l.append(node.right.value)
            self.levelorder(node.right, l)


def main():
    l = []
    tree = Tree()
    tree.addNode(tree.root, 20)
    tree.addNode(tree.root, 10)
    tree.addNode(tree.root, 30)
    tree.addNode(tree.root, 8)
    tree.addNode(tree.root, 11)
    tree.addNode(tree.root, 25)
    
    tree.printInorder(tree.root)
    val1 = tree.heightoftree(tree.root)
    tree.levelorder(tree.root, l)
    print(val1, l)
main()
        
