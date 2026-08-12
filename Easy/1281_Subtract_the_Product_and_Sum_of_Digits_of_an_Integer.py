class Solution(object):
    def subtractProductAndSum(self, n):
        digit_sum = 0
        digit_product = 1
        while n>0:
            digit = n % 10
            digit_product = digit_product * digit
            digit_sum = digit_sum + digit 
            n = n // 10
        return digit_product - digit_sum