class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat) #rows
        n = len(mat[0]) # columns
        save = []
        for i in mat:
            save+=i
        if m*n != r*c:
            return mat
        else:
            tmp =[]
            for i in range(r):
                tmp.append(save[i*c:i*c+c])
        return tmp
      
