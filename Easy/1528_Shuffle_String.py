class Solution(object):
    def restoreString(self, s, indices):
        answer =[""]*len(s)
        for i in range(len(s)):
            answer[indices[i]]= s[i]
        return "".join(answer)
