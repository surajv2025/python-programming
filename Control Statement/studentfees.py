fee=200000
m=int(input("Enter marks:"))
income=int(input("Enter Income:"))
if m>=90 and income<=300000:
    print("You are able to get 90% schloorship")
    yf=fee-(fee*90/100)
    print("Your Fee=",yf)
elif m>=80 and income<=300000:
    print("You are able to get 80% schloorship")
    yf=fee-(fee*80/100)
    print("Your Fee=",yf)
elif m>=70 and income<=300000:
    print("You are able to get 50% schloorship")
    yf=fee-(fee*50/100)
    print("Your Fee=",yf)
elif m>=60 and income<=300000:
    print("Sorry No any Discount able")
    print("Your Fee=",fee)
else:
    if m>=60:
        print("You are able to get admission without discount")
    else:
        print("You are not able for admission")