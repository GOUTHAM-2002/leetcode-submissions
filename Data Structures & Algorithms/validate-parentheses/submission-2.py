class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i =='}':
                    if stack.pop() != '{':
                        return False
                elif i ==')':
                    if stack.pop() != '(':
                        return False
                else:
                    if stack.pop() != '[':
                        return False
        return True if not stack else False
        
        