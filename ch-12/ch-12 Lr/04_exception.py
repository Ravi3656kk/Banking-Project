try:
    a = int(input("hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("aalu ka paratha")

except Exception as e:
    print(e)
    print("Thank you for using the program.")