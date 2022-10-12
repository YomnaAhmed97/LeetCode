class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Using Stack
        stack = []
        dic = {}
        for i in nums2:
            while(stack and i > stack[-1]):
                a = stack.pop()
                dic[a] = i
            stack.append(i)
        return [dic.get(i, -1) for i in nums1]
            
        