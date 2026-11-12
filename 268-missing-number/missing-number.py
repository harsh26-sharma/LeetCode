class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        arrange_number = sorted(nums)
        low =0
        high = len(arrange_number)
        while low < high:
            mid = (low + high) // 2
            if arrange_number[mid] > mid:
                high = mid
            else:
                low = mid + 1
        return low