# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # # Iterative Using Parent Pointers
        # # Stack for tree traversal
        # stack = [root]

        # # Dictionary for parent pointers
        # parent = {root: None}

        # # Iterate until we find both the nodes p and q
        # while p not in parent or q not in parent:

        #     node = stack.pop()

        #     # While traversing the tree, keep saving the parent pointers
        #     if node.left:
        #         parent[node.left] = node
        #         stack.append(node.left)
        #     if node.right:
        #         parent[node.right] = node
        #         stack.append(node.right)

        # # Ancestors set() for node p.
        # ancestors = set()

        # # Process all ancestors for node p using parent pointers.
        # while p:
        #     ancestors.add(p)
        #     p = parent[p]

        # # The first ancestor of q which appears in 
        # # p's ancestor set() is their lowest common ancestor
        # while q not in ancestors:
        #     q = parent[q]
        # return q

        # Recursive Approach
        def recurse_tree(current_node: TreeNode) -> bool:

            # If we've reached the end of a branch, return False.
            if not current_node:
                return False

            # Left recursion
            left = recurse_tree(current_node.left)

            # Right recursion
            right = recurse_tree(current_node.right)

            # If the current not is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        #Traverse the tree  
        recurse_tree(root)
        return self.ans  