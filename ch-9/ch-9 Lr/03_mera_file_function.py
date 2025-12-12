try:
    f = open("file.txt", "r")  # open the file in read mode
    line = f.readline()        # read the first line

    while line != "":          # loop until end of file
        print(line.strip())    # print line without extra newline
        line = f.readline()    # read the next line

    f.close()                  # close the file
except FileNotFoundError:
    print("The file 'file.txt' was not found.")
