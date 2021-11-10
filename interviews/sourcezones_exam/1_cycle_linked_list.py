# Linked List Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def find_loop(node):
    index = 0
    values = {}
    
    while (node != None):
        # 判斷是否為走過的Node
        if (node in values.keys()):
            print("tail connects to node index ", values[node])
            return
        # 把Node存進Hash
        else:
            values[node] = index
            index += 1
            node = node.next

    print("no cycle")
    return

if __name__ == '__main__':
    # head = [3,2,0,-4], pos = 1
    first_node = Node(3)
    first_node.next = Node(2)
    first_node.next.next = Node(0)
    first_node.next.next.next = Node(-4)
    first_node.next.next.next.next = first_node.next
    
    #head = [1,2], pos = 0
    # first_node = Node(1)
    # first_node.next = Node(2)
    # first_node.next.next = first_node

    # head = [1], pos = -1
    # first_node = Node(1)
    
    find_loop(first_node)
