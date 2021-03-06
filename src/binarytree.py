from typing import List
from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def preorder_traversal_recursive(root: TreeNode) -> List[int]:
    """ root -> left ->  right"""
    res = []
    if not root:
        return res

    res.append(root.val)
    res.extend(preorder_traversal_recursive(root.left))
    res.extend(preorder_traversal_recursive(root.right))

    return res


def preorder_traversal_iterative(root: TreeNode) -> List[int]:
    """ root -> left ->  right
    1) Create an empty stack nodeStack and push root node to stack.
    2) Do following while nodeStack is not empty.
    ….a) Pop an item from stack and print it.
    ….b) Push right child of popped item to stack
    ….c) Push left child of popped item to stack

    Right child is pushed before left child to make sure that left subtree is processed first.
    """
    res = []
    if not root:
        return res

    stack_nodes = []
    stack_nodes.append(root)

    while stack_nodes:
        cur_node = stack_nodes.pop()
        res.append(cur_node.val)
        if cur_node.right:
            stack_nodes.append(cur_node.right)
        if cur_node.left:
            stack_nodes.append(cur_node.left)
    return res


def inorder_traversal_recursive(root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res

    res.extend(inorder_traversal_recursive(root=root.left))
    res.append(root.val)
    res.extend(inorder_traversal_recursive(root=root.right))

    return res


def inorder_traversal_iterative(root: TreeNode) -> List[int]:
    """ left -> root -> right
        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then
             a) Pop the top item from stack.
             b) Print the popped item, set current = popped_item->right
             c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
    """
    res = []
    if not root:
        return res

    stack_nodes = []
    cur = root
    while cur or stack_nodes:

        while cur:
            stack_nodes.append(cur)
            cur = cur.left

        cur = stack_nodes.pop()
        res.append(cur.val)
        cur = cur.right

    return res


def postorder_traversal_recursive(root: TreeNode) -> List[int]:
    """left -> right -> root"""
    res = []
    if not root:
        return res

    res.extend(postorder_traversal_recursive(root.left))
    res.extend(postorder_traversal_recursive(root.right))
    res.append(root.val)

    return res


def postorder_traversal_two_stack(root: TreeNode) -> List[int]:
    """left -> right -> root
        1. Push root to first stack.
        2. Loop while first stack is not empty
           2.1 Pop a node from first stack and push it to second stack
           2.2 Push left and right children of the popped node to first stack
        3. Print contents of second stack
    """
    res = []
    if not root:
        return res

    stack_nodes = []
    stack_final = []
    stack_nodes.append(root)
    while stack_nodes:
        cur = stack_nodes.pop()
        stack_final.append(cur.val)
        if cur.left:
            stack_nodes.append(cur.left)
        if cur.right:
            stack_nodes.append(cur.right)

    while stack_final:
        res.append(stack_final.pop())

    return res


def postorder_traversal_one_stack(root: TreeNode) -> List[int]:
    """left -> right -> root
        1.1 Create an empty stack
        2.1 Do following while root is not NULL
            a) Push root's right child and then root to stack.
            b) Set root as root's left child.
        2.2 Pop an item from stack and set it as root.
            a) If the popped item has a right child and the right child
               is at top of stack, then remove the right child from stack,
               push the root back and set root as root's right child.
            b) Else print root's data and set root as NULL.
        2.3 Repeat steps 2.1 and 2.2 while stack is not empty.
    """
    res = []
    if not root:
        return res

    stack_nodes = []
    cur = root
    while cur or stack_nodes:
        while cur:
            if cur.right:
                stack_nodes.append(cur.right)
            stack_nodes.append(cur)
            cur = cur.left

        cur = stack_nodes.pop()

        if cur.right and peek(stack_nodes) == cur.right:
            stack_nodes.pop()
            stack_nodes.append(cur)
            cur = cur.right
        else:
            res.append(cur.val)
            cur = None

    return res


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return res

    q = deque()
    q.append(root)
    while q:
        level_res = []
        count = len(q)
        while count > 0:
            cur = q.popleft()
            level_res.append(cur.val)
            count -= 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        res.append(level_res)

    return res


def build_tree_inorder_postorder(inorder: List[int], postorder: List[int]) -> TreeNode:
    # create value to index map to provide O(1) access for index, O(n)
    idx_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(left_idx, right_idx):
        if left_idx > right_idx:
            return None

        root = TreeNode(postorder.pop())

        mid_idx = idx_map[root.val]

        root.right = helper(mid_idx + 1, right_idx)
        root.left = helper(left_idx, mid_idx - 1)

        return root

    return helper(0, len(inorder) - 1)


class Node:
    def __init__(self, data, left=None, right=None, next=None):
        self.val = data
        self.left = left
        self.right = right
        self.next = next


def connect_right(self, root: Node) -> Node:
    if not root:
        return root

    q = deque()
    q.append(root)
    while q:
        count = len(q)
        while count > 0:
            cur = q.popleft()
            count -= 1
            if count > 0:
                n_node = q[0]
                cur.next = n_node
                cur.next
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return root


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(root):
            res = []
            # base case
            if not root:
                return ['None']
            else:
                res.append(str(root.val))
                res.extend(helper(root.left))
                res.extend(helper(root.right))
            return res

        return ",".join(helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(nodes):
            if nodes[0] == "None":
                nodes.pop(0)
                return None

            root = TreeNode(nodes.pop(0))
            root.left = helper(nodes)
            root.right = helper(nodes)
            return root

        nodes = data.split(",")
        root = helper(nodes)
        return root
