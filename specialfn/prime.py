#Q4)WAP TO DEFINE A FUNCTION THAT ACCEPTS A NUMBERS AND 
#CHECKS WHETHER IT IS prime number.
def prime(n):
    if n <= 1:
        print("Not a Prime Number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a Prime Number")
                return
        print("Prime Number")

num = int(input("Enter a number: "))
prime(num)