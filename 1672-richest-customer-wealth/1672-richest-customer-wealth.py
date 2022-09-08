class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(n) for n in accounts ])
        