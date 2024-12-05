#Leetcode Problem 118
#Author: Radhakrishna Rakesh Grandi
# Updated on December 05, 2024


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            nrow=[]
            for j in range(len(res[-1])+1):
                nrow.append(temp[j]+temp[j+1])
            res.append(nrow)
        return res
    
#another way to save space of apx 1mb
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         res = []
#         for i in range(numRows):
#             row = [1]*(i+1)
#             for j in range(1, i):
#                 row[j] = res[i-1][j-1] + res[i-1][j]
#             res.append(row)
#         return res