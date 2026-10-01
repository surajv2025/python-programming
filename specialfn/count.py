#Q10)WAP TO DEFINE A FUNCTION THAT ACCEPTS A NUMBERS
#and returns the count of digits.
def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count
num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))