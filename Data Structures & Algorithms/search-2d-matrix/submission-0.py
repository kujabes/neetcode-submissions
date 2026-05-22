class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.search(row, target)
            
        return False
    
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
                return True
            mid = (low + high) // 2
        
        return False