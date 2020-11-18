class DoublyNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def __str__(self):
        return str(self.val)


class DoublyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def getNode(self, index: int):
        cur = self.head
        i = 0
        while cur and i < index:
            cur = cur.next
            i += 1
        return cur

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.getNode(index)
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = DoublyNode(val=val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = DoublyNode(val=val)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        prev_node = self.getNode(index - 1)
        if prev_node is None:
            return
        next_node = prev_node.next
        cur_node = DoublyNode(val=val)
        prev_node.next = cur_node
        cur_node.prev = prev_node
        cur_node.next = next_node
        if next_node:
            next_node.prev = cur_node
        self.size += 1

    def deleteAtHead(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def deleteAtTail(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        # head case
        if index == 0:
            self.deleteAtHead()
            return

        if index == self.size - 1:
            self.deleteAtTail()
            return

        cur_node = self.getNode(index)
        if cur_node is None:
            return

        prev_node = cur_node.prev
        next_node = cur_node.next

        if prev_node:
            prev_node.next = next_node

        if next_node:
            next_node.prev = prev_node

        self.size -= 1

    def print_reverse(self):
        nums = []
        cur = self.tail
        while cur:
            nums.append(str(cur.val))
            cur = cur.prev
        nums_str = ",".join(nums)
        print(f"[{nums_str}]; length ={self.size}")

    def tolist(self, reverse=False):
        l = []
        if reverse:
            cur = self.tail
            while cur:
                l.append(cur.val)
                cur = cur.prev
        else:
            cur = self.head
            while cur:
                l.append(cur.val)
                cur = cur.next
        return l

    def __str__(self):
        nums = []
        cur = self.head
        while cur:
            nums.append(str(cur.val))
            cur = cur.next
        nums_str = ",".join(nums)
        return f"[{nums_str}]; length ={self.size}"


if __name__ == "__main__":
    # ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"]
    # [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
    # 6 4 6 1 2 0 0 4
    lst_obj = DoublyLinkedList()
    lst_obj.addAtHead(1)
    lst_obj.addAtHead(2)
    lst_obj.addAtHead(7)

    lst_obj.addAtTail(7)
    lst_obj.addAtTail(2)
    lst_obj.addAtTail(1)

    print(lst_obj.get(-1))
    print(lst_obj.get(0))
    print(lst_obj.get(1))
    print(lst_obj.get(2))
    print(lst_obj.get(3))
    print(lst_obj.get(4))
    print(lst_obj.get(5))
    print(lst_obj.get(6))
    print(lst_obj)
    lst_obj.print_reverse()

    lst_obj.addAtIndex(6, 100)
    lst_obj.addAtIndex(1, -1)
    lst_obj.addAtIndex(0, -99)
    lst_obj.print_reverse()
    print(lst_obj)
    # delete head
    lst_obj.deleteAtIndex(0)
    # delete middle
    lst_obj.deleteAtIndex(2)
    # delete tail
    lst_obj.deleteAtIndex(7)
    lst_obj.print_reverse()
    print(lst_obj)
    # lst_obj.addAtIndex(3, 0)
    # print(lst_obj)
    # lst_obj.deleteAtIndex(2)
    # print(lst_obj)
    # lst_obj.addAtHead(6)
    # lst_obj.addAtTail(4)
    # print(lst_obj)
    # print(lst_obj.get(4)) #4
    # lst_obj.addAtHead(4)
    # lst_obj.addAtIndex(5, 0)
    # print(lst_obj)
    # lst_obj.addAtHead(6)
    # print(lst_obj.get(1))
    # print(lst_obj, lst_obj.head, lst_obj.tail)
