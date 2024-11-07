class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP
    
print(Solution().maxProfit([7,1,5,3,6,4]),5)