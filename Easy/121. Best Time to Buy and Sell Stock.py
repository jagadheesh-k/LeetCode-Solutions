class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        best_profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            profit = prices[i] - minimum
            if profit > best_profit:
                best_profit = profit
        return best_profit