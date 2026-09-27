u=int(input("Enter Unit"))
if u<=125:
    bill=0.00
elif u<=200:
    bill=(u-125)*8.50
elif u<=250:
    bill=75*8.50+(u-200)*10.50
else:
    bill=(u-125)*10.50
bill=bill+100+450
sub=bill*10/100
print("Meter Rent=",100)
print("EC=",450)
print("Gov Sub=",sub)
print("Your Bill=",bill-sub)