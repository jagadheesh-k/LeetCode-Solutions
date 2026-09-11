class Solution(object):
    def majorityElement(self, nums):
        for i in range (len(nums)):
            if nums.count(nums[i]) > len(nums) / 2:
                return nums[i]
        