# Chapter 2: Getting Started with Dash

- Structure of a Dash App
  -  Dash is a Python framework which allows to build data visualization apps in pure Python. Dash applications are rendered and accessible in a web browser
  -  Dash apps are rendered and accessible in a web browser and require the developer to follow some folder structure and naming conventions. A simple Dash App is normally composed by the following elements:
      -  an "App" object
      -  the app layout: i.e. the objects that we intend to show in the dashboards
      -  data
      -  some statements to run the app (run_server)
      -  callbacks: functions that can be defined to enable user interaction, e.g. allow the user to filter a chart by geography
      -  (any other additional app asset such as: "css" files to further customise the layout; any file that we want to show in the app, e.g. images or icons)

- Installation and setup
- Create your first Dash app
- Live updates and debugging
  - how to stop your app (and why you should) (Ctrl+C)
  - how to update your app (Ctrl+C and then re-run)
  - how to turn on "live updating" (with debug=True) and what this means (i.e. what happens if you have a syntax error and your app crashes)
  - error message if something is missing (example where we didn't import html)

