class Solution(object):
    def countOdds(self, low, high):
        count = 0
        for number in range (low , high + 1):
            if number % 2 == 1:
                 count = count + 1
        return count
   