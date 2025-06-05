# File paths

All computers have a *file system* that starts at some special "root" directory (`/` on Mac and Linux, `C:\` on Windows), which contains files and/or subdirectories, each of which may contain other files and subdirectories, and so on. How then do we specify a location within this system?

### Absolute paths

The most explicit way is to describe the entire path from the top of the file system to the file or directory we want. Such paths always begin with the symbol for the root. Each subdirectory is split by a "file separator", which on Mac and Linux is also `/` and on Windos is `\`.

For example, on a Mac the following would be absolute paths
- `/`
- `/Users/smith`
- `/Users/smith/Code/image_analysis/find_cells.py`

When you reference a location this way, your current working directory doesn't play a role, but you have to give the complete information of where the file is on your computer. That means if you send your code to someone else, it won't work unless their computer is set up the exact same way as yours (what if they do not have a user named "smith"?).

### Relative paths

Relative paths do not begin with the root symbol, and are added to the end of whatever your current working directory is. For example, since user "smith" is probably working under their home directory, they wouldn't need to type `/Users/smith` at the front of every path they describe.

For example, on a Mac the following are relative paths
- `Users/smith` (this looks for a directory `Users` in your current working directory, *not* at the top of the file system, because the path does not begin with a slash `/`)
- `find_cells.py` (this will look for a file called `find_cells.py` in the current working directory)
- `Code/image_analysis/find_cells.py` (this will look for a subdirectory of the current working directory called `Code`, then a subdirctory called `image_analysis` within `Code`, and then a file called `find_cells.py` within `image_analysis`)

For the last example, if your current working dircetory is `/Users/smith`, then the relative path would get translated into
```
/Users/smith/Code/image_analysis/find_cells.py
```
but if your current working directory was `/Users/smith/Documents`, then the same relative path would get translated into
```
/Users/smith/Documents/Code/image_analysis/find_cells.py
```

Relative paths are less system dependent, but the process using them must be in the working directory you are expecting for the relative path to point to the correct destination. Generally speaking we prefer relative paths, except when we really do need to do something system specific.

Note that a file name by itself actually is a relative path, that is translated into an absolute location by preceding the file name with the current working directory. So for example, if you are in the directory `/Users/smith/Documents` what 
```
ls find_cells.py
```
does behind the scenes is look for a file at the absolute location 
```
/Users/smith/Documents/find_cells.py
```

### Special path symbols

On most systems a period by itself ("`.`") means whatever the current working directory is, and two periods together ("`..`") means the directory one level up. So 
```
../data/subject_1.csv
```
means go up one directory from the current working directory, look for a subdirectory there called "`data`", and look for a file called "`subject_1.csv`" in that directory.

If you have a well-organized project directory, this kind of relative path is the one you will use most often, as all the paths will be correct on other systems so as long as they keep your entire project directory together. That is, you can move the entire project without breaking any of the paths.

On most Linux and Mac systems, there is also a special symbol for your home directory, `~`. So if your home directory is `/Users/smith/`, then `~/Documents/report.txt` will look for the file `report.txt` in the directory `/Users/smith/Documents/`.
