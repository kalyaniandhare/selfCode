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

    def printInorder(self, node):
        if node!= None:
            self.printInorder(node.left)
            print(node.value)
            self.printInorder(node.right)


    def countleafnode(self, node):
        if node is None:
            return 0
        if node.left == None and node.right == None:
            return 1

        else:
            return self.countleafnode(node.left) + self.countleafnode(node.right)




        
def main():
    tree = Tree()
    tree.addNode(tree.root, 10)
    tree.addNode(tree.root, 8)
    tree.addNode(tree.root, 11)
    tree.addNode(tree.root, 6)
    tree.addNode(tree.root, 9)
    tree.addNode(tree.root, 12)

    tree.printInorder(tree.root)
    a = tree.countleafnode(tree.root)
    print(a)
main()
