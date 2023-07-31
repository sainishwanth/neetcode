class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        minj = 0
        comp = strs[0]
        # Getting the intital value of minj by comparing the first two strings
        for i in range(len(strs[0])):
            if i < len(strs[1]):
                if strs[0][i] == strs[1][i]:
                    minj += 1
                else:
                    break
        # Updating minj as we go
        for Str in strs[2:]:
            j = 0
            while j < len(Str) and j < len(comp):
                print(comp[j], Str[j],j, minj)
                if comp[j] == Str[j]:
                    j += 1
                else:
                    break
            minj = min(minj, j)
        return comp[0:minj]