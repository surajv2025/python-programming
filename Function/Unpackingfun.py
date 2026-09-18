def sum(*a):
    s=0
    for x in a:
        s=s+x
    return s

x=sum(12,10,19,56,78)
print(x)
x=sum(12)
print(x)