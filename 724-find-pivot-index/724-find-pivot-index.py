class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sleft = 0
        sright = 0
        s = sum(nums)
        for i in range (len(nums)):
            s -= nums[i]
            if sleft==s:
                return i
            sleft += nums[i]
        return -1
        
       