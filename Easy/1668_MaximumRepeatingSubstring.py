#Leetcode Problem 1668
#Author: Radhakrishna Rakesh Grandi
# Updated on December 05, 2024

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # count=0
        # l=len(word)
        # for i in range(len(sequence)):
        #     if sequence[i:i+l]==word:
        #         count+=1
        # return count

        # the above code should work but the test case 
        # "aaabaaaabaaabaaaabaaaabaaaabaaaaba"  is expecting 5 "aaaba"
        # while it has 7 "aaaba"


        ## well i got the reason why it is not 7 
        ## it should be a consicutive sequence

        count=0
        while True:
            if word * count not in sequence:
                return count-1
            count+=1