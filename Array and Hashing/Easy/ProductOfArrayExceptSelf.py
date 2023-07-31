#!/usr/bin/env python3

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        Prod = 1
        for num in nums:
            print(num)
            Prod *= num
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] == 1:
                nums[i] = Prod
            else:
                nums[i] = int(Prod/nums[i])

        return nums

Sol = Solution()
print(Sol.productExceptSelf([-1,1,0,-3,3]))
