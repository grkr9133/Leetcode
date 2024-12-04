#Leetcode Problem 509
#Author: Radhakrishna Rakesh Grandi
# Updated on December 04, 2024



class Solution:
    def fib(self, n: int) -> int:
        f=0
        s=1
        if n==0:
            return 0
        for i in range(n+1):
            if i==0:
                next=0
            elif i==1:
                next=1
            else:
                next=f+s
                f=s
                s=next
        return next
        

# def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1

#         prev, cur = 0, 1

#         for _ in range(2,n - 1):
#             tmp = cur
#             cur = prev + cur
#             prev = tmp
        
#         return cur