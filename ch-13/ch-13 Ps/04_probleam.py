#filter function to filter elements divisible by 5 from a list
def divisible5(n):
      if (n%5== 0):
            return True
      return False

a = [1,5,5,8,855,150,75]

f = list(filter(divisible5, a))
print(f)


