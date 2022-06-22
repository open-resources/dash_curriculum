# Overview of Dash Curriculum
 * note: for creation of gifs- [windows software](com), [mac software](https://getkap.co/). 
## Preface

- What is this resource?
- [Learner Personas](https://teachtogether.tech/en/#s:process-personas)
- How to use this resource?
- Who created this resource?
  - Introduction to the team
  - What is Plotly and Dash?
- Acknowledgements

## Chapter 0: Installation Stack

- checklist of things they need
- install stack

## Part I: Introduction to Dashboards in Dash

- Summary and overview of this part
- Learning Intentions

### Chapter 1: What is a Dashboard?

- Sample Dashboards
- Theory on Dashboards
- Principles of effective dashboard design
- Usability and Accessibility of Dashboards
- Web app versus dashboard

### Chapter 2: Getting Started with Dash

- Structure of a Dash app
- Installation and setup
- Create your first Dash app
- Live updates and debugging
  - how to stop your app (and why you should) (Ctrl+C)
  - how to update your app (Ctrl+C and then re-run)
  - how to turn on "live updating" (with debug=True) and what this means (i.e. what happens if you have a syntax error and your app crashes)

### Chapter 3: Dash Components and Layouts

 - What you will Learn
 - Dash Components
   - Markdown
   - Button
   - Dropdown
   - Checkbox
   - Slider
   - Graph
 - Design App layout
   - Container: Dash Bootstrap Components
   - Row and Col: Dash Bootstrap Components

### Chapter 4: Linking Dash Components

 - Introduction to decorators in Python
 - Callback decorators in Dash
   - Input
   - Output
   - Component_id
   - Component_property
 - Setting up a callback
   - Dropdown and Graph
   - Slider and Graph
 
### Chapter 5: App Deployment

 - Basic deployment to Heroku

## Part II: Data Visualization

- Summary and overview of this part
- Learning Intentions

### Chapter 6: Working with Data in Dash

- From excel or csv to pandas df
- Loading a dataframe from a URL
- Creating our own pandas df 
- Using data from an API
- "do wrangling inside app" --> show that it is slow

### Chapter 7: Wrangling Data

- "do wrangling separately in py files" --> show that it's faster
- Case Study: Select a dataset
- Basic operations with pandas
- Cleaning, processing, wrangling
- Preprocessing files

### Chapter 8: Data Visualization

 - Principles of Effective Visualizations
 - Introduction to Plotly Express
 - Plotly Express graphs
   - scatter plot
   - line plot
   - bar plot
   - etc...
 - Incorporting PX graphs in a Dash app 
 - References and resourcres

### Chapter 9: DataTables

 - Intro to the DataTable: creating a basic DataTable
 - Linking dataTable to graph
 - Editing the DataTable
 - Other importnat DataTable props

## Part III: Advanced Dash

- Summary and overview of this part
- Learning Intentions
 
### Chapter 10: Advanced Callbacks

 - States
 - Multiple buttons: callback_context
 - Multiple outputs and inputs

### Chapter 11: Additional Components

- Advanced DBC
- Advanced DCC
   - RangeSlider
   - Datepicker
   - Interval
   - Store

## Part IV: Polishing Dash Apps

### Chapter 12: Advanced Styling and Layout

 - Creating a layout component inside a callback
 - More Dash Bootstrap Components
 - Sytling app with Dash Bootstrap Components
  
### Chapter 13: Improving App Performance

- Callback graphs to asses speed
- Actions to improve app speed
  - Sharing data between callbacks(?)
- Efficiency

## Part V: Multi-page Apps

### Chapter 14: Introduction to Multi-page Apps

- Why separate into multiple pages?
  - Advantages of multi-page apps (lower load times, less processing, more modular pages, more focused content, easier to collaborate in teams)
  - Disadvantages of multi-page apps (increased maintenance effort/time, complex structure, potentially some repeated code, etc...)

- Structure of Multi-page Apps
  - Storyboarding and building out pages
  - File and folder layouts
  - Registering pages
  - Callbacks
  - building out the app.py file

### Chapter 15: Making Multi-page Apps

- A few words on what multipage layouts are possible
- Building multi-page app examples

## Appendix

### Gallery and Template

- [Dashboard Layouts](https://github.com/matthewconnell/dashr_sample_layouts)
  - Layouts with control panels and graphs
    - Template 1: Controls-left, Graph-right
    - Template 2: Controls-bottom, Graph-top
  - Layouts with navigation panels and Graphs
    - Template 1: Navigaton-right, Graph-left
    - Template 2: Navigaton-top, Graph-bottom 
  - Cpmbining nnavigation and control panels
    - Template 1: 
    - Template 2: 

- [Case Studies](https://dashboard-showcase-532.herokuapp.com/)
 - Case Study 1
 - Case Study 2

## Part X: Automations and Deployments

- What you will learn in this part
- Learning Intentions
- 
### Chapter XX: Full Deployment

- Components of deployment
  - Procfile
  - requirements.txt
  - Dockerfile
  - Heroku build pipeline 
- Deploying to Pythoanywhere ? (Optional)

### Chapter XX: Continuous Integration/Deployment

- Testing
- Setting up a pipeline
- Github Actions
