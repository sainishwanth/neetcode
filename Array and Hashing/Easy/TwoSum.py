class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap: # o(log(n))
                return [hashMap[diff], i]
            hashMap[n] = i


# O(n^2) Solution
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]