class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When a single element is considered then its average will be the number itself only.
        if k == 0:
            return nums

        window_size = 2 * k + 1
        n = len(nums)
        averages = [-1] * n

        # If n < window_size, any index  will not have 'k' elements in it's left and right.
        if window_size > n:
            return averages

        # Sliding Window
        # Time: O(n), Space: O(1)
        # FIrst get sum of first window of the 'nums' array.
        window_sum = sum(nums[:window_size])
        averages[k] = window_sum // window_size

        # Iterate on rest indices which have at least 'k' elements
        # on its left and right sides.
        for i in range(window_size, n):
            # We remove the discarded element and add the new element to get current windo sum.
            # 'i' is the index of new inserted element, and
            # 'i - (window_size)' is the index of the last removed element.
            window_sum = window_sum - nums[i - window_size] + nums[i]
            averages[i - k] = window_sum // window_size

        return averages

        # # Prefix Sum
        # # Time: O(n), Space: O(n)
        # # Generate 'prefix' array for 'nums'.
        # # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # # We iterate only on those indices which have atleast 'k' elements in their left and right.
        # # i.e. indices from 'k' to 'n - k'
        # for i in range(k, n - k):
        #     leftBound, rightBound = i - k, i + k
        #     subArraySum = prefix[rightBound + 1] - prefix[leftBound]
        #     average = subArraySum // window_size
        #     averages[i] = average
        
        # return averages