class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = (high + low) // 2
        while low <= high:
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
            mid = (low + high) // 2
        
        return -1
            



        