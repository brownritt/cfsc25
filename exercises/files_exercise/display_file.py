# display_file.py
#   Jason Ritt, Brown University
#
# Answer to File Handling Exercise:
#   https://github.com/brownritt/cfsc25/blob/main/exercises/files_exercise/files_exercise.md
#
# Part of the Computational Fluency Short Course 2025, in the Carney Institute for 
# Brain Science at Brown University.

# This version assumes there is a subdirectory `data` in the current working
# directory of the running code, which contains a text file named `messages.txt`.
#
# As a hint, if using VS Code to run the file, use the Explorer tab to open the 
# folder containing the code. Then the "Play" button will run the code in the 
# correct working directory. With other IDEs, you may need to use other procedures
# to run the code in the correct working directory.

import os

# As a diagnostic, print the working directory
print(f"The code's current working directory is {os.getcwd()}")

# Define a relative path to the data file
data_dir = r'data'
file_name = r'messages.txt'
FILEPATH = os.path.join(data_dir, file_name)

# Open the file, read all lines, then print each line
with open(FILEPATH, 'r') as f:
    lines_all = f.readlines()
    for line in lines_all:
        print(line)

# Aside: with...as uses a "context manager" to open the file.
# This motif provides some convenience and also protection 
# against possible file handling errors (files will "close
# cleanly" even if something inside the `with` block throws
# an error).
