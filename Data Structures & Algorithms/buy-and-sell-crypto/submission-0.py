class Solution:
    def maxProfit(self, prices: List[int]) -> int:



        max_profit = 0
        
        for i ,price in enumerate(prices):
            left,right = i,len(prices)-1
            while left<right:
                current_profit=prices[right]-prices[left]
                if current_profit>max_profit:
                    max_profit = current_profit
                right-=1

        return   max_profit 