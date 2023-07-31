class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        for _ in range(numRows-1):
            n = len(lst[-1]) + 1
            lst2 = [0 for _ in range(n)]
            lst2[0], lst2[-1] = 1, 1
            for i in range(1,n-1):
                lst2[i] = lst[-1][i-1] + lst[-1][i]
            lst.append(lst2)
        return lst