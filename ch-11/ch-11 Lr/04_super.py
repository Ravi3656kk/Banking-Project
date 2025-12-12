class employee:
      def __init__(self):
            print("constructor of employee")
      a = 100

class programmer(employee):
      def __init__(self):
            print("constructor of programmer")
      b = 22

class manager(programmer):
      def __init__(self):
            super().__init__()
            print("constructor of manger")
      c = 300

# o = employee() #print the attribute
# print(o.a) #sho ad error as there is no b attribute is not 

# o = programmer()
# print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)
