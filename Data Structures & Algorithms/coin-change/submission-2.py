class Solution:
    def coinChange(self,coins, amount):
        # Create a memoization dictionary
        memo = {}

        # Helper function to perform the recursion with memoization
        def helper(remaining):
            # Check if we've already computed this state
            if remaining in memo:
                return memo[remaining]
            
            # Base cases
            if remaining == 0:
                return 0  # No coins needed
            if remaining < 0:
                return float('inf')  # Invalid case
            
            min_coins = float('inf')
            
            for coin in coins:
                # Recur for the remaining amount after using one coin
                result = helper(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)  # Count this coin
            
            # Memoize the result
            memo[remaining] = min_coins
            return min_coins

        # Start the recursion
        result = helper(amount)
        return result if result != float('inf') else -1


        