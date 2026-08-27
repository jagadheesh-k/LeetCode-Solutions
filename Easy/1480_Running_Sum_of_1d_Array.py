class Solution(object):
    def runningSum(self, nums):
        answer = []
        count = 0
        for number in nums:
            count = count + number
            answer.append(count)
        return answer