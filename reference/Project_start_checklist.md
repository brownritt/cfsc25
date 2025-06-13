# Project start checklist

Below is one possible default set of steps to start new projects. One can modify to suit the specifics of each project. 

The key outcomes are to have version control enabled, to keep different types of things (main code, "helper" code, test data, documentation, etc) in well organized subdirectories, to have meaningful documentation of what the repo is supposed to do, and to set up any environments or installations of software dependencies.

- Set up a [git](Git_basics.md) repository
  - If you are [starting from scratch](GitHub_enabled_projects.md)
    - Make a new repo on GitHub (or other preferred remote)
    - Clone to your machine
  - If you are collaborating on an existing project and are authorized to push
    - Clone their repo from GitHub to your machine
    - Use git branching to separate your changes from `main` and enable pull requests
  - If you will work on shared code but are not authorized to change it
    - *Fork* their repo on GitHub
    - Clone your forked repo to your machine and work on it
- Set up [environments](Virtual_environments.md)
  - If needed, make a new environment with the packages you will use
  - Or, if the repo includes an `environment.yml`, `requirements.txt`, or similar, use it to make a virtual environment
  - Or, choose an existing environment on your machine
  - Activate the desired environment
  - Export your environment to a environment file for reproducibility
  - Make sure `.gitignore` includes any environment directories like `venv`
  - Use git to add and commit the environment file(s)
- Modify the README as appropriate, then add and commit
- Set up an appropriate [directory structure](Directory_and_file_organization.md)
- Copy in any existing files you might need, then add and commit
- Code away, making commits after each "chunk" of progress or distinct "idea"
- Fetch/Pull before beginning work and at regular intervals during the day; Push changes after making big changes and at regular intervals
