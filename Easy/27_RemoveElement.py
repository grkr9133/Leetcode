#Leetcode Problem 27
#Author: Radhakrishna Rakesh Grandi
# Updated on December 10, 2024
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ## mycode which occupies extra memory

        # res=[]
        # for i in nums:
        #     if i != val:
        #         res.append(i)
        # nums[:len(res)]=res
        # return(len(res))

        ## code with space of O(1)
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1
        return k

