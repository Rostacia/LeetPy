class Solution:
    def subsets(self, nums):
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # NOT include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

print(Solution().subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]