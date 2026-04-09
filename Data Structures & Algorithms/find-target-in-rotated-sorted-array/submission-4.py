class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        minIndex = left
        if minIndex == 0:
            left = 0
            right = len(nums) - 1
        elif nums[minIndex] <= target and nums[-1] >= target:
            left = minIndex
            right = len(nums) - 1
        elif nums[0] <= target and nums[minIndex- 1] >= target:
            left = 0
            right = minIndex- 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1


        