class Solution:
    def __init__(self):
        self.delCount = 1

    def validPalindrome(self, s: str) -> bool:
        # abc
        # l r
        l, r = 0, len(s) - 1
        

        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                if not self.delCount:
                    return False
                   
                skip_right = s[r-1] == s[l]
                skip_left = s[l+1] == s[r]
                if (skip_left and skip_right):
                    self.delCount -= 1
                    return self.validPalindrome(s[l+1:r+1]) or self.validPalindrome(s[l:r])
                elif skip_right:
                    r -= 1
                elif skip_left:
                    l += 1
                else:
                    return False
                self.delCount -= 1
        return True

    
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
t = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"
#                                              l                 r
print(Solution().validPalindrome(s))