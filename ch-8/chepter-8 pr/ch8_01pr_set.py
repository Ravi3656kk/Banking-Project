

def greatest(a,b,c):
     if (a>b and a>c):
          return a
     elif(b>a and b>c):
          return b
     elif(c>b and c>a):
          return c
     
a=4
b=8
c=3
print("the gratest number is :",greatest(a,b,c))