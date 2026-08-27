class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum =max(candies)
        answer = []
        for kid in candies:
            if (kid + extraCandies) >= maximum:
                answer.append(True)
            else:
                answer.append(False)
        return answer
        