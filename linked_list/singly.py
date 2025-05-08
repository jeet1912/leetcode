class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        totalSum = 0
        current = self.head
        while current:
            totalSum += current.val
            current = current.next
        return totalSum

    def getSum(self, head):
        # Using recursion
        if not head:
            return 0
        return head.val + self.getSum(head.next)
    
    def append(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
            print("head.val ",self.head.val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        #print("Current.val ",current.val)
        return
    
    def addInBetween(self, prevVal, val):
        current = self.head
        while current and current.val != prevVal:
            current = current.next
        if not current:
            print(f"Node with val {prevVal} not found.")
        newNode = ListNode(val)
        newNode.next = current.next
        current.next = newNode
        #print("Current.val ",current.val)
        #print("Current.next.val ", current.next.val)
        return

    def delete(self, val):
        if not self.head:
            print("Empy list!")
            return
        current = self.head
        while current and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print(f"Node with val {val} not found.")


singly = SinglyLinkedList()
singly.append(1)
singly.append(2)
singly.append(4)
singly.addInBetween(2,3)
print(singly.traversal())
singly.delete(2)
print(singly.getSum(singly.head))
'''
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
head = one
one.next = two
two.next = three
#print(one.next.val)
three.addToEnd(three,four)
head.addInBetween(three,five)
print(three.next.val)
print(five.next.val)
head.deleteNode(three)
print(three.next.val)
print(four.next)
print(five.next.val)
head.addToEnd(four,five)
five.next = None
print(two.getSum(head))
'''


