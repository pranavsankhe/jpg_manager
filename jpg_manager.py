import os
import glob
import shutil
"""This is a simple script used to automate the copy pasting of the .jpg files from a source to destination folder.
If the user selects a path, the script looks for all the .jpg files in its subfolders.""" 

# we use the os module for file related operations such as chdir
# glob is used to search for the files that have a ".jpg" extention
# shutil is used to copy paste the items that are searched by the glob module
# we have made use of the help funtion for each module method funtioning and syntax

print("We would need a file paths to move all the photos from source to destination\n")

path = input ("PLease enter the path of the source file")
destination = input ("Please enter the path of the destination file")

os.chdir(path)
for file in glob.glob("*.jpg"):
    shutil.copy(file, destination)

