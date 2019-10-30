from TreeNode import TreeNode

class BTree(object) :
        def __init__(self):
            self.root = None

        def add(self, val: int):
            if self.root == None:
                self.root = TreeNode(val)
            else:
                self._add(self.root, val)

        def _add(self, node, val):
            if(val < node.val):
                if(node.left != None):
                    self._add(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if(node.right != None):
                    self._add(val, node.right)
                else:
                    node.right = TreeNode(val)

        def find(self, val):
            if (self.root != None):
                return self._find(self.root, val)
            else:
                return None

        def _find(self, node, val):
            if node == None:
                return None
            if val == node.val:
                return node
            elif val < node.val:
                self._find(node.left, val)
            else:
                self._find(node.right, val)


        def inOrderTraversal(self):
            if self.root == None:
                print ("Empty")
            else:
                self._inOrderTraversal(self.root)

        def _inOrderTraversal(self, node):
            if node == None:
                return
            self._inOrderTraversal(node.left)
            print(node.val)
            self._inOrderTraversal(node.right)

        def preOrderTraversal(self):
            if self.root == None:
                print ("Empty")
            else:
                self._preOrderTraversal(self.root)

        def _preOrderTraversal(self, node):
            if node == None:
                return
            print(node.val)
            self._preOrderTraversal(node.left)
            self._preOrderTraversal(node.right)

        def postOrderTraversal(self):
            if self.root == None:
                print ("Empty")
            else:
                self._preOrderTraversal(self.root)

        def _postOrderTraversal(self, node):
            if node == None:
                return
            self._postOrderTraversal(node.left)
            self._postOrderTraversal(node.right)
            print(node.val)

        def getMaxDepth(self) -> int:
            if self.root != None:
                return self._getMaxDepth(self.root)
            else:
                return 0

        def _getMaxDepth(self, node) -> int:
            if node == None:
                return 0

            leftDepth = self._getMaxDepth(node.left)
            rightDepth = self._getMaxDepth(node.right)
            if(leftDepth > rightDepth):
                return leftDepth+1
            else:
                return rightDepth+1




tree = BTree()
tree.add(20)
tree.add(15)
tree.add(10)
tree.add(17)
tree.add(25)
print(tree.getMaxDepth())
