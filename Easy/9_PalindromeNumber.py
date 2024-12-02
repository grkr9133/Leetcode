#Leetcode Problem 9 Palindrome Number
#Author: Radhakrishna Rakesh Grandi
# Updated on December 02, 2024

# best code 

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return f"{x}" == f"{x}"[::-1]

# My code

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            string = str(x)
            if string == string[::-1]:
                return True
            else:
                return False