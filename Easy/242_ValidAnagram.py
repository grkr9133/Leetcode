#Leetcode Problem 242
#Author: Radhakrishna Rakesh Grandi
# Updated on December 06, 2024

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## Mycode

        # map_s={}
        # map_t={}
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     map_s[s[i]]=1+map_s.get(s[i],0)
        #     map_t[t[i]]=1+map_t.get(t[i],0)
        # for j in map_s:
        #     if map_s[j]!=map_t.get(j,0):
        #         return False
        # return True


        ## Most Efficient code

        if len(s)!=len(t):
            return False
        for i in set(t):
            if s.count(i)!=t.count(i):
                return False
        return True