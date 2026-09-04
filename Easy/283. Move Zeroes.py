class Solution(object):
    def moveZeroes(self, nums):
        answer1 = []
        answer2 = []
        for i in range(len(nums)):
            if nums[i] == 0:
                answer2.append(nums[i])
            else:
                answer1.append(nums[i])
        nums[:] = answer1 + answer2