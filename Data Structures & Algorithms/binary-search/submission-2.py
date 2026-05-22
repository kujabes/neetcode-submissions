class Solution:
    def search(self, nums: List[int], target: int) -> int:
        midpoint = len(nums) // 2
        high = len(nums) - 1
        low = 0

        while low <= high:
            # if target is larger than midpoint, search right half
            # by setting low to the midpoint
            if target > nums[midpoint]:
                # we add 1 since we have already checked the midpoint
                low = midpoint + 1
            elif target < nums[midpoint]:
                high = midpoint - 1
            else:
                return midpoint
            
            midpoint = (low + high) // 2
        
        return -1
            



        