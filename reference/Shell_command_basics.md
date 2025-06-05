# Shell command basics

It's easy to be overwhelmed by the cryptic names and sophistication of a shell's command line interface, but in practice, there's a small set of essential commands that get one up and running on most tasks.

One source of help is the `man` command ("manual"). For example, typing `man ls` will print help pages for the list command. The web also provides many instructions and examples.

Everything below assumes a Linux-like or Mac command line, but there are analogous versions of working in a Windows shell (usually PowerShell).

### A bit about command line arguments

The general format is a command name, followed by some number (maybe zero) of *arguments* separated by spaces. It's often the arguments that are harder to figure out than the command itself.

There are generally three types of arguments. First, "flag" options are preceded by a dash (`-`), and switch between two settings. For example, `ls` by itself gives a compact listing of the contents of the current working directory, while `ls -l` switches the listing to a "long" format with more details on each file. The flag is either present or not, and flags can be combined behimd a single dash. For example, `ls -l -t` and `ls -lt` both display a long format listing of the current directory (`l`) sorted by file modified time (`t`).

Second, some arguments are options that take an additional parameter. For example, `ls -l -D %A` will display the directory in long format (`l`) using a display format for the file modified time (`D`) that is just the day of the week (`%A`). The option `D` tells `ls` to reformat the time display, and the parameter `%A` describes the format to choose; for example, `ls -l -D %F` will instead display the modified time as "year-month-day".

Third, some arguments are not options but other kinds of information. For examle, `ls notes.txt` will display the information of the file `notes.txt` if it exists in the current working directory, or do nothing if it does not exist. Often options and other arguments are combined, such as `ls -l notes.txt` to get a long listing (not just the name) of a specific file, or `ls -l -D %F notes.txt` to get a long listing of the file `notes.txt` with the last modified time shown as "year-month-day". 

It's hopefully clear by now that both the enormous power and the initial challenge of working with shell-like command line interfaces is not really the commands themselves, but rather the combinatorial explosion of possibilities from combining lots of arguments.

### Some essential commands

`ls`
"List". List the contents of the current directory.
- `-a` for all
- `-l` for long
- `-t` to sort by last modified time

`more`
Display the contents of a (text) file in a simple viewing interface.

`less`
Display the contents of a (text) file in a simple but improved viewing interface. *N.B.*: Programmer humor often escapes through command names.

`pwd`
"Print Working Directory". Display the working directory

`cd`
"Change Directory".
- `cd` by itself often changes to the current user's home directory, though this is system dependent.
- `cd ~` always returns to the home directory
- `cd ..` goes up one directory in the file system
- `cd DIRNAME` changes to the directory named `DIRNAME` *if the shell can*. If the directory doesn't exist or one does not have permissions to access it, an error is displayed.
- More generally, `cd PATHNAME` changes to the directory at the end of `PATHNAME` if possible, whether a relative or absolute path.

`mv`
"Move". Move a file named as the first argument to the location specified by the seond argument (renaming the file if the last argument is not a directory name). For example, `mv file_old.txt file_new.txt` wil rename the file `file_old.txt`, if it exists. `mv file_old,txt Desktop/` will move the file to the directory `Desktop` if both exist, and if `Desktop` is a subdirectory of the current working directory.

`cp`
"Copy". Works the same way as mv, but makes a copy of the file without deleting the original.
- `-p` preserves file file information such as last modified time

`rm`
"Remove". Deletes a named file; **warning**: there is no undo or Trash for this command. The moment you use it, the file is gone forever (except in some special cases).
- `rm FILENAME` deletes the named file, if it exists
- `rm -i FILENAME` asks for confirmation first

`mkdir`
"Make directory". Create a directory
- `mkdir DIRNAME` makes a subdirectory named `DIRNAME` in the current working directory, *if possible* (otherwise it will display an error).
- Note, if `DIRNAME` begins with a slash `/`, then `mkdir` will try to make the directory at the absolute location in the file hierarchy. For example, `mkdir /Users/smith` will try to make a directory named `smith` in the directory `Users` which is just one subdirectory below the top of the file hierarchy (this should fail on most systems, because you do not have permissions to change `Users`). 

`rmdir`
"Remove directory". `rm` generally will not delete a directory. The system wants you to confirm that you really want to delete the directory, and even `rmdir` will throw an error if the directory is not empty.
