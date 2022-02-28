# Chapter 3 - Dash Components and Layouts
## Overview

In this chapter we explore Dash **layouts** and the **components** that make up the layout.

## Dash Layout
Dash applications are comprised of 2 parts:
- Layout: What the application looks like
- Callabacks: Interactivity of the application

The **layout** is made up of **components**.  Let's make a minimal Dash application to demonstrate this concept:
<details>
  <summary>Minimal Dash App</summary>
  
Create **app.py** in the `tutorial/part1` directory:

![Make app.py](../assets/p1_s3/make_app_py.png)

Copy/paste the minimal Dash app code:  
```python
# Import Python libraries
from dash import Dash, html 

# Create a Dash application
app = Dash()
# Create the layout of the app
app.layout = html.Div("This is a HTML Div component")
# Run the app
app.run_server()
```

Now **Run/Debug** the code:
![Running minimal Dash app](../assets/p1_s3/run_minimal.png)


Open a web browser, enter http://127.0.0.1:8050/ in the address bar, and you should see our minimal application:
![Display minimal Dash app](../assets/p1_s3/display_minimal.png)
</details>

