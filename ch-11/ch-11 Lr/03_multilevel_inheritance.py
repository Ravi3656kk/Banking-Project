class employee:
      a = 100

class programmer(employee):
      b = 22

class manager(programmer):
      c = 300

o = employee() #print the attribute
print(o.a) #sho ad error as there is no b attribute is not 

o = programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)
