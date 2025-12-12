# a = 1
# b = 2
# c = 3

# def greatest (a,b,c):
#       if (a>b and a>c):
#             return a
#       elif(b>a and b>c):
#             return b
#       elif(c>a and c>b):
#             return c
      
# a = 1
# b = 2
# c = 3      
# print(greatest(a,b,c))

def sum(n):
      if(n==1):
            return 1
      return sum(n-1)+n
print(sum(4))