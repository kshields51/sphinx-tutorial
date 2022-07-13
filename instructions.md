# To Get Everything Installed Via Pip

Run the following command to install sphinx

Important! On mac pip should be referenced as pip3

```
pip install -U sphinx
```

To check that sphinx was properly installed you can run

```
sphinx-build --version
```

This should return something like `sphinx-build 5.0.2` (version may differ)

Since you will be using `.md` files and not `.rst` files, you need to install the `myst-parser` 

```
pip install myst-parser
```
Optional: To make it easier to work with the docs, you need a way to listen for changes to the docs automatically and reload the docs website. To do this, use `sphinx-autobuild`
```
pip install sphinx-autobuild
```

# To start a project
Sphinx comes packaged with a command line interface (CLI) for beginning a project in an easy way. Simply navigate to the path that you would like the documentation to live and enter the following command.

```
sphinx-quickstart docs
```

This should start the program. It should ask you a few questions that will allow it to configure itself properly. 

- For `Separate souce and build directories` enter `n`
- For `Project name:` and `Author name(s):` and `Project Release []:` enter whatever you wish
- By default, sphinx uses English so if you would like to keep it that way, just hit enter when prompted to pick a langauge. I am assuming that if you want Spanish you would put `es` (untested)


# Anatomy of a Sphinx Docs folder (when started with n for separate source and build directories)
The CLI tool generates the following folders and files
- conf.py - The most important configuration file for sphinx. 
- _build - Contains
- _static - A place to store
- _templates - a place to store 


# Allowing the use of .md Files Instead of .rst
To have Sphinx allow you to use `.md` files you need to add the `myst-parser` to the list of extensions. To do this:
- Open the `conf.py` file inside of the `docs` folder
- add `myst_parser` to the list contained inside of the variable `extensions` Like this:
```python
extensions = [
'myst_parser'
]
```
Now you are all setup to use `.md` files
# Our Test Code for using Docstrings
This repository contains a folder called `test-project`. This will contain various Python files that will be used to demonstrate the power of Sphinx for documentation generation.

# Generating and Viewing Your Documentation
Sphinx looks in the `docs` folder for markdown files when given the command `make html`. To generate the documentation:
- Make sure that you are inside of your docs folder on the command line. When there, run this comand:

```
make html
```
Note: on windows you may need to type `./make html` as 
`cmd` and `Powershell` force you to do this.

Now, inside of your `_build` folder, navigate to the `html` folder and you should see an `.html` file with the same name as you had for your `.md` file. This can be opened with any webbrowser and rendered to the screen. Voila!

# (Optional) Using `sphinx-autobuild` for Easy Coding

You can use `sphinx-autobuild` to live update your html rendered documentation as you edit your markdown files. This eliminates the need to compile your `.md` files all the time using the `make html` command.

From your `docs` folder
```
sphinx-autobuild . docs/_build
```
This will take everything from your current directory and place it into a directory called `docs-autorefresh/_build`. It's a little confusing since you already have a docs directory