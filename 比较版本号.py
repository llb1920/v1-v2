#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split(".")
        lst2 = version2.split(".")
        L1 = len(lst1)
        L2 = len(lst2)
        if L1 < L2:
            lst1.extend(["0"]*(L2-L1))
        else:
            lst2.extend(["0"]*(L1-L2))
        L = max(L1, L2)
        for i in range(L):
            if int(lst1[i]) < int(lst2[i]):
                return -1
            if int(lst1[i]) > int(lst2[i]):
                return 1
        return 0
# @lc code=end

