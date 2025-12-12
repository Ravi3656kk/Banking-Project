with open ("this.txt") as f:
      content1 = f.read()

with open("this_copy.txt") as f:
      content2 = f.read()

if(content1 == content2 ):
      print(" yes this file is identical")         

else:
      print("no these file is not identical")