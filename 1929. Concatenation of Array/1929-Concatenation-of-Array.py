class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums) #Add first Array
        ans.extend(nums) #Add 2nd Array
        return ans

        