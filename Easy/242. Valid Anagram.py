class Solution(object):
    def isAnagram(self, s, t):
        count1 = {}
        count2 = {}
        for char in s:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1
        for char in t:
            if char in count2:
                count2[char] +=1
            else:
                count2[char] = 1
        if count1 == count2:
            return True
        else:
            return False
