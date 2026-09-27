ch=input("Enter any char:")
if ord(ch)>=65 and ord(ch)<=90:
    print("UpperCase")
elif ord(ch)>=97 and ord(ch)<=122:
    print("Lowercase")
elif ord(ch)>=48 and ord(ch)<=57:
    print("Numeric case")
else:
    print("Special case")