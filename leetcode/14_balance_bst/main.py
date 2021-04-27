from math import floor

# Given a binary search tree, return a balanced binary search tree with the same node values.

# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

# If there is more than one answer, return any of them.



# Example 1:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return f"Left: {self.left} -- Val: {self.val} -- Right: {self.right}"

def balanceBST(root):
    sorted_node_list = inOrderTraversal(root, [])
    return balance_nodes_recursively(sorted_node_list, 0, len(sorted_node_list) - 1)


def balance_nodes_recursively(nodes, start_idx, end_idx):
    if start_idx > end_idx:
        return

    middle = floor(start_idx + (end_idx - start_idx) / 2)
    new_root = TreeNode(nodes[middle])

    new_root.left = balance_nodes_recursively(nodes, start_idx, middle - 1)
    new_root.right = balance_nodes_recursively(nodes, middle + 1, end_idx)

    return new_root

def inOrderTraversal(node, arr):
    if node is None:
        return arr

    arr = inOrderTraversal(node.left, arr)
    arr.append(node.val)
    arr = inOrderTraversal(node.right, arr)
    return arr

t = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5)))))

result = balanceBST(t)
print(result)