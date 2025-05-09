from singly import SinglyLinkedList

class Practice:
    
    def getMiddle(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    def hasCycle(self, head) -> bool:
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

l = SinglyLinkedList()
l.append(1)
l.append(2)
l.append(3)

p = Practice()
print(p.hasCycle(l.head))