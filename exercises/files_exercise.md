# File handling exercise

This exercise summarizes the interfaces and file system concepts discussed today.  Follow the steps below:

- Using a terminal, create a "top level" project directory, say `files_project`, using `mkdir`
- Change the working directory into your new directory using `cd`
- Use a text editor to write a three or four line text file (content is up to you)
- Make a new directory `data`
- Move your text file into `data` using `mv` (Mac/Linux) or `Move-Item -Path XXX -Destination YYY` (Win)
- Open a new file `display_file.py` in VS Code, inside `files_project`
- At the top of the python file, put `import os`. This will import the "operating system" module form the standard library.
- Use it to define a path to your text file (hint, try `os.path.join`) in the variable `FILEPATH`
- Include the following code to print the content of your file:
```
with f as open(FILEPATH):
    lines_all f.readlines()
    for line in lines_all:
        print(line) 
```
- Run it and see if it works

- As a variation, create another subdirectory of your project called `code`, put your python script there, and then redefine the paths appropriately

