class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0, 0
        curr = 0
        maxSum = nums[0]
        for right in range(len(nums)):
            if curr < 0:
                left = right
                curr = 0
            curr += nums[right]
            maxSum = max(curr, maxSum)
        return maxSum

