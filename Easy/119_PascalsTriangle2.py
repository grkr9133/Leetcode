#Leetcode Problem 119
#Author: Radhakrishna Rakesh Grandi
# Updated on December 05, 2024


##code traversal
# rowIndex=3
# res=[1]
# for i in range(rowIndex):
#     print("i = "+str(i))
#     res=[0]+res
#     print("before j loop: "+str(res))
#     for j in range(len(res)-1):
#         print("j = "+str(j))
#         res[j]=res[j]+res[j+1]
#         print("after j loop: "+str(res))
# print(res)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            res=[0]+res
            for j in range(len(res)-1):
                res[j]=res[j]+res[j+1]
        return res
        