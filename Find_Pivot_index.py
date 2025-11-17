# 2025/11/17
# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums) - nums[0]
        if ls == rs : return 0

        for i in range(1, len(nums)) :
            ls = ls + nums[i-1]
            rs = rs - nums[i] 
            if ls == rs : return i
        return -1