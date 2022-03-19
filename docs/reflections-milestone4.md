# Milestone 4 Reflection


### Accomplishments of dashboard deliverables

1. Both our DashPy and DashR dashboards showcase the same combination of visualizations including a bubble map, a bubble chart, a line chart, and a bar chart. The feedback from both the peer review and TA feedback was that our app was aesthetically pleasing, so we retained the format whilst making minor modifications such as changing the globe format of the bubble map, changing the size of the panels to adapt to most laptop screen dimensions, and changing the size of the bubbles proportional to the value for that variable. The lesson learned here, borrowing a quote from Leonardo Da Vinci, is that "simplicity is the ultimate sophistication". A simple visualization can go a much longer way in the business world to communicate an idea than a complicated output that is not as easily interpreted.

2. We went one step further by adding a scatterplot to showcase the visual association between two variables, based on the feedback from the peer review process of including interactions between our variables. This has enhanced our own understanding of the tremendous progress made in the increase of life expectancy across countries between 1952 and 2007, despite the looming inequality based on GDP per capita, which is particularly stark in the case of African countries. The lesson learned here is that visualizing associations can be a first step towards statistical modeling of relationships across variables.

3. Ensuring that users learn something different from each panel was of utmost importance to us. We therefore spent significant time in each milestone planning what plots would demonstrate different information, where to place them, what tools and labels to include, alongside brainstorming best practices to significantly avoid overlap in the information gained from each panel. 


### Differences between DashPy and DashR

1. The scales are slightly different between DashPy and DashR. However, due to the tooltip, we believe that this is not a major issue.

2. At present, we can export individual plots in DashR but not DashPy. Should time permit, we would like to refine DashPy to enable this feature. 

3. Plots are in different color themes for DashPy and DashR apps. 


### Limitations and future improvements

1. Some minor tweaks can be made to the overall web aesthetic design for both DashR and DashPy such as aligning fonts, axis values etc.

2. There are some challenges with zooming in and out in each plot. For example, once I have zoomed into the plot, there is no way to go back to the original view other than refreshing the page. The manual zoom function tends to alter the x and y axis values being displayed. 

3. DashPy can be finetuned to allow exporting individual plots instead of all three together for more flexibility.

4. Another futuristic goal would be to allow users to create their own set of customized charts, based on the user's preferences of x and y axis alongside type of graph desired. We could have general layouts for each type of chart that is available in the statistical world, and allow users to create their own visualizations rather than forcing them to only go with the axes we have pre-selected. 

5. Another possible improvement can be using more comprehensive gapminder dataset with more categories. It would be also great to include another tab for country-specific informations.  

6. The bubbles on the world map look similar for life expectancy because the gaps of life expectancy across different countries within the same time period changes marginally compared to population and GDP. Perhaps, we need to design a function so as to show significant changes in life expectancy with more noticeable changes in the bubble size.
