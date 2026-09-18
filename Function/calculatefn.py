def calc(a,b,op='+'):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='//':
        return a//b
    else:
        print("op has invalid value")

x=calc(12,10)
print(x)
x=calc(12,10,op='*')
print(x)
x=calc(12,30,22)