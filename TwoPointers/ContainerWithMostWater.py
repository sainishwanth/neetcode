class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res

sol = Solution()
print(sol.maxArea([1,2,3,4,5]))
