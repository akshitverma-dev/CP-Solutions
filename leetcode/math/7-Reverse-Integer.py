class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0:
            num = x
            while num > 0:
                ans = ans*10 + num%10
                num = num//10
            if ans > 2147483647:
                return 0
            else:
                return ans
        elif x < 0:
            num = x*(-1)
            while num > 0:
                ans = ans*10 + num%10
                num = num//10
            if ans > 2147483648:
                return 0
            else:
                return ans*(-1)
            
        else:
            return 0

