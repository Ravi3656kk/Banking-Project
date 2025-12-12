a = 89
def fun():
      global a
      a = 69
      print(a)
      # Removed the argument to match the function definition
      # fun(a)
      # To avoid infinite recursion, do not call fun() recursively here

fun()
print(a)

