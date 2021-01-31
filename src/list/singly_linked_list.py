class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get_node(self, index: int):
        """

        Args:
            index: index for the node of interest

        Returns: the value of the index-th node if valid else return -1

        """

        cur = self.head
        i = 0
        while cur and i < index:
            cur = cur.next
            i += 1

        if i != index:
            return None
        return cur

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val=val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def get_tail(self):
        cur = self.head
        while cur and cur.next:
            cur = cur.next

        return cur

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        tail = self.get_tail()
        if not tail:
            self.head = new_node
        else:
            tail.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val=val)
            prev_node = self.get_node(index - 1)
            if prev_node:
                new_node.next = prev_node.next
                prev_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0 and self.head:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            cur_node = prev_node.next if prev_node else None
            if prev_node and cur_node:
                prev_node.next = cur_node.next

    def __str__(self):
        nums = []
        cur = self.head
        while cur:
            nums.append(str(cur.val))
            cur = cur.next
        nums_str = ",".join(nums)
        return f"[{nums_str}]; length ={len(nums)}"


if __name__ == "__main__":
    # ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    # [[], [1], [3], [1, 2], [1], [1], [1]]
    lst_obj = SinglyLinkedList()
    lst_obj.addAtHead(1)
    lst_obj.addAtTail(3)
    lst_obj.addAtIndex(1, 2)
    print(lst_obj)
    print(lst_obj.get(1))
    lst_obj.deleteAtIndex(1)
    print(lst_obj.get(1))
