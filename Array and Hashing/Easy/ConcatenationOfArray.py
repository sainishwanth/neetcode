class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = []
        for _ in range(2):
            for i in nums:
                nums2.append(i)
        return nums2