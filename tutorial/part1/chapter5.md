# Chapter 5 - App Deployment

## Overview

__Heroku__ is a platform as a service (PaaS) that supports Python where you can deploy and manage public Dash applications. Heroku uses containers called "dynos" to deploy your app by packaging its code and dependencies and executing it in a virtualized environment in a way that's scalable according to the changing resource needs of your application. 

It's free to create a Heroku user account, and a Free tier is available for a basic app. Additional tier options support the specification needs of more complex apps or those requiring additional memory (RAM), and you can read more about [Heroku pricing](https://www.heroku.com/pricing).

```{note} Make sure you have set up Git version control on your project folder directory by following those steps in Stack Installation, and that you've successfully tested your Dash app locally on your computer.```

## Instructions

1.  Make a copy of your local development app project for deployment. 
    * This will need to be initiated with Git.
    * If you are using a GitHub repository, that can integrate with Heroku easily into a deployment pipeline.
    * Turn off debugging mode by changing your app.py run statement to ```debug=FALSE```.
2. Setup or log into a Heroku user account.
    1. From a web browser, [sign up](https://signup.heroku.com/dc) or [log in](https://id.heroku.com/login) if you have an existing account.
    2. Verify your identity for security purposes using one of Heroku's available verifaction methods.
    3. This takes you to your user account dashboard.
3. Setup the Heroku Command Line Interface CLI.
    1. Install Heroku CLI for your platform (macOS, Windows, or Ubuntu).
    2. From your command shell, use the ```heroku login``` command to log in to the Heroku CLI.
4.  Install the additional dependency ```gunicorn``` production server for Python web applications
    1. Use the ```pip install gunicorn``` command.
5.  Prepare the necessary additional files for deployment.
    1.  A Procfile with ```web: gunicorn app:server``` on a single line.
    2.  ```requirements.txt``` file describing your Python dependencies. Create this automatically with the command ```pip freeze > requirements.txt```. Be sure gunicorn now also appears in this file.  
6.  Initialize Heroku, add files to Git, and deploy.
    * You should now be able to view your app at ```http://my-dash-app.herokuapp.com``` (changing ```my-dash-app``` to what you have named your app.
