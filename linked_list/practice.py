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
    
    def swapInPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = head.next               
        prev = None                     
        while head and head.next:
            if prev:
                prev.next = head.next   
            prev = head                 
            next_node = head.next.next  
            head.next.next = head       
            head.next = next_node     
            head = next_node            
        return dummy
    
    def maxTwinSum(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        curr = mid
        prev = None
        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode
        maxSum = 0
        while prev:
            maxSum = max(maxSum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return maxSum
    
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        first = prev.next
        curr = first.next

        for _ in range(right - left):
            nextNode = curr.next
            curr.next = prev.next
            prev.next = curr
            first.next = nextNode
            curr = nextNode

        return dummy.next

            

l = SinglyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
p = Practice()
print(p.reverseBetween(l.head.next,2,4))