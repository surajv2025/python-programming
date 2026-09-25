#fibonacci series 0 1 1 2 3 5 8 har pichale no ka addition next no h
n=int(input("Enter value of Term:"))
a=0
b=1
c=a+b
print(a,b,c,end=" ")
for i in range(4,n+1,1):
 a=b
 b=c
 c=a+b
 print(c,end=" ")