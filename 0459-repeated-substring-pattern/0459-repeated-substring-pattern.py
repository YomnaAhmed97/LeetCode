class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # Create a string by use of substring starting from 1 to last index and 0th to last             but 1 index.
        # Check if the given string s is present in the above created new string and return             True if present.
        combined="".join((s[1:],s[:-1]))
        return s in combined

        