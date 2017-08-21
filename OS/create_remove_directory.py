# We will try to create files from the os module of python and then delete the created one.
import os;

def tryCreateDirectory(dirName, suffix):
    "This method tries to create a directory until a unique name is established."
    try:
        os.mkdir(dirName) # If directory name exists, it will raise an exception, otherwise will create the directory.
    except FileExistsError as e:
        suffix = suffix + 1; # Modifies the name of the directory and calls the method again with the new name.
        tryCreateDirectory(dirName + str(suffix), suffix);
    else:
        global finalDirName; # once the final directory name is established, store it as we have to delete it later.
        finalDirName = dirName;

def tryRemoveDirectory(dirName):
    os.rmdir(dirName);

tryCreateDirectory('test', 1); 
tryRemoveDirectory(finalDirName);