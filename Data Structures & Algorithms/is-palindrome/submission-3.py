class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = ""

        for c in s:
            if c.isalnum():
                char+= c.lower()
        return char == char[::-1]

        