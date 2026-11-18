class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower_bound = mid + 1
            elif nums[mid] > target:
                upper_bound = mid - 1
        return -1