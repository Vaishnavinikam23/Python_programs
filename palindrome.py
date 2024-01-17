class Solution(object):
    def isPalindrome(self,x):
        s1=''
        s2=s1[:1]
        if s1==s2:
            print("True")
        else:
            print("False")
t1=Solution(121)
t2=Solution(-121)
t3=Solution(10)
t1.isPalindrome()
t2.isPalindrome()
t3.isPalindrome()