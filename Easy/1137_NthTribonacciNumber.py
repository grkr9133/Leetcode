#Leetcode Problem 1137
#Author: Radhakrishna Rakesh Grandi
# Updated on December 04, 2024


class Solution:
    def tribonacci(self, n: int) -> int:
        tf,ts,tt=0,1,1
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n):
            tfi=tf+ts+tt
            tf=ts
            ts=tt
            tt=tfi
        return tt


#another way to reduce space by apx 1mb
# def tribonacci(self, n: int) -> int:
#         # 0, 1, 2, 3, 4
#         # 0, 1, 1, 2, 4, 7, 13, 24, 44
#         result = [0, 1, 1]
#         for x in range(3, n+1):
#             result.append(result[x-3] + result[x-2] + result[x-1])
#         return result[n]