class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            ans = ans + mat[i][i]
            mat[i][i] = 0
            ans =  mat[i][len(mat)-i-1] + ans
        return ans
        