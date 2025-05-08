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


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
#print(one.next.val)
print(two.traversal(head=one))



