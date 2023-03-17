
class LinkedNode:
    def __init__(self,val) -> None:
        self.value = val
        self.next = None

def addNodeSL(prev_node,node_to_add):
        node_to_add.next = prev_node.next
        prev_node.next = node_to_add

def deleteNodeSL(prev_node):
    prev_node.next = prev_node.next.next

def get_sumSL(head):
    sum = 0
    dummy = head
    while(dummy!=None):
        sum += dummy.value
        dummy = dummy.next
    return sum

def recursiveSumSl(head):
    if not head:
        return 0
    return head.value + recursiveSumSl(head.next)


one = LinkedNode(1)
two = LinkedNode(2)
three = LinkedNode(3)
head = one
one.next = two
two.next = three

print(head)
print(head.next)
print(head.next.value)
print(head.next.next.value)

addNodeSL(three,LinkedNode(4))
deleteNodeSL(three)
s = recursiveSumSl(head)
print('Sum ',s)
