#Leetcode Problem 1929
#Author: Radhakrishna Rakesh Grandi
# Updated on December 10, 2024

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums

        #another way of writing it
        #  ans = []
        # for i in range(2):
        #     for num in nums:
        #         ans.append(num)
        # return ans
        
