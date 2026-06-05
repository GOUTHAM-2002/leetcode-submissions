from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize min_price to a very high value
        max_profit = 0  # Initialize max_profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price to the current price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if the current profit is greater
                
        return max_profit


        