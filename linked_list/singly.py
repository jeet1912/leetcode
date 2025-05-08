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
    
    def addToEnd(self, node1, node):
        if node1.next != None:
            print("Sorry, try another approach.")
        node1.next = node
    
    def addInBetween(self, node1, node):
        node.next = node1.next
        node1.next = node


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
print(two.getSum(head))



