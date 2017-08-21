# Change the current directory to another directory.
import os;
from create_remove_directory import tryCreateDirectory;
from create_remove_directory import finalDirName;

tryCreateDirectory('test', 1);
os.chdir(finalDirName); # This will change the current directory the move to the provided directory.
print(os.getcwd());
