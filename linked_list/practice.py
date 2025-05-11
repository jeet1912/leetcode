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

    def getMiddle2(self, head: ListNode) -> int:    
        slow = fast = head  
        length = 0
        while fast:
            length += 1
            fast = fast.next
        print("length ", length)
        for _ in range(length // 2): 
            slow = slow.next
        return slow.val 
    '''
        slow = fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    '''

    def deleteDuplicatesAscendingOrder(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next #edge case [1,1,1]
        return curr
    
    def reverse(self, head:ListNode) -> ListNode:
        prev = ListNode(None)
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
                
l = SinglyLinkedList()
'''
l.append(1)
l.append(2)
l.append(3)
l.addInBetween(3,4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
'''
l.append(1)
l.append(1)
l.append(2)
l.append(3)
l.append(3)
p = Practice()
print(p.deleteDuplicates(l.head.next))
print(l.getSum(l.head.next))