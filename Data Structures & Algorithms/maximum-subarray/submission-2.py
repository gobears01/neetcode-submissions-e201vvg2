class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        currMaxSum = -float('inf')
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > currMaxSum:
                currMaxSum = currSum
            if currSum < 0:
                currSum = 0
        return currMaxSum