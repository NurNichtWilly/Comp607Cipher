#delete all .txt files in a directory
import os
import glob

#get all the files in the directory with the .txt extension
files = glob.glob('*.txt')


#explaination: glob.glob('*.txt') gets all the files in the directory with the .txt extension
#list files
print(files)
#ask the user if they want to delete the files
if input("Do you want to delete the files? (y/n): ") == "y":
    for file in files:
        os.remove(file)
        #explanation: os.remove(file) deletes the file
    print("Files deleted")
else:
    print("Files not deleted")