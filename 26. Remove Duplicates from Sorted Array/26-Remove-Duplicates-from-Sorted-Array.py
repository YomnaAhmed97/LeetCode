class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Initialize the counter for unique elements
        k =1

        # Traverse the array starting from the second element
        for i in range(1,len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k


        