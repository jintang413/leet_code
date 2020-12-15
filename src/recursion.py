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


def is_tree_symmetric(root: TreeNode) -> bool:
    # empty tree
    if not root:
        return True
    # tree only contains one node
    if not root.left and not root.right:
        return True

    return helper(root.left, root.right)


def helper(left: TreeNode, right: TreeNode) -> bool:
    if left and right and left.val == right.val:
        return helper(left.left, right.right) and helper(left.right, right.left)
    if not left and not right:
        return True
    else:
        return False

def has_path_sum(root: TreeNode, sum: int) -> bool:
    # empty tree
    if not root:
        return False
    # leaf node
    if not root.left and not root.right:
        return sum == root.val

    return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)

def is_univalue(root: TreeNode) -> int:
    # leaf node are all uni_value
    if not root.left and not root.right:
        return True, 1

    count = 0

    left_is_uni = True
    if root.left:
        left_is_uni, left_count = is_univalue(root.left)
        left_is_uni = left_is_uni and root.val == root.left.val
        count += left_count

    right_is_uni = True
    if root.right:
        right_is_uni, right_count = is_univalue(root.right)
        right_is_uni = right_is_uni and root.val == root.right.val
        count += right_count

    # check if current node is univalue
    if left_is_uni and right_is_uni:
        return True, count + 1

    return False, count


def count_unival_subtrees(root: TreeNode) -> int:
    if not root:
        return 0

    _, count = is_univalue(root)

    return count