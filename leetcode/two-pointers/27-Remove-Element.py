class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tnum = 0 
        for k in nums:
            if k == val:
                tnum +=1
        snum=0
        for i in range(len(nums)-1):
            if i>len(nums)-tnum-1:
                break
            j = len(nums)-1
            if nums[i] == val :
                snum +=1
                while nums[j] == val:
                    j-=1
                nums[i], nums[j] = nums[j], nums[i]
        for m in range(tnum):
            nums.remove(val)
