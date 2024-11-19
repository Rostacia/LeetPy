# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS without Sorting
        # Time: O(n), Space: O(n)
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

                min_column = min(min_column, column)
                max_column = max(max_column, column)

        return [columnTable[x] for x in range(min_column, max_column + 1)]



        # # BFS with Sorting
        # # Time: O(nlogn), Space: O(n)
        # columnTable = defaultdict(list)
        # queue = deque([(root,0)])

        # while queue:
        #     node, column = queue.popleft()

        #     if node is not None:
        #         columnTable[column].append(node.val)
        
        #         queue.append((node.left, column - 1))
        #         queue.append((node.right, column + 1))

        # return [columnTable[x] for x in sorted(columnTable.keys())]