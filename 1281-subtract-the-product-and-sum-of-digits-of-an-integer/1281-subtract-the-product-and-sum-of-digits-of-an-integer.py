# class Solution:
    # def subtractProductAndSum(self, n: int) -> int:
        #     Normal iterative
        # prod_ , sum_ = 1 , 0
        # while n:
            # last = n%10 
            # prod_ *= last
            # sum_ += last
            # n = n// 10
        # return prod_ - sum_
# Example:
            
     # n =234
    
          #           1st loop     2nd loop    3rd loop 
             # last =    4            3           2
            # prod =    1*4 = 4      4*3 = 12    12*2 = 24
            # sums =    0+4 = 4      4+3 = 7     7+2 = 9
             # n    =    23           2           0
          # 24 - 9 = 15
#     -------------------------------------------------------------


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return prod((list(map(int,str(n))))) - sum((list(map(int,str(n)))))
    

