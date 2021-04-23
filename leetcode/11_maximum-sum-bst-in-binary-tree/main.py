from sys import maxsize

max_sum = 0

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth_first_traversal(node):
    global max_sum

    if node == None:
        return True, -maxsize, maxsize, 0

    if node.left == None and node.right == None:
        max_sum = max(max_sum, node.val)
        return True, node.val, node.val, node.val

    left_is_bst, left_min, left_max, left_sum = (True, node.val, node.val - 1, 0) if node.left == None else depth_first_traversal(node.left)
    right_is_bst, right_min, right_max, right_sum = (True, node.val + 1, node.val, 0) if node.right == None else depth_first_traversal(node.right)

    is_bst = left_is_bst and right_is_bst and left_max < node.val and right_min > node.val

    if is_bst:
        max_sum = max(max_sum, (left_sum + right_sum + node.val))

    return is_bst, min(left_min, node.val), max(right_max, node.val), (left_sum + right_sum + node.val)

def maxSumBST(root):
    global max_sum
    depth_first_traversal(root)
    return max_sum

r = TreeNode(1, TreeNode(4, TreeNode(2), TreeNode(4)), TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(6))))
print(maxSumBST(r))