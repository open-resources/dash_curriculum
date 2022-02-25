# Chapter 2 (Group 1)

## Procedure for Activity together

- Talk about what challenges people have when first being exposed to Dash
- Refer back to the Dash Tutorial, and identify areas where people can be "taught" some concepts 
- Order in which they need to be taught dash
- Which parts to focus on when installing stack

Outcome of this activity:

- an ordered and unordered list of topics/sections that belong in this first chapter

### Reminder of the "intended order"

Chapter 2: Getting Started with Dash

- Structure of a Dash app
  - Libraries
  - Data
  - Layout
  - Callback
   
- Installation and setup
  - 
- Create your first Dash app
  ```
  from dash import Dash
  
  app = Dash(__name__)  # Instantiate your app
  
  app.layout = html.Div([
      html.Label("Hello to my first App")
  ])
  
  # @callback(....) # more about this later
  
  if __name__=='__main__':  # Run your App
      app.run_server()
  ```
- Live updates and debugging
  - how to stop your app (and why you should) (Ctrl+C)
  - how to update your app (Ctrl+C and then re-run)
  - how to turn on "live updating" (with debug=True) and what this means (i.e. what happens if you have a syntax error and your app crashes)
