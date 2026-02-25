"""
## Magic methods. task
***
Create a context manager `TempDir` (Use Context Manager protocol - methods `__enter__`, `__exit__`):
1. When entering the context, a new temporary directory is created with random, unique name.
   Use `os.mkdir` to create the directory.
2. Until exiting this context the new created directory becomes current one and all actions are executed
   in scope of this new directory.
3. When exiting this context, the temporary directory is removed with all files in it.
   Use `rmtree` from `shutil` to remove whole directory.
4. The new working directory becomes the same as before entering context.
"""
import os
import shutil
import tempfile

class TempDir:
    # TODO: please ad your code here
    # temp_file = tempfile.TemporaryFile() # a temporary file

    def __enter__(self):
        self.old_dir = os.getcwd() # getting path to our current directory

        temp_file = tempfile.NamedTemporaryFile(delete=True)
        random_name = os.path.basename(temp_file.name) # collect name temp_file
        temp_file.close()

        self.temp_dir = os.path.join(self.old_dir, random_name)
        os.mkdir(self.temp_dir) # creating directory to the unique temp_file

        os.chdir(self.temp_dir) # going into the temp directory
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        first, we need to go back to the initial directory old_dir
        since we cannot close temp_dir if we are inside it
        """
        os.chdir(self.old_dir)
        shutil.rmtree(self.temp_dir) # removing the temp_dir
        return False

if __name__ == '__main__':
    with TempDir() as path:
        print("Temp dir:", path)
        print("CWD:", os.getcwd())

    print("Back to:", os.getcwd())

