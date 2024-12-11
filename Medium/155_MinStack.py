#Leetcode Problem 155
#Author: Radhakrishna Rakesh Gandi
# Updated on December 11, 2024

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minStack[-1] if self.minStack else val)
        ##simple way of writing avove in multiple stmts
        # if not self.minStack:
        #     self.minStack.append(val)
        # elif self.minStack[-1]<val:
        #     self.minStack.append(self,minStack[-1])
        # else:
        #     self.minStack.append(val)

        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]