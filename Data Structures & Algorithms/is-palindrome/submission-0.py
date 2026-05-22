class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned_str == cleaned_str[::-1]