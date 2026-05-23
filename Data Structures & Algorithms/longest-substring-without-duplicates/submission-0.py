class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        substring = ''
        max_length = 0
        for char in s:
            while char in substring:
                visited.discard(char)
                substring = substring[1:]
            else:
                substring = substring + char
                max_length = max(max_length, len(substring))

        return max_length
                

                
