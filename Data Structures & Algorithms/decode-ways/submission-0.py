class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        mem = {}

        def helper(index):
            if index in mem:
                return mem[index]
            if index == n:
                return 1
            if s[index]=='0':
                return 0
            res = helper(index+1)

            if index < n - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] in '0123456')):
                res += helper(index + 2)

            mem[index] = res
            return res
        return helper(0)
        