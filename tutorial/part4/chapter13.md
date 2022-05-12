# Chapter 13: Improving app performance

## What you will learn

By now, you have everything together to get your first app up and running using even advanced components, layouts and callbacks. As dashboards are designed for data analysis and visualisations at some point you might run into efficiency constraints when the amount of data you are working with gets growing. To circumvent any possible performance lacking this chapter will give you some insights on improving your app performance.

```{admonition} Learning Intentions
- Preprocessing data
- Higher Performing Plotly graphs
- Caching
```

## 13.1 Preprocessing data
the main idea is to give two examples on data wrangling. Once where the data wrangling takes place before initializing the app, once after or during a callback. The plan is to show some difference in processing time.

## 13.2 Higher Performing Plotly graphs
So far, we have used the `plotly.express` library to implement our graphs. This is a very easy and convenient way to do so. However, most plotly charts are rendered with SVG (Short for Scalable Vector Graphics). This provides crisp rendering, publication-quality image export as SVG images can be scaled in size without loss of quality, and wide browser support. Unfortunately, rendering graphics in SVG can be slow for large datasets (like those with more than 15k points). To overcome this limitation, `plotly.js` has WebGL (Short for Web Graphics Library) alternatives to some chart types. WebGL uses the GPU to render graphics which make them higher performing. Three WebGL alternatives are the follwing:

- [`ScatterGL`](https://plotly.com/python/line-and-scatter/#large-data-sets): A webgl implementation of the scatter chart type.
- [`Pointcloud`](https://plotly.com/python/reference/#pointcloud): A lightweight version of scattergl with limited customizability but even faster rendering.
- [`Datashader`](https://plotly.com/python/datashader/): A webgl implementation of the heatmap chart type.

## 13.3 Caching
[memoization](https://dash.plotly.com/performance#memoization)

## other potential ideas if need be:
https://community.plotly.com/t/how-to-improve-the-loading-speed-of-my-page/17197

https://community.plotly.com/t/is-there-a-way-to-increate-the-performance-of-my-dash-web-app/23117/10

https://github.com/ijl/orjson

## Summary
