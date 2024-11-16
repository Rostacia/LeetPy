class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        # create a dict to keep track of target and current window
        target = defaultdict(int)
        window = defaultdict(int)
        for char in t:
            target[char] += 1
        
        have, need = 0, len(target)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for  r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in target and window[c] == target[c]:
                have += 1
            
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            
