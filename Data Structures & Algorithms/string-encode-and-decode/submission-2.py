class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs):
            return ',{}?'.join(strs)
        return 'empty_list'

    def decode(self, s: str) -> List[str]:
        if s == 'empty_list':
            return []
        return s.split(',{}?')