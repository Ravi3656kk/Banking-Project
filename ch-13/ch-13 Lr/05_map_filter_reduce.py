l = [1, 22, 55, 2, 5, 6 ,7]
square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))

# #filter example
# def even(n):
#       if (n%2 ==0):
#             return True
#       return False

# onlyEven = filter(even, range(1, 11))
# print(list(onlyEven))

from functools import reduce

#reduce Example
def sum(a,b):
      return a + b
mul = lambda x,y:x*y

print(reduce(sum, l))