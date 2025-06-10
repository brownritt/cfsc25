# Basic git usage

## Initializing 

To manually initialize a new git repository (or just "repo") in a terminal type the command
```shell
git init
```
This will create a `.git` subdirectory in the current working directory (check `pwd`to make sure you are in the right place first!) and initialize it with information git needs to track changes.

*However*, since we often want our local repo linked to a remote provider like GitHub or GitLab, a very common workflow avoids using `git init` directly, and instead  [initializes an empty repo on GitHub](GitHub_enabled_projects.md) and clones it locally before beginning work. This workflow automatically sets the "remote" so pushing and pulling will work without further configuration.

## Checking the state of things

The terminal command 
```
git status
```
displays **local** information on things like changes git has detected in any tracked files. When in doubt, check `git status`.

While `git status` will also report a comparison to any remote repo, it uses "cached" information about the server and can get out of date. To be sure you have the latest **remote** information, type
```
git fetch --all
```
This will download the current git information from the remote, but will not make any changes to local files (unlike `pull`, see below).

It is a good idea to `fetch` whenever you have been away from a repo for a while, or whenever there is a chance someone else may have made changes to the remote repo. Otherwise, when you go to `push` you may be surprised by conflicting code changes.


## The local loop

Once a repo is set up, most git usage is just the "change-add-commit" loop:
```
<MAKE CHANGES TO LOCAL FILES>
git add <FILENAMES>
git commit -m "<COMMIT MESSAGE>"
```
Don't forget the quotes on the commit message.

Following the camera metaphor in the course, you can think of `add` as telling git to point the camera at specific files, and `commit` as telling git to take a picture. Any files that change "out of frame" (not staged for commit by `add`) will not be stored in the latest "picture" / commit.

One has to choose when to commit changes. It's generally unhelpful to treat commits like file saving as you end up with too many commits, or commit only at the end of a day and end up with too few.

One popular rule of thumb is to commit each distinct "idea": a new function, an added feature, a new analysis. 

## Other git functions 

Git is a very powerful version control system, and with that power comes some complexity. One can move back and forth between new and old versions of code, edit several independent versions in parallel, get precise summaries of changes, and combine changes from multiple collaborators with a minimum of friction. Learning how to use these other parts of git takes some time; the change-add-commit loop is the core practice that enables all the other functions.

## Commit messages

All commits should have a message that summarizes what changed. Most commit messages are brief one liners, but they can span several pages if desired. There are many conventions and style guides for commit messages, but the main goal is just to make it easy to skim or search the log of commits for particular changes. A common convention is to use a small set of prefixes such as `fix:` (for bug fixes), `feat:` (for adding a new feature), or `doc:` (for updating documentation), followed by a simple description of the details.

If you type `git commit` without the `-m` flag, git will launch a text editor, usually [vim](https://en.wikipedia.org/wiki/Vim_(text_editor)); when you close the editor its contents become the message and the commit finishes (tip: to quit vim right away and cancel the commit, type `:q!` and hit enter/return; you can then retry with the `-m` flag).  In GUIs like VS Code or GitHub Desktop there will be a small text box to write the message before hitting the commit button.

One should use the same principles regardless of the interface: short summary of the major changes first,  followed by more detailed information if needed.

## The remote loop

When there is a remote repo, there is an additional "pull-push" loop to keep the local and remote git history in sync.
```
git pull
<MAKE CHANGES TO LOCAL FILES>
git add <FILENAMES>
git commit -m "<COMMIT MESSAGE>"
git push
```
`pull` brings any new changes on the remote into your local copy. `push` does the opposite for any local *committed* changes.

If you know you are the only one working on a repo, it is not necessary to `pull` (since the remote should not have any changes not coming from your local copy), and also one can rack up a sequence of local commits before deciding to `push` them to the remote server.

However, it is generally a good idea to keep the local and remote in a similar state.

`pull` will change local (tracked) files to match the most recent commit on the remote. In general, *any local changes that have not been committed are at risk*, but committed changes can be recovered, even when there is a conflict between local and remote versions. As much as possible, Git tries to provides options and hints for resolving conflicts.

One can use `git fetch` to find out if things have changed on the remote (with `git status`), but without making any local changes.  

## Branching and collaboration

There are many other Git features and workflows. A major feature is "branching", allowing work on several distinct versions of the code simultaneously (switching between versions with `git switch`). Branches can be brought back together with `git merge`. These features become especially important when working with collaborators.

There are many distinct patterns for using Git in a team setting, and many choices about the ways branches can be created and merged. These workflows often use additional functionality provided by GitHub (such as "pull requests") that are not, strictly speaking, Git functions.

If you are working on a repo owned by someone else (e.g. your host lab), they should describe their preferred collaboration approach and workflow. As long as you understand and make a habit of the two loops above ("change-add-commit" and "pull-push"), these additional steps should be straightforward to adopt.
