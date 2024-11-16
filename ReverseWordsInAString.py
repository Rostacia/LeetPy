class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res = " ".join(res[::-1])

        return res