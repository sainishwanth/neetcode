class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # .split() -> Creates a List containing all the strings in the Input String (Ignoring all spaces)
        # [-1] -> Last item in the list of strings
        # len() -> Returns length of the string

        return len(s.split()[-1])


# Non Cheese Solution
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c