class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexesToRemove = set() # keep track of closing parenthesis with no open prior
        stack = [] # keep track of open parentheses

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            else:
                if not stack:
                    indexesToRemove.add(i)
                else:
                    stack.pop()
        
        indexesToRemove = indexesToRemove.union(set(stack))
        stringBuilder =[]
        for i, c in enumerate(s):
            if i not in indexesToRemove:
                stringBuilder.append(c)
        
        return "".join(stringBuilder)
