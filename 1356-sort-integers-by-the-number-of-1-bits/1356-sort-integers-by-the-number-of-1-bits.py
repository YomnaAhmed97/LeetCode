class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # return sorted(arr,key=lambda i: (str(bin(i))[2:].count('1'),i))
    
         return sorted(sorted(arr), key=lambda i: bin(i).count('1'))
        
        