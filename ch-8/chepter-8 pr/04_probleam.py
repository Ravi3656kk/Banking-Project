'''
def print_pattern(n):
      for i in range(n, 0, -1):
            print('*' * i)

print_pattern(3)     
'''
def pattern(n):
      if (n==0):
            return
      print("*" * n)
      pattern(n-1)

pattern(3)

