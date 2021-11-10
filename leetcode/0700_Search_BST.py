from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val: int):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, cur_root: TreeNode, val: int):
        if val < cur_root.val:
            if cur_root.left == None:
                cur_root.left = TreeNode(val)
            else:
                self._insert(cur_root.left, val)
        else:
            if cur_root.right == None:
                cur_root.right = TreeNode(val)
            else:
                self._insert(cur_root.right, val)
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)

        return None

if __name__ == '__main__':
    # root = [4,2,7,1,3], val = 2
    val = 2
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    ans = Solution().searchBST(root, val)
    print("Done.")
