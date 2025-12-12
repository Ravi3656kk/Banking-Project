import os
# slect the drictory whose content you want to list
directory_path = "/"
#use the os module to list the drictory content
contents = os.listdir(directory_path)
# print the content of directory
print(contents)