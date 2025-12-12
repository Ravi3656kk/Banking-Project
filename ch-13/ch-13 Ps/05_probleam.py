from functools import reduce
a = [1, 52, 58, 45, 88, 89, 90, 100, 101, 102, 103, 104, 105]

def greater(a, b):
      if(a>b):
            return a
      return b

print(reduce(greater, a))