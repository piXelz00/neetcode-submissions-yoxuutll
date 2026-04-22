class Solution:
    def maxProfit(self, prices) :
        max_profit = 0

        for i ,price in enumerate(prices):
            print(i)
            left,right = i,len(prices)-1
            while left<right:
                while prices[left]>prices[right]:
                    right-=1
                else:
                    current_profit=prices[right]-prices[left]
                    print(current_profit)
                    if current_profit>max_profit:
                        max_profit = current_profit
                    right-=1


        return   max_profit