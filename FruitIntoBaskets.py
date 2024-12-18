class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        l = 0
        maxF = 1
        fruitBask = {}
        fruitBask[fruits[l]] = 1

        for r in range(1, len(fruits)):
            fruitBask[fruits[r]] = fruitBask.get(fruits[r], 0) + 1

            while len(fruitBask) > 2:
                fruitBask[fruits[l]] -= 1
                if fruitBask[fruits[l]] == 0:
                    del fruitBask[fruits[l]]
                l += 1
            maxF = max(maxF, 1 + r - l)
        return maxF
       
        # if not fruits:
        #     return 0
        # l = 0
        # maxF = 0
        # fruitBask = defaultdict(int)

        # for r in range(len(fruits)):
        #     fruitBask[fruits[r]] += 1

        #     while len(fruitBask) > 2:
        #         fruitBask[fruits[l]] -= 1
        #         if fruitBask[fruits[l]] == 0:
        #             del fruitBask[fruits[l]]
        #         l += 1
        #     maxF = max(maxF, 1 + r - l)
        # return maxF