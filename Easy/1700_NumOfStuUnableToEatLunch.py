#Leetcode Problem 1700
#Author: Radhakrishna Rakesh Grandi
# Updated on December 11, 2024

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res=len(students)
        count=Counter(students)
        for i in sandwiches:
            if count[i]>0:
                res-=1
                count[i]-=1
            else:
                return res
        return res
        


## another way of writing the code
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         students_left = len(students)
#         sandwiches_left = len(sandwiches)
#         students_checked = 0
#         while students_left and sandwiches_left:
#             if students[0] == sandwiches[0]:
#                 students.pop(0)
#                 sandwiches.pop(0)
#                 students_left -= 1
#                 sandwiches_left -= 1
#                 students_checked = 0
#             else:
#                 students.append(students.pop(0))
#                 students_checked += 1
            
#             if students_checked >= students_left:
#                 return students_left
#         return students_left