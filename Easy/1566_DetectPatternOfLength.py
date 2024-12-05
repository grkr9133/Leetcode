#Leetcode Problem 1566
#Author: Radhakrishna Rakesh Grandi
# Updated on December 05, 2024


#even below should work
# arr = [2,2]
# m = 1
# k = 2
# n=len(arr)
# for i in range(n-(m*k)):
#     print(arr[i:i+m*k],arr[i:i+m]*k)
#     if arr[i:i+m*k]== arr[i:i+m]*k:
#         print(True)
# print(False)



class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n=len(arr)
        for i in range(n-m):
            if arr[i:i+m*k]== arr[i:i+m]*k:
                return True
        return False
