#Leetcode Problem 1 TwoSum
#Author: Radhakrishna Rakesh Grandi
# Updated on December 01, 2024
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={} #dictionary to store index:value pairs
        for index,number in enumerate(nums):
            if target-number in hash_map:   #finds if diff between target and current number in dictionary
                return (hash_map[target-number],index)     #return index of the difference and the index of current number
            hash_map[number]=index      #else appends the new number to the dictionary with key as index
                