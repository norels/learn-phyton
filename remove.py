import os

file_path = "file.txt"

if os.path.exist(file_path):
    os.remove(file_path)
else:
    print("file nit exist")

#print(os.path.exist("file.txt"))

#os.remove("file.txt")
