class Solution(object):
    def isPalindrome(self,x,y):
        self.s1=x
        self.s2=y
        if x==y:
            print("True")
        else:
            print("False")
t1=Solution()
t1.ispalindrome(121,-121)