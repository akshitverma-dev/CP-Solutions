class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for char in nums:
            steps=0
            while char > 0:
                char = char//10
                steps +=1
            if steps %2 ==0:
                ans +=1
        return ans
