class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length or not self.head:
            return -1
        cur = self.head
        for i in range(0, index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # self.print_list()
        # print(f"Add at head: {val}")
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            new_head = Node(val, self.head)
            self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # self.print_list()
        # print(f"Add at tail: {val}")
        new_node = Node(val)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # self.print_list()
        # print(f"Add at index {index}: {val}")
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            prev = None
            cur = self.head
            for i in range(0, index):
                prev = cur
                cur = cur.next

            new_node = Node(val, cur)
            prev.next = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # self.print_list()
        # print(f"Delete at index {index}")
        if index < 0 or index >= self.length:
            return

        if self.length == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            for i in range(0, index):
                prev = cur
                cur = cur.next

            if index == self.length - 1:
                prev.next = None
                self.tail = prev
            else:
                prev.next = cur.next
        self.length -= 1

    def __str__(self):
        nums = []
        cur = self.head
        while cur:
            nums.append(str(cur.val))
            cur = cur.next
        nums_str = ",".join(nums)
        return f"[{nums_str}]; length ={self.length}"

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)