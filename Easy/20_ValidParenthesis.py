#Leetcode Problem 20
#Author: Radhakrishna Rakesh Grandi
# Updated on December 11, 2024

class Solution:
    def isValid(self, s: str) -> bool:
        match={")":"(","]":"[","}":"{"}
        stack=[]
        for c in s:
            if c in match:
                if stack and stack[-1]==match[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
