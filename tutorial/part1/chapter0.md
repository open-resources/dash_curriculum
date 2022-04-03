# Chapter 0 - Stack Installation
## What you will learn

In this chapter we will set up the tech stack used in this course.  A **tech stack** is a combination of tools used to build and run an application.  For this course we have chosen the most popular professional tools to develop our applicatoins.

- **Visual Studio Code**
  - VScode is a program that we will use to edit and debug our code
  - VScode Extensions help us to code and improve productivity
  - **Note**: There are many different [IDE](https://www.codecademy.com/article/what-is-an-ide) options but using VScode will make for a smoother learning experience for this course
- **Python**
  - Python is the programming language we will use to build our applications
  - We will use various Python [libraries](https://www.geeksforgeeks.org/libraries-in-python/) (such as Dash and Pandas) as the primary building blocks for our application
- **Git**
  - Git is a [version control systems](https://www.geeksforgeeks.org/version-control-systems/) that is used to track and manage changes to our code over time in a [repository](https://www.geeksforgeeks.org/what-is-a-git-repository/)
  - [Learn Git in 15 minutes](https://youtu.be/USjZcfj8yxE)
- **Github**
  -  Github is a website that hosts Git [repositories](https://www.geeksforgeeks.org/what-is-a-git-repository/)


## Installation Instructions
[**Windows**](chapter0_windows.md)\
[**Mac**](chapter0_mac.md)\
[**Linux**](chapter0_linux.md)

## Github
- [Getting started with your github account](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)
- [Video - How to Create Github account](https://www.youtube.com/watch?v=QUtk-Uuq9nE)

After you create an account we need to make a repository that will store your code:
- [Text - Create a public repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Video - How to create a Github repository](https://www.youtube.com/watch?v=u-_uGO95xco)

Now we need to set up a secure way to talk with Github by using a personal access token:
- [Text - Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Video - Using a personal access token](https://www.youtube.com/watch?v=kHkQnuYzwoo)

We can now **clone** the repository from Github to our local machine.  Go to your Github repository home page, click the green *Code* button, select *HTTP*, copy the web address.  Go to the VScode terminal and enter:\
```git clone *web address copied from Github*```

**Add gif of copying https clone command, pasting into VScode**\
Press enter, enter your github account credentials (might need to set up git config here for first time)
```
git config --global user.name "bolajiayodeji"
git config --global user.email mailtobolaji@gmail.com
 ```
**Add gif of being prompted for github credentials and entering them**\
Lastly, open the newly cloned folder in VScode\
**Add gif of opening repo folder in vscode**


## Test the stack
Let's make sure everything is installed correctly.  Open VScode and create a new file called **main.py**.  Copy and paste this code:
```
import dash 
import dash_bootstrap_components as dbc
import pandas


print("Hello World!")
```
Then press **F5** to debug/run the file.  If we see **Hello World!** printed out in the console then we know the Python code is working properly with all libraries installed. 
**gif:  Code working in VScode**

Now that we have our **main.py** file running let's use ```git``` to track the file in our repository.  Go to the terminal in VScode and type ```git status```.  We see that there is a new **Untracked file** called **main.py**:
**gif: Git status**

We'll **add** that file to the git **staging area** with ```git add main.py```:
**gif: Git add**

Then we need to **commit** the changes.  Type in ```git commit -m "This is a commit message"```.  Every commit needs a message and this is a good opportunity to include a short reminder of what this commit changed:
**gif: Git commit**

Lastly, we will push the changes to our Github repo with ```git push```
**gif:  succesful git push**
