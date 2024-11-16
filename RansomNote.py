class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False

        # rMap = collections.Counter(ransomNote)
        mMap = collections.Counter(magazine)
        
        for c in ransomNote:
            if mMap[c] <= 0:
                return False
            mMap[c] -= 1
        
        return True
        
        # rMap = defaultdict(int)
        # mMap = defaultdict(int)

        # for c in ransomNote:
        #     rMap[c] += 1

        # for c in magazine:
        #     if c in rMap.keys():
        #         mMap[c] += 1
    
        # for key in rMap:
        #     if rMap[key] > mMap[key]:
        #         return False
        # return True