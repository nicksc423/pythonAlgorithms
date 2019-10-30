import Node
from typing import Optional

class LinkedList:
    def __init__(self):
        self.root = None # the pointer initially points to nothing

    def getRoot(self) -> Node:
        return self.root

    def getNodeByVal(self, val) -> Optional[Node]:
        return self.root

list = LinkedList()
print(list.getRoot())
