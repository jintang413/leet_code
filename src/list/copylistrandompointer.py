class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyListRandomPointerIterativeAdditionalMemory:
    def __init__(self):
        self.visited = {}

    def get_cloned_node(self, node):
        if node:
            # if visited return cached node
            if node in self.visited:
                return self.visited[node]
            # if not add the node to visited and return
            else:
                self.visited[node] = Node(node.val)
                return self.visited[node]
        return None

    def copy_random_list(self, head: 'Node') -> 'Node':

        # head is null case
        if not head:
            return None

        old_node = head
        new_node = Node(old_node.val)
        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.get_cloned_node(old_node.random)
            new_node.next = self.get_cloned_node(old_node.next)

            new_node = new_node.next
            old_node = old_node.next

        return self.visited[head]


class CopyListRandomPointerRecursive:
    def __init__(self):
        self.visited = {}

    def copy_random_list(self, head: 'Node') -> 'Node':

        # head is null case
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val)
        self.visited[head] = node

        node.random = self.copy_random_list(head.random)
        node.next = self.copy_random_list(head.next)

        return node


class CopyListRandomPointerIterativeNoAdditionalMemory:

    def copy_random_list(self, head: 'Node') -> 'Node':
        # head is null case
        if not head:
            return None

        # create weavered list
        ptr = head
        while ptr:
            new_node = Node(ptr.val)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        # update random pointer
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old
