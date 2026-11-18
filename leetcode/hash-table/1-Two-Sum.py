class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        length = range(len(nums))
        for numbers in length:
            if nums[numbers] not in hash_map:
                hash_map[nums[numbers]] = [1, numbers]
            else:
                hash_map[nums[numbers]][0] += 1
                hash_map[nums[numbers]].append(numbers)
        for numbers in length:
            t2 = target - nums[numbers] 
            if t2 != nums[numbers] and hash_map.get(t2) != None:
                return [numbers,hash_map.get(t2)[1]]
            elif t2 == nums[numbers] and hash_map.get(t2) != None :
                if hash_map.get(t2)[0] > 1:
                    return [hash_map.get(t2)[1], hash_map.get(t2)[2]]

                    