# Basics of virtual environments

Virtual environments keep track of your code "dependencies", which is the set of other software needed to run your code. They also isolate dependencies across projects to avoid conflicts. If you send someone else your code without those dependencies, there's a good chance your code won't work on their system.

Rather than send someone a full copy of your operating system (which is close to what a *container* does), it is often enough to list in a very precise way (that is, precise to a computer) what other code their system might need. This is an approximate way to communicate dependencies, and sometimes fails, but has the virtue of being efficient (only a small "environment" needs to be included in your repo) and descriptive (you explicitly describe what you used, rather than send some incomprehensible list of everything in your operating system).

There are really two things happening here:
- *package management*, which installs new software while resolving possible conflicts between versions
- *environment management*, which keeps packages organized such that one can easily switch between multiple and possibly incompatible sets of software for different project

## Beware slopy installs

It is generally a bad idea to install new software in Conda's `base` environment, or to use `pip` without first creating a "local" environment to modify. The danger is that one might alter their "core" python distribution in some way that breaks basic operations.

Instead, **always** activate a project-specific environment (after creating it if needed) before installing or modifying packages. Then if something goes wrong, you can delete that environment and start over, without having to reinstall your whole distribution.

Similarly, be careful to always check what environment you are "in" before proceeding with any other steps (coding or package installation). In terminals, the currently active package is usually noted at the beginning of the command line. In IDEs, there is usually a display box (e.g. lower right in VS Code).

## Using `conda`

### Creating and "storing" environments

If you have `conda` on your system, you can make a virtual environment with a command like
```
conda create -n fmri_analysis numpy pandas matplotlib
```
This tells `conda` to create a new virtual environment named `fmri_analysis` (that's what the `-n` otpion does), and to include in that environment the packages `numpy`, `pandas`, and `matplotlib`, assuming it can find them at expected locations online.

Note `conda` will also install *all packages that those packages depend on*, and `conda` may also need to make changes to other packages already on your system, if the versions do not match. This is a complicated process, which is why most of the time we want to let the package managers sort it out if they can.

If you are currently in a virtual environment, you can make a file that describes the environment with
```
conda env export -f environment.yml
```
This will make a new file `environment.yml` (in the current working directory) that lists all the packages in the current environment. If you send that file to someone else, they can recreate your environment with
```
conda env create -f environment.yml
```
Note the `env` invocation of the "environment" module (use it when creating from an environment file but not when typing a list of packages). This create command does not include a name for the virtual environment; the name is listed inside the `environment.yml` file, and that is the name `conda` will use.

One useful pro-trick is to export a list of just the packages you actually requested, not including all the other packages `conda` installs to satisfy the dependencies:
```
conda env export --from-history -f environment_minimal.yml
```
This file also can be used with "create", but will list only the packages you explicitly requested. In the above `fmri_analysis` example, the file `environment_minimal.yml` would list just the packages  `numpy`, `pandas`, and `matplotlib`, while the file `environment.yml` would list a bewildering array of many, many packages including detailed version numbers.

I suggest including both types of environment files in your repos. The more explicit version is needed for reproducibility, but if anything goes wrong, the minimal version communicates what you intended to set up.

### Activating and deactivating environments

One activates an environment with
```
conda activate <ENVIRONMENT_NAME>
```

When needed, an environment can be deactivated with
```
conda deactivate
```
which deactivates the currently active environment. Sometimes one needs to deactivate a current environment before switching to a different environment.

One can see all the environments currently available with
```
conda env list
```
Note the `env`; `conda list` would instead list all the packages installed in the currently activated environment.

### Modifying with new packages

If an environment already exists and **it is currently activated**, you can add new packages to it with

```
conda install <PACKAGE_NAME>
```

Again, this will install packages in whatever the currently active environment is.

It is best practice to export new environment files after changes, so that your list of dependencies remains accurate.


## Other environment and installation choices

While `conda` is accessible and popular, there are other options to do the same kind of work. Some people have strong opinions about these sorts of things, and there are real differences between the options. Not every package is available through every package manager, some are much faster and/or efficient than others, and so on.

Th most common alternative is the "official" Python package manager, `pip`. To keep things organized in environments, one typically uses `venv` with `pip`. See more information below.

There are also a few "flavors" of `conda`, that differ mostly in the underlying machinery used to select packages for installation.

*Note*: `conda` and `pip` do not play nice together; try to avoid using them in the same environment. If you must use both (for example, because they have access to different packages), best practice is to finish all `conda` installs, and use `pip` only at the end.

More recent tools like `poetry` improve on usability and robustness, and try to slant towards *project* management instead of just *package* management.

## Using `pip` and `venv`

The workflow for `pip` and `venv` is similar to that for `conda`. One key difference is that `conda` by default keeps a set of environments in a central location, that can be used across multiple projects. By contrast, `venv` by default maintains each environment within each project directory.

### Creating, activating, and deactivating environments

To create an environment, use
```
python3 -m venv venv
```
This will create a directory called "venv" (or whatever name you put as the last argument) in the current working directory. 

To activate the environment, first make sure no other environments are active, and type
```
source ./venv/bin/activate
```
Note you will sometimes see the `source` command replaced with a period and a space `. `, which works with many shells including Windows PowerShell.

To deactivate:
```
deactivate
```

### Installing and tracking packages

Once an environment is active, you can install new packages with
```
pip install <PACKAGE_NAME>
```
You can list several packages simultaneously.

To save a list of currently installed packages, use
```
pip freeze > requirements.txt
```

To install packages from a list of requirements, use
```
pip install -r requirements.txt
```
