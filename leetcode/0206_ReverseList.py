from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class SingleLikedList:
    def __init__(self): 
        self.head: ListNode = None
        self.tail = None
    
    def add_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head == None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p

        return new_head
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        p = head
        head = head.next
        node = self.reverseList2(head)
        p.next = node

        return p

if __name__ == '__main__':
    head = [1,2,3,4,5]
    list1 = SingleLikedList()
    for item in head:
        list1.add_item(item)
    
    sol = Solution()
    ans = sol.reverseList2(list1.head)
    
    print("Done.")
