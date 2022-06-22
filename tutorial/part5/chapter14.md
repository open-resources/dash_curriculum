# Chapter 14: Introduction to Multi-page Apps

## What you will learn
In this chapter we will introduce multi-page apps which will allow us to build more complex apps.
```{admonition} Learning Intentions
- How to structure multi-page apps project
- Navigate between apps
```

## Why separate into multiple pages?
  - Advantages
    - Easy to develop small apps and features
    - New apps can be built on to old apps
  - Disadvantages
    - Extra infrastructure is required
    - Slightly more complex apps

## Structure of Multi-page Apps
  - Storyboarding and building out pages
  - File and folder layouts
    - Create subdirectory `./pages`
      - Each page needs to 
        - contain a `layout`
  - Registering pages
    -  call ```dash.register_page(__name__)```
    - ```dash.page_registry``` is an `ordered dictionary` containing each page's paths, name, title, etc.
  - Callbacks
  - Building out the app.py file
