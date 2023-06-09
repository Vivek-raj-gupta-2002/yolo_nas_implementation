class TreeNode:
    def __init__(self, val = None, right = None, left = None) -> None:
        self.val = val
        self.right = right
        self.left = left

    def __str__(self) -> str:
        return str({'val':self.val,'left':str(self.left),'right':str(self.right)})


class BST(TreeNode):
    def __init__(self, val=None) -> None:
        super().__init__(val)
        self.root__ = self

    def add_node(self, val: int) -> None:
        
        node = self.root__

        if not node.val:
            self.root__.val = val
            return

        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    
                    break
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    
                    break
                else:
                    node = node.left
    

    def __add__(self, val):

        self.add_node(val)
        return self
    
    def __len__(self):
        if not self.root__:
            return 0
        return 1 + len(self.right) + len(self.left)



a = BST(12)
print(len(a))




