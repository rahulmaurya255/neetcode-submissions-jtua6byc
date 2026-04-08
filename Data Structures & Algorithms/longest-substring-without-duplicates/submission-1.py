class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        max_s = 0

        for r in range(len(s)):
            if s[r] in char_map:
                l = max(l, char_map[s[r]]+1)

            char_map[s[r]] = r
            max_s = max(max_s, r-l+1)
        return max_s