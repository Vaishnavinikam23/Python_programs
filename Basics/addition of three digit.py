a=int(input("Enter a three digit number:"))
b=a//100
print(b)
c=a%100
d=c//10
print(d)
e=c%10
print(e)
r=b+d*10+e*100
print(r)