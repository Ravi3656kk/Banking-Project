st = "kamala is funniest gyes"
#f = open("myfile.txt","a")
#f.write(st)
#f.close()

#by the help this write a program shortly using of "with statement"
with open("myfile.txt","a")as f:
      print(f.write(st))


# no need to explicity close the file

