class Solution(object):
    def maximumWealth(self, accounts):
        count = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > count:
                count = wealth
        return count
                
