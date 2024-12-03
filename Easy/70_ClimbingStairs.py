#Leetcode Problem 70
#Author: Radhakrishna Rakesh Grandi
# Updated on December 03, 2024

# mycode

class Solution:
    def climbStairs(self, n: int) -> int:
        first,second = 1,1
        for i in range(n-1):
            temp=first
            first=first+second
            second=temp
        return first
    

# another way to save a bit of space

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         a, b = 1, 2
#         for i in range(3, n + 1):
#             a, b = b, a + b
#         return b