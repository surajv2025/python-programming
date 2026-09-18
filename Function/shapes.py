def area(l=None,b=None,r=None,s=None,shape=None):
    if shape==None:
        return -1
    elif shape=="Rectangle":
        return l*b
    elif shape=="Square":
        return s*s
    elif shape=="circle":
        return 3.14*r*r
    else:
        return "no any shape is given"
        
x=area()
print(x)
x=area(l=23,b=34, shape="Rectangle")
print(x)
x=area(s=34, shape="Square")
print(x)