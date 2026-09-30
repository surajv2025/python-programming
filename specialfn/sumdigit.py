#Q5)WAP TO DEFINE A FUNCTION THAT ACCEPTS A NUMBERS AND 
#returns the sum of its digits.
def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total

num = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(num))