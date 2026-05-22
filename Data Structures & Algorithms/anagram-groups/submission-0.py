class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict containing a counts families
        families = {}
        for s in strs:
            s_counts = self.encode(s)
            # turn the counts encoding into a tuple so we can 
            # use as a key for the families hash_map
            hash_key = tuple(sorted(s_counts.items()))
            families.setdefault(hash_key, list()).append(s)
        
        sublists = []
        for group in families:
            sublists.append(families[group])
        
        return sublists

    
    def encode(self, s: str) -> Dict[str, int]:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        return counts