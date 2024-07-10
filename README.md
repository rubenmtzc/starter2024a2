# Template repository for oTree experiment project

This is a template repository that sets up a project using oTree (https://otree.org).

Aside from saving a few steps in setting up the repository itself (via GitHub's templating feature),
this pre-populates your project with some useful infrastructural files:

## Basic features

* Sets up a `requirements.txt` file including oTree (5.10.4) as well as numpy, scipy, and pandas,
  which are often useful to have in programming an experiment.
  To replicate, do these steps:
  * `pip install otree numpy scipy pandas`
  * `pip freeze > requirements.txt`
* Adds a `runtime.txt`, so the project is ready for deployment to Heroku.
* Runs `otree startproject` and includes the basic files generated.
* Some improvements to the `.gitignore` file.

## Some goodies

* Defines an app, `splash`, which implements a simple splash screen suitable for opening
  an experiment in the lab.  This screen has a `Next` button only when in demo mode.
* The app `quiz` illustrates one way to implement a multiple-choice comprehension quiz,
  coding the questions and answers as data to avoid repetitive code.  Additional
  features:
  - Records the number of incorrect attempts
  - Returns custom hint text
  - Illustrates how, using JavaScript/jQuery, to disable a submission button until the
    user has made acceptable input (in this case, selecting one of the options)

## Advanced programming tools

* Includes a `pyproject.toml` file which configures `ruff` (https://docs.astral.sh/ruff/),
  a fast linter (code checker) for Python.
* Also includes a `.flake8` file which configures the popular `flake8` code checking tool.
* Includes a configuration file for `pre-commit` (https://pre-commit.com).
  If you choose to use pre-commit, this configuration file runs `ruff` and `flake8` as above,
  as well as a few other checks which tidy your files and warn on unexpected items
  (such as committing large files).

These configuration files enforce a few opinionated settings which improve code
consistency and quality:
* Quoted strings should always use double-quotes instead of single-quotes.
* `from otree.api import *` and similar constructs are a bad idea; `ruff` will complain about this.
