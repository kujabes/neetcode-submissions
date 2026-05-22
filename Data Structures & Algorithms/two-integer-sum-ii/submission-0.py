class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1
        candidate = numbers[idx1] + numbers[idx2]

        while candidate != target:
            # we need higher values, push left pointers
            if candidate < target:
                idx1 += 1
            # need lower values, pull right pointer
            elif candidate > target:
                idx2 -= 1

            candidate = numbers[idx1] + numbers[idx2]
        
        return [idx1 + 1, idx2 + 1]