class Solution:
    def calculate(self, s: str) -> int:
        # Time: O(n), Space: O(1)
        if len(s) == 0: return 0
        currentNumber = lastNumber = result = 0
        sign = '+'

        for i, c in enumerate(s):
           currentChar = c
           if currentChar.isdigit():
            currentNumber = (currentNumber * 10) + int(currentChar)
           if (not currentChar.isdigit() and not currentChar.isspace() or i == len(s) - 1):
            if sign == '+' or sign == '-':
                result += lastNumber
                lastNumber = currentNumber if sign =='+' else -currentNumber
            elif sign == '*':
                lastNumber = lastNumber * currentNumber
            elif sign == '/':
                lastNumber = int(lastNumber / currentNumber)
            sign = currentChar
            currentNumber = 0
        result += lastNumber
        return result
            

        # # Time: O(n), Space: O(n)
        # # if cur char is digit, add it to the num
        # # Otherwise char must be an op and we eval based on type of op
        # # if + or - we must eval exp later based on next op.
        # # So we must store currentNumber to use ltr -> psh to stack
        # # if * or / pop top values from stack an eval cur expression
        # if (len(s) == 0): return 0
        # stack = []

        # currentNumber = 0
        # operation = '+'

        # for i, c in enumerate(s):
        #     currentChar = c
        #     if currentChar.isdigit():
        #         currentNumber = (currentNumber * 10) + int(currentChar)
        #     if (not currentChar.isdigit() and 
        #         not currentChar.isspace() or 
        #         i == len(s) - 1):
        #         if operation == '-':
        #             stack.append(-currentNumber)
        #         elif operation == '+':
        #             stack.append(currentNumber)
        #         elif operation == '*':
        #             stackTop = stack.pop()
        #             stack.append(stackTop * currentNumber)
        #         elif operation == '/':
        #             stackTop = stack.pop()
        #             if stackTop > 0:
        #                 sgn = 1
        #             else:
        #                 sgn =-1
        #             stack.append(sgn*(abs(stackTop) // currentNumber))
        #         operation = currentChar
        #         currentNumber = 0

        # while stack:
        #     stackTop = stack.pop()
        #     currentNumber += stackTop

        # return currentNumber




            

