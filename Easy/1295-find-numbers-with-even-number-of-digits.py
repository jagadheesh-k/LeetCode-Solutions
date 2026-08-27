class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for number in nums:
            text = str(number)
            digit = len(text)
            if digit % 2 == 0:
                count = count + 1
        return count
