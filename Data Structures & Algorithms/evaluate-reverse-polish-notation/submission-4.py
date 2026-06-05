from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                op2 = stack.pop()
                op1 = stack.pop()
                
                if token == "+":
                    result = op1 + op2
                elif token == "-":
                    result = op1 - op2
                elif token == "*":
                    result = op1 * op2
                elif token == "/":
                    # Use integer division with truncation towards zero
                    result = int(op1 / op2)
                
                stack.append(result)
            else:
                # Convert token to integer and push onto stack
                stack.append(int(token))
        
        return stack[0]


        
        