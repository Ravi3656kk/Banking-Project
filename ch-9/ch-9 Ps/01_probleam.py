# with open("n.txt", "w") as file:
#       file.write("aman ki bibi bada badmashhai.\n")
# content = file.write

# with open("n.txt", "a") as file:
#       file.write("flowrs representing of softeness of humanity.\n")
#       file.write("humenity always live longs in the worlds!\n")
# file.close()

# with open("n.txt", "r") as file:
#       for line in file:
#             print(line.strip())
# file.close()

with open("n.txt", "r") as file:
      content = file.read()

if "flower" in content:
      print("the word 'flowers' is present in this sentence.")
else:
      print("the word 'flowers' is not available in this sentence.")