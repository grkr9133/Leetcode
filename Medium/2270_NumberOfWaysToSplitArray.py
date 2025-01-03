#Leetcode Problem 2270
#Author: Radhakrishna Rakesh Gandi
# Updated on January 03, 2025

### the below code is good for most of the testcases
### but if the input size is too high then it throws a time limit exceed error


# nums = [2,3,1,0]
# count=0
# for i in range(len(nums)-1):
#     if sum(nums[:i+1]) >= sum(nums[i+1:]):
#         count+=1
# print(count)

### the better way to do it with O(n) cimplexity is shown below

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_left=0
        sum_right=sum(nums)
        count=0
        for i in range(len(nums)-1):
            sum_left+=nums[i]
            sum_right-=nums[i]
            if sum_left>=sum_right:
                count+=1
        return count