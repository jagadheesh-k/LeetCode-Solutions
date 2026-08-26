class Solution(object):
    def shuffle(self, nums, n):
        x = nums[:n]
        y = nums[n:]
        answer= []
        for i in range(n):
            answer.append(x[i])
            answer.append(y[i])
        return answer
        