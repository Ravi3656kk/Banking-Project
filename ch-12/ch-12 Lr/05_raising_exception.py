try:
    a = int(input("enter a number: "))
    b = int(input("Enter second number:"))
    if b == 0:
        raise ZeroDivisionError("hey your program is not meant to divide numbers by zero")
    print(f"the division a/b is {a/b}")
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError as e:
    print(e)