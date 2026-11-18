class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower_bound = 0
        upper_bound = num
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound)//2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                upper_bound = mid - 1
            elif mid*mid < num:
                lower_bound = mid + 1
        return False