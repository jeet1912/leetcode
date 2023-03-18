class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

def addDL(node,node_to_add):
    prev_node = node.prev
    node_to_add.prev = prev_node
    node_to_add.next = node
    prev_node.next = node_to_add
    node.prev = node_to_add

def deleteDL(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
        
def add_to_end(node):
    node.next = tail
    node.prev = tail.prev
    tail.prev.next = node
    tail.prev = node

def remove_from_end():
    if head.next == tail:
        return
    to_remove = tail.prev
    to_remove.prev.next = tail
    tail.prev = to_remove.prev

def add_to_start(node):
    node.prev = head
    node.next = head.next
    head.next.prev = node
    head.next = node

def remove_from_start():
    if head.next == tail:
        return
    to_remove = head.next
    to_remove.next.prev = head
    head.next = to_remove.next
    
def getSumUsingDummy(head):
    ans = 0
    dummy = head
    while(dummy):
        if dummy.val != None:
            ans += dummy.val
        dummy = dummy.next     
    return ans

# With sentinel nodes
head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

add_to_start(one)
addDL(one,two)
add_to_end(three)
s = getSumUsingDummy(head)
print(s)
