from singly import SinglyLinkedList, ListNode

class Practice:
    
    def getMiddle(self,head: ListNode) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
        '''
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
        '''

    def kThEleFromEnd(self, head: ListNode, k:int) -> int:
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val

l = SinglyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.addInBetween(2,4)
l.append(5)
p = Practice()
print(p.kThEleFromEnd(l.head,3))