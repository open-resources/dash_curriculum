# Chapter 3 - Dash Components and Layouts
## Overview

In this chapter we explore Dash **layouts** and the **components** that make up the layout.

## Dash Layout
Dash applications are comprised of 2 parts:
- Layout: What the application looks like
- Callabacks: Interactivity of the application

The **layout** is made up of **components**.  Let's make a small Dash application to demonstrate this concept.  Create **app.py** in the `tutorial/part1` directory:
(TODO- PIC OF MAKING FILE)

Copy/paste the following code:
```python
from dash import Dash, html

app = Dash()

app.layout = html.Div("This is a HTML Div component")

app.run_server()
```
(TODO- PIC OF RUNNING FILE)

Open a web browser, enter **http://127.0.0.1:8050/** in the address bar, and you should see our minimal application:
(PIC)

