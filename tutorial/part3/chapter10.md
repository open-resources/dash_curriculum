# Chapter 10: Advanced Callbacks

## What you will learn

You have already learned about callbacks in chapter 4. Now, it is time to upskill and deal with more advanced callbacks. You will learn how to circumvent different components to trigger a callback action immediately as well as how to handle multiple outputs and inputs in one callback.

```{admonition} Learning Intentions
- Multiple outputs and inputs
- States
```

## Multiple outputs and inputs

You might want to have a graph that should be linked to more than one component, changing or affecting different dimensions of your graph. If you think the other way around, you might want to have several graphs that should be affected by the same component. Here is where multiple outputs and inputs come into play.

```{attention}
In addition to a much cleaner and shorter code, note that assigning two different callbacks the same component as an output argument is just not allowed by dash.
```



## States

So far, we had linked components of your app together which immediately affected each other. In a more advanced setup it might be useful though to circumvent this direct relationship. You might first want to have all of the input arguments together before your outpout is triggered. This could be helpful for any kind of forms. For this purpose there is a third argument that can be used within the callback decorator, the state.

## Summary
