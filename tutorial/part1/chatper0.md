# Chapter 0 - Stack Installation
## Overview

In this chapter we will set up the tech stack used in this course.  A **tech stack** is a combination of tools used to build and run an application.  For this course we have chosen the most popular professional tools to develop our applicatoins.

- Visual Studio Code
  - Code editor and debugger
  - Extensions help us to code and improve productivity
- Python
  - Programming language we will use
  - Python libraries (such as Dash and Pandas) are collections of code that we will use to make the applications
- Git
  - Version control systems allow us to track and manage changes to our code over time
  - [Learn Git in 15 minutes](https://youtu.be/USjZcfj8yxE)
- Github
  -  Website that will store our repository
  - **Git** is not related to **Github**.  Github is a website that stores [repositories](https://www.youtube.com/watch?v=9A26ybw6tGY), and Git is a version control system.


## Installation Instructions
<details>
  <summary>Windows</summary>
  
Add link to Windows instructions

</details>

<details>
  <summary>Mac</summary>
  
Add link to Mac instructions
</details>

<details>
  <summary>Linux</summary>
  
Add link to Linux instructions
</details>


## Test the stack
Let's make sure everything is installed correctly.  Open VScode and create a new file called **main.py**.  Copy and paste this code:
```
import dash 
import dash_bootstrap_components as dbc
import pandas


print("Hello World!")
```
Then press **F5** to debug/run the file.  If we see **Hello World!** printed out in the console then we know the Python code is working properly with all libraries installed. 
**Picture:  Code working in VScode**

Now that we have our **main.py** file running let's use ```git``` to track the file in our repository.  Go to the terminal in VScode and type ```git status```.  We see that there is a new **Untracked file** called **main.py**:
**Picture: Git status**

We'll **add** that file to the git **staging area** with ```git add main.py```:
**Picture: Git add**

Then we need to **commit** the changes.  Type in ```git commit -m "This is a commit message"```.  Every commit needs a message and this is a good opportunity to include a short reminder of what this commit changed:
**Picture: Git commit**

Lastly, we will push the changes to our Github repo with ```git push```
**Picture:  succesful git push**
