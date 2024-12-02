#Leetcode Problem 26 remove duplicates from sorted array
#Author: Radhakrishna Rakesh Grandi
# Updated on December 02, 2024

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myset=set(nums)
        k=len(myset)
        l=list(myset)
        l.sort()
        nums[:len(l)] = l
        return k
    
    # another way of writing the code

        # j=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         nums[j]=nums[i]
        #         j+=1
        # return j
