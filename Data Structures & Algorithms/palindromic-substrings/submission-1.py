class Solution:
    def countSubstrings(self, s: str) -> int:
        #O(n*3) approach
        # res=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         sub=s[i:j+1]
        #         if sub == sub[::-1]:
        #             res+=1
        # return res

        #O(n^2) approach
        res=0
        def helper(l,r):
            nonlocal res
            while l > -1 and r < len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
        return res


        