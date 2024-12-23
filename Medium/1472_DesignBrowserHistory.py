#Leetcode Problem 1472
#Author: Radhakrishna Rakesh Gandi
# Updated on December 23, 2024

## using double linked list

class Listnode:
    def __init__(self,val,prev=None,next=None):
        self.val=val
        self.prev=prev
        self.next=next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Listnode(homepage)
        

    def visit(self, url: str) -> None:
        self.curr.next=Listnode(url,self.curr)
        self.curr=self.curr.next
    def back(self, steps: int) -> str:
        while self.curr.prev and steps>0:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps>0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


##using array/list:


class BrowserHistory:
    def __init__(self,homepage:str):
        self.i=0
        self.len=1
        self.history=[homepage]
    def visit(self,url:str)->None:
        if len(self.history)<self.i+2:
            self.history.append(url)
        else:
            self.history[self.i+1]=url
        self.i+=1
        self.len=self.i+1
    def back(self,steps:int)->str:
        self.i=max(self.i-steps,0)
        return self.history[self.i]
    def forward(self,steps:int)->str:
        self.i=min(self.i+steps,self.len-1)
        return self.history[self.i]