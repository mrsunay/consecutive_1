"""Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3."""




class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = -1
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_ones, prev = max(max_ones, i-prev-1), i
        if len(nums) and nums[-1] == 1:
            max_ones = max(max_ones, len(nums)-prev-1)
        return max_ones
