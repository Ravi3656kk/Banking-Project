word ="ram"
with open("r.txt", "r") as f:
      contants = f.read()
contantsnew = contants.replace(word, "vishnu")
with open("r.txt", "w") as f:
      f.write(contantsnew)

with open("r.txt","r") as f:
      for line in f:
            print(line.strip())
f.close()
            