import os 
filename = "2.txt"

if not os.path.exists(filename):
      with open(filename, "w") as f:
            f.write("this is new file created by the program./n ")
      print(f"{filename} cretead.")
      
else:
      print(f"{filename} already exist. no action taken.")

