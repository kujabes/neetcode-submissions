class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dividor = len(nums)//2
        low = 0
        high = len(nums) - 1

        while low <= high:
            if nums[dividor] < target:
                low = dividor + 1
                dividor = (low + high)//2 
            elif nums[dividor] > target:
                high = dividor -1
                dividor = (low + high)//2
            elif nums[dividor] == target:
                return dividor

        return -1
            



        