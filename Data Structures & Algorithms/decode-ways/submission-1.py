class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        # Initialize dp array with size n + 1
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case for the empty string
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]  # Single digit decoding
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                    dp[i] += dp[i + 2]  # Two digit decoding

        return dp[0]  # Return the total ways to decode the string

        