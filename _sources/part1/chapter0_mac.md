# Mac Installation

## VS Code
- [Text based instructions](https://code.visualstudio.com/docs/setup/mac)
- [Video instructions](https://www.youtube.com/watch?v=bJaBHGKHv9A)
- [Extensions - Text](https://code.visualstudio.com/docs/languages/python)
- [Extensions - Video](https://www.youtube.com/watch?v=Z3i04RoI9Fk)
## Python
- [Text based instruction](https://www.python.org/downloads/)
- [Video instructions](https://www.youtube.com/watch?v=M323OL6K5vs)
- Copy and paste this line into a terminal to install the required Python libraries:\
``` pip install dash dash-bootstrap-components pandas```
  **PICTURE/GIF of pip install process and terminal in VScode**

## Git
- [Git - Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Github
- [Getting started with your github account](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account)
- [Video - How to Create Github account](https://www.youtube.com/watch?v=QUtk-Uuq9nE)

After you create an account we need to make a repository that will store your code:
- [Text - Create a repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Video - How to create a Git repository](https://www.youtube.com/watch?v=u-_uGO95xco)

Now we need to set up a secure way to talk with Github by using a personal access token:
-[Text - Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
-[Video - Using a personal access token](https://www.youtube.com/watch?v=kHkQnuYzwoo)

We can now **clone** the repository from Github to our local machine.  Go to your Github repository home page, click the green *Code* button, select *HTTP*, copy the command, paste it into VScode, \
**Add gif of copying https clone command, pasting into VScode**\
Press enter, enter your github account credentials (might need to set up git config here for first time)
```
git config --global user.name "bolajiayodeji"
git config --global user.email mailtobolaji@gmail.com
 ```
**Add gif of being prompted for github credentials and entering them**\
Lastly, open the newly cloned folder in VScode\
**Add gif of opening repo folder in vscode**
