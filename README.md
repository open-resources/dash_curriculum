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

## Chapter 0: Prerequisites

- checklist of things they need
- install stack

## Part I: Introduction to Dashboards in Dash

- Summary and overview of this part
- Learning Intentions

### Chapter 1: What is a dashboard?

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
 - Dash Core components
   - Markdown
   - Dropdown
   - Checkbox
   - Slider
   - Graph
 - Design App layout
   - Container: Dash Bootstrap Components
   - Row and Col: Dash Bootstrap Components

### Chapter 4: Linking Dash components

 - Introduction to decorators in Python
 - Callback decorators in Dash
   - Input
   - Output
   - Component_id
   - Component_property
 - Setting up a callback
   - Dropdown and Graph
   - Slider and Graph
 
### Chapter 5: Deploying a Dash app to the Web

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

### Chapter 7: Wrangling data

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

## Part III: Polishing your Dash application

- Summary and overview of this part
- Learning Intentions
 
### Chapter 9: Advanced Layout and Styling

 - Creating a layout component inside a callback
 - More Dash Bootstrap Components
 - Dash HTML components
 - Sytling app with Dash Bootstrap Components
  
### Chapter 10: Advanced Callbacks

 - States
 - Multiple buttons: callback_context
 - Multiple outputs and inputs

### Chapter 11: Advanced Components

- Advanced DBC
- Advanced DCC
 - RangeSlider
 - Datepicker
 - Interval
 - Store

### Chapter 12: DataTable

 - Intro to the DataTable: creating a basic DataTable
 - Linking dataTable to graph
 - Editing the DataTable
 - Other importnat DataTable props

## Part IV: Publishing your Dash Application

- What you will learn in this part
- Learning Intentions

### Chapter 13: Full Deployment

 - Components of deployment
   - Procfile
   - requirements.txt
   - Dockerfile
   - Heroku build pipeline 
 - Deploying to Pythoanywhere ? (Optional)

### Chapter 14: Improving app performance and multi-page app

 - Callback graphs to asses speed
 - Actions to improve app speed
 - Efficiency
 - Building multi-page app
 
### Chapter 15: Gallery and Template

- [Dashboard Layouts](https://github.com/matthewconnell/dashr_sample_layouts)
  - Template 1
  - Template 2
  - Template 3  
- [Case Studies](https://dashboard-showcase-532.herokuapp.com/)
 - Case Study 1
 - Case Study 2
