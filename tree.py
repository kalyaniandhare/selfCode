class treeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if node==None:
            self.root = treeNode(value)
        else:
            if value < node.value:
                if node.left == None:
                    node.left = treeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if node.right == None:
                    node.right = treeNode(value)
                else:
                    self.addNode(node.right, value)

    def printInorder(self, node):
        if node != None:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)

    def printPreorder(self, node):
        if node != None:
            print(node.value)
            self.printInorder(node.left)
            self.printInorder(node.right)

    def printPostorder(self, node):
        if node != None:
            self.printInorder(node.left)
            self.printInorder(node.right)
            print(node.value)
                        
        
def main():
    tree = Tree()
    tree.addNode(tree.root, 200)
    tree.addNode(tree.root, 300)
    tree.addNode(tree.root, 100)
    tree.addNode(tree.root, 20)

    tree.printInorder(tree.root)
    tree.printPreorder(tree.root)
            
main()
