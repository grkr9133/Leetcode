#Leetcode Problem 217
#Author: Radhakrishna Rakesh Grandi
# Updated on December 06, 2024

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map=set()
        for i in nums:
            if i in map:
                return True
            map.add(i)
        return False