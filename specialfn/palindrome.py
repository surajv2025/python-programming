#Q7)WAP TO DEFINE A FUNCTION THAT ACCEPTS A NUMBERS AND 
#CHECKS WHETHER it is an palindrome.
def pali():
    s = input("Enter a string: ")
    i=0
    j=len(s)-1 # len hamesha 1 se chalta h
    while i<j:
        if s[i]!=s[j]:
            print("string not palindrome")
            break
        i=i+1
        j=j-1
    else:
        print("string is palindrome")
pali()