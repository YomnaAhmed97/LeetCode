from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rNote_counter , maga_counter = Counter(ransomNote), Counter(magazine)
        for i in ransomNote:
            if rNote_counter[i] > maga_counter[i]:
                return False
        return True