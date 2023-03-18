
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

# get middle value of ll
def getMiddle(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

# return middle elements
def getMiddle(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# remove duplicates
def removeDup(head):
    curr = head
    while curr and curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def reverseList(head):
    prev = None
    curr = head
    while curr:
        c

    
# Given the head of a linked list, determine if the linked list has a cycle.    
def hasCycle(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

# Given the head of a linked list and an integer k, return the kth node from end
def kFromEnd(head,k):
    fast = head
    slow = head
    for _ in range(k):
        fast = fast.next      
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.value

def reverseList(head):
    prev = None
    curr = head
    while(curr):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def swapInPairs():
    pass

one = LinkedNode(1)
two = LinkedNode(2)
three = LinkedNode(3)
head = one
one.next = two
two.next = three

print(head.value)
print(head.next)
print(head.next.value)
print(head.next.next.value)
#s = reverseList(head)
#print(s.next.value)

