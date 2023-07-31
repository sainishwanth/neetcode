class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s) > len(t):
            return False
        while len(s) > 0 and j < len(t):
            if s[0] == t[j]:
                j += 1
                s = s[1:]
                print(s)
            else:
                j += 1
        if s == "":
            return True
        else:
            return False