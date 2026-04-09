class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        currMin = float("inf")
        for i in range(len(prices)):
            diff = prices[i] - currMin
            if diff > maxDiff:
                maxDiff = diff
            if prices[i] < currMin:
                currMin = prices[i]
        return maxDiff
