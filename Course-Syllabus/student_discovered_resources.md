# Helpful Resources
As instructors, we've tried hard to provide you with the information that you need. With that being said, we can't necessarily find every good resource. If you find helpful hints, tips, and tricks create a pull request to post them here.

# Git related

http://rogerdudler.github.io/git-guide/

https://www.youtube.com/playlist?list=PLfdtiltiRHWFEbt9V04NrbmksLV4Pdf3j

https://www.youtube.com/watch?v=1ffBJ4sVUb4

[Dealing with pulling from a specific branch](http://stackoverflow.com/questions/658885/how-do-you-get-git-to-always-pull-from-a-specific-branch)

# Python related

## Python Style Guide Support

Instructions for Pep 8 style checker at command line

https://pypi.python.org/pypi/pep8

It's worthwhile to install the pep8 module so you can check your code against the PEP8 formatting standard, install with "pip install pep8" and run it using "pep8 <your script here>"

## Line counters

There are several line counters available as python modules:

Lizard -- measures actual lines of code, ignoring blanks lines and comments
linecounter -- counts lines in file, or just non-blank lines

Install either module using "pip", as "pip install lizard" or "pip install linecounter"

## Code Skulptor

Code Skulptor is a browser-based Python editor and runner, somewhat similar to Jupyter

http://www.codeskulptor.org
http://www.codeskulptor.org/docs.html

## Reference Data

A python dictionary of states with their abbreviations: http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/

## String Methods (reference)

Documentation on useful string methods (such as .ascii_lowercase):
https://docs.python.org/2/library/string.html

## Supplemental Reading

Good supplemental reading to our textbook
http://openbookproject.net/thinkcs/python/english3e/index.html

## Sorting Lists using a function applied to each item

How to sort using a "key" function:  
a_list = ['1', '5', '9', '11', '2', '100', '4']  
\# sort as if item is a string  
a_list.sort()  
print(a_list)  
\# determine sort postition based on int value  
a_list.sort(key=int)  
print(a_list)  
> ['1', '100', '11', '2', '4', '5', '9']  
> ['1', '2', '4', '5', '9', '11', '100']  

6 Useful Sorting examples
http://www.thegeekstuff.com/2014/06/python-sorted/

b_list = ["Ajay", "basic", "Barnie", "alice"]  
\# sort alpha with uppercase  
b_list.sort()  
print(b_list)  
\# sort but ignore uppercase  
b_list.sort(key=str.lower)  
print(b_list)  
> ['Ajay', 'Barnie', 'alice', 'basic']  
> ['Ajay', 'alice', 'Barnie', 'basic']  

## Great Overall Resource For Programming Concepts
http://composingprograms.com/

# Environment related

If you're having issues running Python on Windows, you may want to look at the Berkeley Compute Environment, a VM with Python and everything pre-installed. Inlcudes links to help too!

http://bce.berkeley.edu/

If running your Python program on Windows and you get an error when trying to print Unicode characters you can use this resource to help prevent the errors:
http://chase-seibert.github.io/blog/2014/01/12/python-unicode-console-output.html

# Command Line related

A great survival guide...
https://github.com/jlevy/the-art-of-command-line?imm_mid=0d3d37&cmp=em-prog-na-na-newsltr_20150620

## A simple Windows working environment

The following software will provide a Windows working environment that includes Python 3.x, common Python libraries, IPython, Jupyter notebooks, Git, a Bash shell, a Windows command prompt for git (if you prefer that to Bash), a Git GUI, and some other useful Windows/Bash/Git integration.

### Installation
1. **Anaconda** : https://www.continuum.io/downloads
  * Download and run the Python 3.x installer for your version of Windows (32- or 64-bit).
  * With the possible exception of your installation directory, accept all of the default installation options.  
2. **git-scm** : https://git-for-windows.github.io/
  * Download and run the installer from the 'Download' link at the top of the page.
  * As with Anaconda, accept all default installation options (except default directory if you want to change that)  

### Use
From this point, you can work using *only the Git Bash terminal* (available under Git in your Windows start menu). Git CMD and Git GUI are optional - only use them if you prefer to interact with Git that way - and you don't need to interact with Anaconda/Python via Windows.

From within Git Bash:
- `python file_name.py` executes a .py file as usual
- `ipython` runs the interactive IPython command shell from within your current instance of Git Bash
- `ipython notebook` starts a Jupyter Notebook server in your current directory and launches your default web browser.
- Git commands run directly from the Bash prompt, e.g. `git status`
  * Your Git credentials are not automatically saved. If you want to save credentials locally, you must execute the command `git config credential.helper store` prior to entering a git command that will ask for your credentials (such as a `git pull`). You will need to repeat this once for each local repository.
  * See details, and a discussion of credential privacy, here: https://git-scm.com/docs/git-credential-store

# Jupyter Related

Here's a great resource for using MathJax script (it's not difficult) to insert mathematical notation into markdown cells:
http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

We've discussed Jupyter shortcuts a few times in class. I've been focusing on incorporating them each time I do classwork and they have been very helpful in speeding up my work. I went ahead and captured a PDF of the in-tool shortcut documentation, as I found it helpful as a printout at my desk. Feel free to print a copy if you think it would be helpful: https://goo.gl/9oXfXP

There was recently a webinar hosted by Jonathan Witmore on "Make Data Science Easier - Power Tips & Tricks Using Jupyter Notebooks".  Seemed very helpeful and links to the recording and his Github repository are below:

  The recording to the webinar is here:
  http://berkeleydatascience.adobeconnect.com/p90quk4u0z3/

  Jonathan's Github repository is here: https://github.com/jbwhit/berkeley-jupyter-notebook

A nice Jupyter Notebook visualization intro published from Kaggle (you should subscribe to Kaggle if you're not yet):
https://www.kaggle.com/benhamner/d/uciml/iris/python-data-visualizations

## Jupyter Hints
If you highlight a block of text in Jupyter and hit "tab" it will indent all the selected code one indent. This is useful if you suddenly realize a bunch of text needs to be wrapped in an "if" statement or a "try" statement.
This also works in reverse. If you want to un-indent a block by a certain number of tabs, you can highlight the whole block and press SHIFT+TAB.
This works the same way in most semi-smart editors (not just Jupyter!)


# Functions

Closures can be tricky but they're worth learning. [Here's a helpful resource.](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)

[I did a little write up on closures](http://newtodatascience.blogspot.com/2016/02/understanding-closer-in-python.html) to try to help myself understand Python's implemenation. Maybe others will find it helpful.

# Article Tips:
Good resource on coupling/look coupling examples:
http://stackoverflow.com/questions/2832017/what-is-the-difference-between-loose-coupling-and-tight-coupling-in-object-orien

# Exception Handling
This is a great write up on exception handling: https://wiki.python.org/moin/HandlingExceptions

# Formatting
Found this great resource of different ways to format strings at the command line/printing.
https://pyformat.info/

# Programs from book are available here:
https://github.com/madscheme/introducing-python

# Pandas
Repository on Github with useful Pandas lessons/practice data: https://github.com/jvns/pandas-cookbook  
=======
# Regular Expressions
I'm sure there are dozens of regular expressions tutorials, but i found and gained from doing some
exercises and running through the python usage of regular expressions on:
http://regexone.com
Also, I think Anubhav referred to the site below, which has a cheat sheet and also tests your expressions:
http://pythex.org
>>>>>>> fa08bce769f02170e01859cd54c1484cfab44132
