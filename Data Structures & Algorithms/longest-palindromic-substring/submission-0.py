class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, a, b = 0, 0, 0
        
        def helper(l, r, tres):
            nonlocal res, a, b
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tres += 2 if l != r else 1  # Increment by 2 for both sides, or 1 for the center character
                l -= 1
                r += 1
            if tres > res:
                res = tres
                a, b = l + 1, r - 1  # Update a and b correctly after expanding

        for i in range(len(s)):
            helper(i, i, 0)      # Odd-length palindromes
            helper(i, i + 1, 0)  # Even-length palindromes
            
        return s[a:b + 1]
