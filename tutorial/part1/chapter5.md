# Chapter 5 - App Deployment


Start with this skeleton app from Chapter 4.


---

## Overview

In this chapter you will learn how to deploy your Dash application to the web publicly so you can share it with your friends. This example uses a Heroku account and Git.

__Heroku__ is a platform as a service (PaaS) that supports Python where you can deploy and manage public Dash applications. Heroku uses containers called "dynos" to deploy your app by packaging its code and dependencies and executing it in a virtualized environment in a way that's scalable according to the changing resource needs of your application. 

It's free to create a Heroku user account, and a Free tier is available for a basic app. Additional tier options support the needs of more complex apps or those requiring additional memory (RAM), and you can read more about [Heroku pricing](https://www.heroku.com/pricing).

```{note} 
Make sure you have set up Git version control on your project folder directory by following those steps in the Stack Installation chapter, and that you've successfully tested your Dash app locally on your computer.
```


---

## Instructions


### Turn off Debugging mode

1. Open your app.py script file and turn off the interactive debugging mode by changing your app.py run statement to ```debug=FALSE```.

(code detail here)

2. Save and close app.py.


### Heroku CLI section --figure out best way to order this (install CLI first or login with browser first with note that login command will take you there also)

3. Setup or log into a Heroku user account.
    1. From a web browser, [sign up](https://signup.heroku.com/dc) or [log in](https://id.heroku.com/login) if you have an existing account.
    2. Verify your identity for security purposes using one of Heroku's available verifaction methods.
    3. This takes you to your user account dashboard.

4. Setup the Heroku Command Line Interface CLI.
    1. Install Heroku CLI for your platform (macOS, Windows, or Ubuntu).
    2. From your command shell, use the ```heroku login``` command to log in to the Heroku CLI.

5.  Install the additional dependency ```gunicorn``` production server for Python web applications.
    1. Use the ```pip install gunicorn``` command.
    
6.  Prepare the necessary additional files for deployment.
    1.  A Procfile *without a file extension* with ```web: gunicorn app:server``` in it on a single line.
    2.  A ```requirements.txt``` file describing your Python dependencies. Be sure gunicorn now also appears in this file. (add quickest way to add only the few packages we need, since we will not use a virtual environment up to this chapter, so we don't want to use pip freeze)
    (move this to a later chapter for full web deployment: Create this automatically with the command ```pip freeze > requirements.txt```.   

7.  Initialize Heroku, add files to Git, and deploy. (add details)

You should now be able to view your app at ```http://my-dash-app.herokuapp.com``` (changing ```my-dash-app``` to the name of your app.

8.  Fix errors.
(add details about common deployment errors for example app, i.e. forgetting to add a package dependency in your requirements file.)

---

## Outcome

When you've completed this chapter, your app should be visible on the web by anyone with its URL link. 

It should look like this.
