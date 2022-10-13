class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ctr,n=0,len(arr)
        for i in range(n):
            prod=((i+1)*(n-i)+1)//2
            ctr+= prod*arr[i]
        return ctr
        