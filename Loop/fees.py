fee=200000
m=int(input("Enter your marks:"))
i=int(input("Enter your income:"))
if m>=90 and i<=300000:
   print("your are eligible for  90% scholorship")
   yf=fee-(fee*90/100)
   print("your fees:",yf) 
elif m>=80 and i<=300000:
    print("your are eligible for  80% scholorship")
    yf=fee-(fee*80/100)
    print("your fees:",yf) 
elif m>=70 and i<=300000:
    print("your are eligible for  50% scholorship")
    yf=fee-(fee*50/100)
    print("your fees:",yf) 
elif m>=60 and i<=300000:
    print("no discount")
else:
     if m>=60:
         print("you are able to get admission without discount")
     else:
         print("you are not eligible")
   