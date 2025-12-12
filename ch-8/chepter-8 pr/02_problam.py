def f_c(f):
      return 5*(f-32)/9
f = int(input("enter the temprature in F: "))
c = f_c(f)
print(f"{round(c,2)} °C")