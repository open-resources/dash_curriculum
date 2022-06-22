# Chapter 14: Introduction to Multi-page Apps

## What you will learn
In this chapter we will introduce multi-page apps which will allow us to build more complex apps.
```{admonition} Learning Intentions
- How to structure multi-page apps project
- Navigate between apps
```

## Why separate app into multiple pages?
  - <b>Advantages</b>
    - Easy to develop small apps and features
    - Easy to troubleshoot bugs
    - New apps can be built on to old apps
  - <b>Disadvantages</b>
    - Extra infrastructure is required
    - Slightly more complex apps

## Structure of Multi-page Apps
  - Storyboarding and building out pages
    - <b>Do we need this?</b>
  - File and folder layouts
    - Create main `app.py` file is root directory
    - Create subdirectory `/pages`
      - Add individual apps to `/pages` directory
        - Each page needs to contain a `layout`
        - Registering pages
          -  call ```dash.register_page(__name__)```
          - ```dash.page_registry``` is an `ordered dictionary` containing each page's paths, name, title, etc.
  - Callbacks
  - Building out the app.py file
