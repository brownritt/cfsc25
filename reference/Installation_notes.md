# Installation notes

 Notes on setting up your machine for the Carney Computational Fluency Short Course at Brown University.  Given the wide variability in student equipment, *these are not comprehensive instructions*, but point to online resources with their own installation instructions.

Please contact course staff if you need help. Additionally, we will provide time for support in the first course meeting.

## Overview

For the short course, please set up each of the below applications and accounts as needed (roughly in order of priority):

- [Python](#python)
    - Option 1: Anaconda
    - Option 2: Miniconda
    - Option 3: Official python
- [git](#git)
- [GitHub](#github)
    - Create an account
    - Keys or tokens for authentication
    - (optional) GitHub Desktop
- [VS Code](#vs-code)


## Python

If you already have a version of python on your machine, you can skip this section. If you don't and are not sure what to install after reading the below, I suggest going with "Option 1: Anaconda".

### Option 1: Anaconda

A historically popular option to install python for scientists is the [Anaconda distribution](https://www.anaconda.com/products/distribution). On the linked page, click the tiny "Skip Registration" button if you do not want to give your email address (or enter your address if preferred); on the next page, choose an appropriate option from "Distribution Installers" on the left side of the page.

This distribution is a "fremium" collection of core python plus a large pre-installed selection of useful packages and other tools. For many scientists the convenience is a key selling point, but some researchers prefer a leaner code base that installs only what they know they will need. Also, the company behind the distribution recently introduced controversial new licensing terms, though use is still free for academic researchers and small organizations.

`Anaconda Navigator` is a specialized launcher app that comes installed with the Anaconda distribution, but you can still launch python without it (e.g. from a terminal). You may or may not prefer this particular GUI interface to start new projects and manage environments.

Installing Anaconda will also install the tool `conda`, which handles package management and virtual environments.

### Option 2: Miniconda

People who prefer `conda` package management over `pip` (see below) but don't want to install the full Anaconda distribution or use `Navigator`, instead install a "miniature Anaconda distribution" called `miniconda`.

Follow the same [link](https://www.anaconda.com/products/distribution) and instructions as for full Anaconda, except choose an appropriate option under "Miniconda Installers" on the right side of the page.

### Option 3: Offical python with pip package manager

Installation of the "official" python distribution from the [Python Software Foundation](https://www.python.org/downloads/) has become much easier and cleaner in recent years, and lowers reliance on third party applications.

The python installation comes with `pip` and `venv`, which can be used for package management and virtual envrionments instead of `conda`. There are many opinions about which is better (and we will discuss some of the choices in class), but geneally speaking, either `pip` or `conda` will work fine for your projects.


## Git

Git is by far the dominant choice of version control tool. It works best for plain text documents (including code); if needed `git` can also handle binary files (like images or raw data), but there are other tools optimized for such files.

There are many options to install `git`. You should first check if you have it already by opening a terminal and typing 
```shell
git --version
```
If you see something like "`git version 2.39.5`", you should be set.

General installation instructions and downloads are available directly from the [Git community](https://git-scm.com/downloads). These include binary installers for Windows.

For Macs, I suggest installing the Xcode command line tools (which includes git), by opening a terminal and typing
```shell
xcode-select --install
```
One could alternatively install Xcode in its entirety from the App Store. Xcode is a massive developer suite; most of its components are needed only if you want to develop Apple software (e.g. an iPhone app).  However, some items like the `clang` compiler can be useful for advanced projects.

## GitHub

[GitHub](https://github.com) is the biggest online platform for sharing code repositories, but it is not the only one, and you can use `git` without using GitHub (there is no formal relationship between the tool itself and the online platform; GitHub is owned by Microsoft).

### Make an account

You need a GitHub account in order to "push" code from your computer to the platform or to access private repositories, including in this course. It is up to you if you want to link an account to your Brown email (which will disappear at the end of the summer), or use a persistent account with a permanent email.

To create an account, go to the [main page](https://github.com) and click "Sign up".

### Keys or tokens for authentication

In order to connect with GitHub's server, your local version of `git` needs to be able to authenticate (prove your identity). There are two primary approaches, and unfortunately both take a bit of work to set up. However, actually using `git` is usually smooth once the set up is done.

As an aside, note that although you must log in to GitHub in a web browser to follow the below instructions, merely being logged in to the website does not authenticate `git` itself. Moreover, once your `git` is set up, you can log out of the browser and still use version control.

An older but still generally prefered way to authenticate is with [ssh keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). You can skip the pages in the link on agent forwarding and deploy keys, and just follow the steps to
- [generate a new key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [add the key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [test your connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

A newer alternative method uses [personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) (PATs). While these provide some security advantages for large organizations and advanced development workflows, they can be  confusing to set up correctly and securely (and there are examples of repositories becoming *less* secure with PATs from user mistakes).

You are free to use PATs in the course, following the instructions on the linked page, but I suggest going with ssh authentication, which is likely adequate for most ordinary usage. You should not set up both.

### (optional) GitHub Desktop

GitHub offers a standalone application [GitHub Desktop](https://desktop.github.com), that wraps around the core `git` tool and provides some convenient shortcuts for projects using their platform. This may be an easier option for Windows, and can be used on Mac or Linux if you would like to have a GUI interface. However, it is purely optional for the course.


## VS Code

[Visual Studio Code](https://code.visualstudio.com/download), typically called VS Code, is one of the most popular "integrated development envrionments" (IDE) across operating systems and coding languages. Although owned by Microsoft, VS Code is free and open source (not to be confused with "Visual Studio", which is a different commercial IDE product).

Because it is meant to be general and powerful, VS Code can be a little intimidating when first opened, but in practice you can skip many of the setup prompts if you want.

That said, once VS Code is installed, I suggest you add (using the Extensions panel on the left inside the app) at least the following extensions to expand VS Code's support for python coding:
- Python
- Jupyter
- PowerShell (if using Windows)

In addition to these top level Extensions, there are also many other specialized Extensions you may choose to install. 

I also suggest you follow instructions for enabling Git integration if you are prompted to do so. One needs to have `git` installed first.


