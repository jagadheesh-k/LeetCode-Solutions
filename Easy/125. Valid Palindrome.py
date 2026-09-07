class Solution(object):
    def isPalindrome(self, s):
        ans = []
        for char in s:
            if char.isalnum():
                ans.append(char.lower())
        ans1 = ans[:]
        ans1.reverse()
        if ans == ans1:
            return True
        else:
            return False