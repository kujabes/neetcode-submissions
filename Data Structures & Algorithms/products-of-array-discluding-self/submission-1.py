class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:1]
        for num in nums[1:]:
            prod = prefix[-1] * num
            prefix.append(prod)
        
        suffix = nums[-1:]
        for num in nums[-2::-1]:
            prod = suffix[-1] * num
            suffix.append(prod)

        output = [suffix[-2]]
        for i in range(1, len(nums) - 1):
            output.append(prefix[i - 1] * suffix[self.flip(len(nums), i + 1)])
        output.append(prefix[-2])

        return output       

    def flip(self, n, index):
        return n - 1 - index