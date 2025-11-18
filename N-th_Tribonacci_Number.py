# 2025/11/18
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        if n <= 2 : return arr[n]
        for _ in range(n-2) :
            (arr[0], arr[1], arr[2]) = (arr[1], arr[2], sum(arr))
        return arr[2]