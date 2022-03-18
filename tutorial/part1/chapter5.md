# Chapter 5 - App Deployment

Using your Dash app on your computer is great, but the magic happens when you deploy your app so you can share it with your friends! __Heroku__ is a platform as a service (PaaS) that supports Python where you can deploy and manage public Dash applications. Heroku uses containers called "dynos" to deploy your app by packaging its code and dependencies and executing it in a virtualized environment in a way that's scalable according to the changing resource needs of your application. 

This example uses a Heroku account and Git. It's free to create a Heroku user account, and a Free tier is available for a basic app. Additional tier options support the needs of more complex apps or those requiring additional memory (RAM), and you can read more about [Heroku pricing](https://www.heroku.com/pricing).


## Learning Intentions

In this chapter we intend you to learn:

```{admonition} Learning Intentions

- how to turn off interactive debugging mode
- how to install Heroku Command Line Interface (CLI)
- how to deploy your Dash application to the web publicly using CLI
```

```{note} 
Make sure you have set up Git version control on your project folder directory by following those steps in Git documentation from chapter 0, and that you've successfully tested your Dash app locally on your computer.
```

## App at the Start

As a framework for this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like when you start.


## Turn off Debugging mode

Open your app.py script file and turn off the interactive debugging mode by changing your run statement from ```debug=True``` to ```debug=False```.

Your last lines of code should now look like this.

```
# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
```

Save and close app.py.


## Log in to Heroku user account

From a web browser, [log in](https://id.heroku.com/login) or sign up if you are new to Heroku.

- Follow the prompts to verify your identity for security purposes using one of Heroku's available verifaction methods.
- This takes you to your user account dashboard in your web browser.

Install the Heroku Command Line Interface (CLI).

[The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) article provides instructions for installation and first time setup on multiple computer platforms (macOS, Windows, or Ubuntu).

In your command shell, type the command ```heroku login``` to connect the Heroku CLI to your Heroku account.

```{note} 
If you have not already logged into your Heroku user account, this will open a new window in your web browser where you can follow the promts to log in.
```


## Install the Green Unicorn ```gunicorn``` Web Server Gateway Interface (WSGI)

For UNIX systems, you will need an additional dependency called ```gunicorn``` which is a Python WSGI HTTP Server that handles Python web application traffic for UNIX systems.

[Gunicorn installation](https://gunicorn.org/)

Type the ```pip install gunicorn``` command in your command shell.
    

## Prepare the necessary additional files for deployment.

Make a __Procfile__ *without a file extension*. This file tells Heroku all the commands that must be executed by the app on startup.

Type the following single line of text in the first line of the file.

```web: gunicorn app:server``` 

```{warning} Make sure the first letter '_P_' is capitalized in _Procfile_ and that you spell it exactly that way or Heroku cannot recognize it.
```

Make a ```requirements.txt``` text file describing your Python dependencies. 

Type only the following in the file, with all of the packages your app requires to run each on its own single line, replacing the version numbers to match the packages you have installed and are using with your app.

```
python==3.9.11
dash==2.2.0
dash_bootstrap_components==1.0.2
plotly.express==0.4.1
pandas==1.3.4
gunicorn==20.1.0
```

```{note} In a later chapter as part of a more complex deployment process, you will learn how to create this file automatically with the command ```pip freeze > requirements.txt``` while working in a virtual environment.
```

## Add files to Git

Type these commands in your shell to update changes with git version control tracking.

See all the changed files available.
```
git status
```

Add all of the listed files to git to be tracked.
```
git add -a
```
Commit file changes to git.
```
git commit -m "type a brief message describing updates here"
```

Push changes to git master branch in your repository.
```
git push
```

## Create and initialize Heroku Remote application

From your app's root directory in your shell, type the following command.
```
heroku create -a app
```

For more information, see Heroku's [Deploying with Git](https://devcenter.heroku.com/articles/git) documentation. 


## Deploy

Type the following command in your shell to deploy your app to Heroku using the default Python Buildpack.

```
git push heroku main
```

This should return the result _Initializing repository, done._
You should now be able to view your app at ```http://my-dash-app.herokuapp.com``` (changing ```my-dash-app``` to the name of your app.


## Fix errors

Common deployment errors you could encounter for this example app include:
- Missing a package dependency in your requirements file


## App at the end

At the end of this chapter, [here is a zipped file](https://sportsnet.ca) of what your app should look like.
