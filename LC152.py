class Solution:
    def maxProduct(self, nums):
        mx = mn = ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mx, mn = mn, mx
            mx = max(nums[i], mx * nums[i])
            mn = min(nums[i], mn * nums[i])
            ans = max(ans, mx)
        return ans