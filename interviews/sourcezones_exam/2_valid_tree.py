# Tree Node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def valid_tree(root):
    nums = []
    # inorder走一遍
    traversal(root, nums)

    # 檢查走訪的order是否正確（正確: 小->大）
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return True
    return False

def traversal(node, nums):
    if node == None:
        return
    traversal(node.left, nums)
    nums.append(node.data)
    traversal(node.right, nums)

if __name__ == '__main__':
    # inputs = [5,1,4,None,None,3,6]
    root = Node(5)
    root.left = Node(1)
    root.right = Node(4)
    root.left.left = None
    root.left.right = None
    root.right.left = Node(3)
    root.right.right = Node(6)
    
    # inputs = [2,1,3]
    # root = Node(2)
    # root.left = Node(1)
    # root.right = Node(3)
    
    print(valid_tree(root))
