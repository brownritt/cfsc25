# Directory and file organization

## Directory structure for a project

There are many ways to set up a directory structure for a new project, and no one way will work well in all settings. But setting up your structure in advance will keep things organized and enhance the usability and reproducibility of your work.

Some broad rules of thumb are:
- keep code and data separate
- distinguish "raw" data (e.g. coming directly from an experimental system) from "pre-processed" data
- provide a distinct location for analysis outputs, typically figures and/or numerical tables

The choice of output organization is often subtle, as one may want to keep many different versions of analyses, for example with differing parameters.

An example minimal structure for a data science project **with small data files** could be
```
project_name/
|- README.md
|- data/
|  |- raw/
|  \- derived/
|- code/
\- figures/
```

*Important Note*: `git` can be very inefficient with large binary (non-text) data files. Usually one should include only code and small files in the commits (there are other tools for tracking data files). Data is often kept somewhere other than in the project directory. Sharing this kind of project then requires handling paths to find where the data is on different systems.

One often adds an *environment file* to the top directory to keep track of any package installations, and a `.gitignore` that excludes (at least) data and figure directories.

If one is developing general software instead of doing data analysis the project structure changes accordingly. There would not be `data` or `figures` directories, and there might be other directories like `assets` (e.g. used to store images, sound files, or other media used in an app) and/or `bin` ("binary", used for executable files).

There are many other naming conventions. For example, for historical reasons the `code` directory is often named `src`, an abbreviation of "source", which is short for "source code." Configuration files are often in an `etc` directory, and some people separate `scripts`, code that is meant to be run from a shell as utilities, from the "main" code in `src`.

Tools like [cookiecutter](https://github.com/cookiecutter/cookiecutter), which build project directory structures from templates, are useful when projects are especially complex or when you will be making many similar projects. However, it's usually enough to manually put a few key directories in place initially, and adjust as need.

As usual, a good approach is to start simple, using whatever works for you and your collaborators, and then learn from and adjust to your experience over time.


## File names

Choosing a good file naming convention can dramatically improve usability and reproducibility. A few general conventions:

- do not use spaces within directory or file names; use `_` or `-` as separators
- use ISO standard dates in the form `YYYYMMDD` (e.g. `20240607`)
- if there is also a timestamp, use `HHMM` or `HHMMSS` in 24 hour format (e.g. `20240607_1430`)
- choose "fields" that are the same across data files, for example `sub` for subject, or `task` for task type; examples could be 
  - `sub-1_task-2back_20240607.csv`
  - `sub-1_task-NMS_20240607.csv`
  - `sub-2_task-2back_20240607.csv` 


Researchers increasingly adopt "standardized" data formats that work across systems and types of experiments. Two prominent examples are [BIDS](https://bids-specification.readthedocs.io/en/stable/index.html) for non-invasive human imaging (fMRI, EEG, etc), and [NWB](https://nwb-overview.readthedocs.io/en/latest/) for physiology and behavior. BIDS in particular has a well-worked out convention of file naming for data coming from typical fMRI and EEG experiments.


## Data directories

There are similar considerations for data directory organization. The two most common organizational choices are subject organized or session organized.

A subject organized data archive might look like 
```
project_data/
|- participants.csv
|- sub-1
|  |- 20240606/
|  |  |- 2back/
|  |  \- NMS/
|  \- 20240607/
|- sub-2
|  |- 20240605/
|  |- 20240606/
|  \- 20240607/
\- processed_data/
```

A session or date organized data archive might look like 
```
project_data/
|- participants.csv
|- 20240605/
|  \- sub-2/
|     |- 2back/
|     \- NMS/
|- 20240606/
|  |- sub-1/
|  \- sub-2/
|- 20240607/
|  |- sub-1/
|  \- sub-2/
\- processed_data/
```

The important thing is to have a clearly defined set of rules, so data stays well organized, and can be easily and accurately accessed by analysis pipelines.
