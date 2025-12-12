# Open and read all lines from the file
with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line.lower():  # case-insensitive search
        print(f"Yes, 'python' is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No, 'python' is not present in any line.")
