import pdb
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            pdb.set_trace()
            if nums[l] == 0:
                if nums[r] == 0:
                    r += 1
                    continue
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r = l + 1

sol = Solution()
sol.moveZeroes([0,1,0,3,12])
