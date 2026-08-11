class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        count = 1
        while count <= n:
            if count %3 == 0 and count %5 == 0:
                answer.append("FizzBuzz")
            elif count %3 == 0:
                answer.append("Fizz")
            elif count %5 == 0:
                answer.append( "Buzz")
            else:
                answer.append(str(count))

            count = count+1

        return answer 