class Solution:
    # Time: O(n), Space: O(1)
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n
        first, second = 0, 1
        for _ in range(2, n + 1):
            first, second = second, first + second
        return second

    ## Time: O(n) Space: O(n)
    # def __init__(self):
    #     self.memo = {0:0, 1:1}

    # def fib(self, n: int) -> int:
    #     if n not in self.memo:
    #         self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
    #     return self.memo[n]

    ## Time: O(2^n), Space: O(n)
    # def fib(self, n: int) -> int:
    #   if n <= 1:
    #       return n
    #   else:    
    #       return self.fib(n - 1) + self.fib(n - 2)