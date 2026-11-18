class Solution:
    def mySqrt(self, x: int) -> int:
        lower_bound = 0
        upper_bound = x
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound)//2
            print(mid)
            if mid*mid <= x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    lower_bound = mid + 1
            else:
                upper_bound = mid-1
