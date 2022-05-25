# Linux

```{admonition} Editing TODO
:class: error
Minimum system and operating system requirements should be added here.
```

## Overview

1. **Python**
  - Python is the programming language we will use to build our applications
  - We will use various Python [libraries](https://www.geeksforgeeks.org/libraries-in-python/) (such as Dash and Pandas) as the primary building blocks for our application

2. **Git**
  - Git is a [version control system](https://www.geeksforgeeks.org/version-control-systems/) that is used to track and manage changes to our code over time in a [repository](https://www.geeksforgeeks.org/what-is-a-git-repository/)
  - [Learn (the basics of) Git in 15 minutes](https://youtu.be/USjZcfj8yxE)

3. **Github**
  - Github is a website that hosts Git repositories, which we will use to store our code.
  - You will need to [create an account on GitHub](https://github.com/signup)

## Code Editor

- **Visual Studio Code (VS Code)**
  - VS Code is a program that we will use to edit and debug our code
  - VS Code Extensions help us to code and improve productivity
  - **Note**: There are many different [IDEs](https://www.codecademy.com/article/what-is-an-ide) options but using VS Code will make for a smoother learning experience for this course

## Installing Python

Check if you already have Python installed by typing ```python --version``` in the VScode terminal.  If you see Python installed, skip to section named **"Install additional libraries"**. If you do not have Python installed, follow the installation instructions below first:
- [Text based instruction](https://www.python.org/downloads/)
- [Video instructions](https://www.youtube.com/watch?v=Br2xt6B57SA)

## Installing VS Code

Follow the instructions below to install VScode, set it up, and add Python extentions.
- [Text based instructions](https://code.visualstudio.com/docs/setup/linux)
- [Video instructions](https://code.visualstudio.com/docs/introvideos/basics)
- [Extensions - Text](https://code.visualstudio.com/docs/languages/python)
- [Extensions - Video](https://www.youtube.com/watch?v=Z3i04RoI9Fk)

### Install additional python libraries

We need to install various Python libraries, including Dash, to run our application.
We will use pip to install the libraries, but you may use equivalent commands in other package managers as well including `poetry`, `mamba`, `conda`, and others.

Assuming you are using `pip`, paste the following commands one at a time into the VScode terminal and ensure installation is complete:

- `pip install dash`
- `pip install dash-bootstrap-components`
- `pip install pandas`

![img-install-dash](./ch0_files/install-dash.png)

```{caution} text
You may need be asked to install some dependencies, and you should agree to have those dependencies installed.
```

## Git

To install Git onto your computer, follow the instructions below:
- [Git - Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
