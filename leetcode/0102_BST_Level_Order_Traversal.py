class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []
        queue = [root]
        output = []
        while queue:
            queue_size = len(queue)
            output_tmp = []
            while queue_size > 0:
                node = queue.pop(0)
                output_tmp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                queue_size-=1
            output.append(output_tmp)

        return output

if __name__ == '__main__':
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # root = [1]
    # root = TreeNode(1)
    
    # root = []
    # root = None
    
    ans = Solution().levelOrder(root)
    print(ans)
