class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1  
    
nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target), 4)