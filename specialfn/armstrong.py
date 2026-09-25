n=int(input("Enter number: "))
order=len(str(n))
sum=0
temp=n
while temp>0:
     sum+= (temp%10)**order
     temp//=10
print("Armstrong" if sum==n else "Not Armstrong")