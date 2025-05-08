class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traversal(self,head):
        self.sum = 0
        while head:
            self.sum += head.val
            head = head.next
        return self.sum

    def getSum(self, head):
        # Using recursion
        if not head:
            return 0
        return head.val + self.getSum(head.next)
    
    def addToEnd(self, prevNode, node):
        if prevNode.next != None:
            print("Sorry, try another approach.")
        prevNode.next = node
    
    def addInBetween(self, prevNode, node):
        node.next = prevNode.next
        prevNode.next = node

    def deleteNode(self, prevNode):
        prevNode.next = prevNode.next.next

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



