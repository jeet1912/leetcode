from singly import SinglyLinkedList

class Practice:
    
    def getMiddle(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    

l = SinglyLinkedList()
l.append(1)
l.append(2)
l.append(3)

p = Practice()
print(p.getMiddle(l.head))