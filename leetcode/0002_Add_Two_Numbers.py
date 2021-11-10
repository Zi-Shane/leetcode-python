class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        base = 1
        while l1 != None or l2 != None:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            sum += (a * base + b * base)
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            base *= 10
        
        output = ListNode()
        cur_node = output
        condition = True
        while condition == True:
            cur_node.next = ListNode(sum % 10)
            sum = sum // 10
            cur_node = cur_node.next
            if sum == 0:
                condition = False
        
        return output.next

if __name__ == '__main__':
    # l1 = [2,4,3], l2 = [5,6,4]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(7)
    
    ans = Solution().addTwoNumbers(l1, l2)
    print("Done.")
