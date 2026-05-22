class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        candidate = tuple(sorted([nums[i], nums[j], nums[k]]))
                        print(candidate)
                        if candidate not in seen:
                            seen.add(candidate)
                            res.append([nums[i], nums[j], nums[k]])

        return res
            
