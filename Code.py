class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0

        target = total_sum % p
        prefix_sum = 0
        seen = {0: -1}
        min_length = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            if (prefix_sum - target) % p in seen:
                min_length = min(min_length, i - seen[(prefix_sum - target) % p])
            seen[prefix_sum] = i
        return min_length if min_length < len(nums) else -1
