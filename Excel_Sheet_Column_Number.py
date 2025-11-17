# 2025/11/18
# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = 0
        for i in columnTitle[::-1] :
            m = ord(i)-64
            ans += (m*pow(26, n))
            n+=1
        return ans
