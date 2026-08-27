class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        for number in nums:
            count = 0
            for other in nums:
                if number > other:
                    count = count + 1
            answer.append(count)
        return answer