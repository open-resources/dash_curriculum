# Chapter 0 - Stack Installation
## What you will learn

In this chapter we will set up the tech stack used in this course.  A **tech stack** is a combination of tools used to build and run an application.  For this course we have chosen the most popular professional tools to develop our applications.

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
  -  Github is a website that hosts Git repositories, which we will use to store our code.


## Installation Instructions
[**Windows**](chapter0_windows.md)\
[**Mac**](chapter0_mac.md)\
[**Linux**](chapter0_linux.md)

## Github
- If you don't have a GitHub account, navigate to https://github.com/ and follow the prompts. A free account is enough for this curriculum.
  - [Video - How to Create Github account](https://www.youtube.com/watch?v=QUtk-Uuq9nE)
- After you create an account, you need to make a Public repository that will store your code:
  - [Text - Create a public repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)
  - [Video - How to create a Github repository](https://www.youtube.com/watch?v=u-_uGO95xco)
  - Make sure to create a `Readme.md` file that will describe your repository's purpose.

- Now we need to set up a secure way to talk with Github by using a personal access token:
  - [Text - Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  - [Video - Using a personal access token](https://www.youtube.com/watch?v=kHkQnuYzwoo)

- Here is a nice summary to learn more about [getting started with a gitHub account](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)


The next step is to **clone** the repository from Github to our local machine. Go to your Github repository home page, click the green *Code* button, select *HTTP*, and copy the web address, as shown below with the `MyDashApps` repository. 

![img-repo](./ch0_files/cloned-repo.png)

Next, start VScode and open a new terminal:

![img-terminal](./ch0_files/vscode-terminal.png)

and enter:\
```git clone *web address copied from Github*```

![img-repo](./ch0_files/cloned-repo2.png)

Now that your file has been cloned to your computer, you need to initiate git by typing inside the terminal: `git init`:

![img-gitinit](./ch0_files/git-init.png)

Do we need this section below?

-----

Press enter, enter your github account credentials (might need to set up git config here for first time)
```
git config --global user.name "bolajiayodeji"
git config --global user.email mailtobolaji@gmail.com
 ```
**Add gif of being prompted for github credentials and entering them**\

----


## Install the necessary Python libraries
To enusre our Dash apps can run, you need to install a few libraries if you have not done so in the previous chapter. Go to the VScode terminal and type: `pip install dash` 

![img-install-dash](./ch0_files/install-dash.png)

Continue using the terminal to `pip install dash-bootstrap-components` and `pip install pandas`


## Test the stack
Let's make sure everything has been installed correctly. Open the newly cloned folder in VScode and create a new file called **`main.py`**.  Copy and paste this code inot the file:

```
import dash 
import dash_bootstrap_components as dbc
import pandas

print("Hello World!")
```
![img-gitinit](./ch0_files/new-code.png)


Click the **Run** tab located in the top section of VScode; then click **Run Without Debugging** to run the file.  If we see **Hello World!** printed out in the terminal, we know the Python code is working properly with all libraries installed. 

![img-vscode](./ch0_files/code-run.png)

Now that we have our **`main.py`** file running, let's use git to track the file in our repository. Go to the terminal in VScode and go into the cloned directory by typing `cd .\MyDashApps\`. Modify `MyDashApps` with the name of your repository. Then, type `git status`.  We see that there is an **Untracked file** called **`main.py/`** since we have not committed that file yet:

![img-status](./ch0_files/git-status.png)

We'll **add** that folder to the git **staging area** by typing: ```git add main.py```.

Then, we need to **commit** the changes. Type in ```git commit -m "This is a commit message"```. Every commit needs a message and this is a good opportunity to include a short reminder of what this commit changed:

![img-commit](./ch0_files/git-commit.png)

Lastly, with the file committed, it is now ready to be uploaded to our online GitHub repository by typing: ```git push```. 

![img-push](./ch0_files/git-push.png)

If you go to [github](https://github.com/), you should now see the new `main.py` file in your github repository.  
