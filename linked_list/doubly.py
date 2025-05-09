class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(None)  
        self.tail = ListNode(None)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_end(self, node_to_add):
        node_to_add.next = self.tail
        node_to_add.prev = self.tail.prev
        self.tail.prev.next = node_to_add
        self.tail.prev = node_to_add

    def remove_from_end(self):
        if self.head.next == self.tail: 
            return
        node_to_remove = self.tail.prev
        node_to_remove.prev.next = self.tail
        self.tail.prev = node_to_remove.prev

    def add_to_start(self, node_to_add):
        next_node = self.head.next
        node_to_add.prev = self.head
        node_to_add.next = next_node
        next_node.prev = node_to_add
        self.head.next = node_to_add

    def remove_from_start(self):
        if self.head.next == self.tail:  
            return
        node_to_remove = self.head.next
        node_to_remove.next.prev = self.head
        self.head.next = node_to_remove.next

    def get_sum(self):
        ans = 0
        current = self.head.next  
        while current != self.tail:  
            ans += current.val
            current = current.next
        return ans


dll = DoublyLinkedList()

one = ListNode(1)
dll.add_to_start(one)
two = ListNode(2)
dll.add_to_end(two)
three = ListNode(3)
dll.add_to_end(three)


print(dll.get_sum())  


dll.remove_from_start()
print(dll.get_sum())  
dll.remove_from_end()
print(dll.get_sum())  