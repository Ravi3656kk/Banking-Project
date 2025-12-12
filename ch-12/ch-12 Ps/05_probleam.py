n = int(input("enter a number: "))

table = [n*i for i in range(1, 21)]

with open("tables.txt", "w") as f:
    f.write(f"table of {n}: {str(table)} \n")