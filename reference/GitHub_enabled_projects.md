# Starting a GitHub enabled project

While there are many ways to start a project on your machine that is also GitHub enabled, it is easier to take steps in a specific order.

The main convenience of first creating the repo through GitHub is:
- The remote URLs are automatically set (check `git remote -v`)
- You can use templates for common files


## With GitHub Desktop

If you are using the GUI application GitHub Desktop, the simplest approach is probably to select `New Repository` under the `File` menu, and then hit the `Publish repository` button (this process assumes your GitHub Desktop is logged in to your GitHub account).

Once you have the repo, you can use the `Show in Finder` (Mac) or `Show in Explorer` (Win) button to open the local directory and begin making changes.


## With command line git

In terminal we do essentially the same thing in reverse.

- Make the repository on GitHub using a web browser
    - Include the default `README.md` file.
    - You may choose to also add a `.gitignore` file (GitHub has templates for many programming contexts) and/or a `LICENSE`.
- In a terminal, use `git clone` to clone the repo to the desired location on your machine, following the instructions in the "Code" button on your repo's webpage. 
- Note: do *not* download a Zip file from the website; you must actually *clone* the repo.

Then start making changes in your terminal, or check `pwd` and direct your other tools to that directory.

## Changes to make before you start coding

It's a good idea to set up some basics in your repo right when it is first created.

- Add subdirectories for your project skeleton
- Edit the `README.md` to add your project information
- Edit the `.gitignore` to exclude data or figures directories (or anything that will be large files), plus any system dependent files (like `.DS_Store` on Macs).
- Add+Commit your changes locally, push your changes to GitHub
- Copy any other existing files you need into your project directory
- Add+Commit. Push.
- Start coding. Add+Commit+Push.

## Keep up to date before making new changes

If you return to a project after some downtime, it is a good idea to `git fetch` and then check `git status` before doing anything else. This will make sure your local copy is aware of any changes that may have been made to the remote on GitHub. If those changes are extensive, you should probably pull them before doing any other work.
