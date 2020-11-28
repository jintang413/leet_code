
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyListRandomPointerIterativeAdditionalMemory:
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            # if visited return cached node
            if node in self.visited:
                return self.visited[node]
            # if not add the node to visited and return
            else:
                self.visited[node] = Node(node.val)
                return self.visited[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':

        # head is null case
        if not head:
            return None

        old_node = head
        new_node = Node(old_node.val)
        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            new_node = new_node.next
            old_node = old_node.next

        return self.visited[head]