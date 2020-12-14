class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def max_depth_bottomup(root: TreeNode) -> int:
    # base case, empty tree has a depth of 0
    if not root:
        return 0

    left_depth = max_depth_bottomup(root.left)
    right_depth = max_depth_bottomup(root.right)

    return max(left_depth, right_depth) + 1


def helper(root: TreeNode, depth: int) -> int:
    # leaf node
    if not root.left and not root.right:
        return depth

    left = helper(root.left, depth + 1) if root.left else depth
    right = helper(root.right, depth + 1) if root.right else depth

    return max(left, right)


def max_depth_topdown(self, root: TreeNode) -> int:
    if not root:
        return 0

    answer = self.helper(root, 1)

    return answer
