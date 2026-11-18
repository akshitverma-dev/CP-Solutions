class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # for i in range(len(nums1)-1):
        #     if nums1[i] > nums1[i+1]:
        #         del nums1[i+1:]
        #         break
        # nums1 += nums2
        # nums1.sort()
        # print(nums1)

        del nums1[m:]
        nums1 += nums2
        nums1.sort()
        print(nums1)
        