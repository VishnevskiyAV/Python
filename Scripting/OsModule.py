import os

print(os.getcwd()) # get the directory you work in
#Use \\ for directoris
os.chdir("D:\\New folder") # Change and create new folder
os.mkdir("path") # create new folder
os.rmdir ("path") # delete folder
os.remove("path") # delete file
print(os.path.join("current_path", "new_directory_path\\file_name")) # Join the current file to a new directory
print(os.path.split("path")) # split the path into two parts, first is directory, second is the last directory in path
print(os.path.exists("path")) # return boolen if folder exist or not