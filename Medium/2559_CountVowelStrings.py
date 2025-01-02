#Leetcode Problem 2559
#Author: Radhakrishna Rakesh Gandi
# Updated on January 02, 2025


### tried my below code it is not working for all the testcases
### and learnt a better way to use prefix sum which leades to less time complexity compared to below.

# words = ["abac","bcb","ece","aa","e"]
# #words=['a','e','i']
# queries = [[0,2],[1,4],[1,1]]
# vowels=['a','e','i','o','u','A','E','I','O','U']
# res=[]
# for i in queries:
#     #print("--------------")
#     count=0
#     for j in words[i[0]:i[1]+1]:
#         # print(j)
#         if j[0] and j[-1] in vowels:
#             count+=1
#             #print(j)
#     res.append(count)
# print(res)
        
### efficient solution with O(n) complexity

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix=[0]
        for word in words:
            if word[0]in "aeiou" and word[-1] in "aeiou":
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])
        res=[]
        for x,y in queries:
            res.append(prefix[y+1]-prefix[x])
        return res


### you can rewrite this code in below manner to make it look few lines less compared to above

# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         PS,V = defaultdict(lambda:0),set("aeiou")
#         for idx,word in enumerate(words):
#             PS[idx]=PS[idx-1]+int(word[0 in V and word[-1] in V])
#         return [PS[y]-PS[x-1] for x,y in queries]