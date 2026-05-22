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
        suffix = suffix[::-1]

        output = [suffix[1]]
        for i in range(1, len(nums) - 1):
            output.append(prefix[i - 1] * suffix[i + 1])
        output.append(prefix[-2])

        return output       