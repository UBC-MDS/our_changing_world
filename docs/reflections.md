# Milestone 2: Reflection

### Current status of the dashboard

Our dashboard has gone through multiple iterations of planning, implementation, and modification, wherein, our objective has consistently been to provide an easy-to-understand visual representation of the data. The dashboard consists of four sections:

1. A "What do you want to know" panel, where the user can choose a topic that they are interested in (Population, Life Expectancy, and GDP per Capita), alongside specifying the year through a scroll bar, available in 5 year intervals between 1952 and 2007. An option for changing the theme of the dashboard is also provided.

2. A bubble map chart panel, where a world map with data for each country is presented. The bubbles are proportional to the magnitude of the value of the variable for each country. 

3. A "World Ranking" panel, where a bar chart at the country level for the options selected is displayed in decreasing rank order. The ranking clarifies the relative position of countries for each combination of indicator and year.

4. A "World Trend" panel, wherein, a time-series plot is presented for each region of the world for the options selected. A dotted bar line gives us the value for each region for the selected year and indicator combination.

To ensure interactivity, all plots are automatically updated when new selections are made in the "What do you want to know" panel.


### Advantages of our dashboard

1. Provides simple representation of three critical global development indicators in an easy-to-understand format.

2. The ability to change theme, which is useful for people preferring different color backgrounds (for example black or white), alongside changing font to suit their preferences.

3. A World Ranking that doesn't just show a bar graph representation but also presents the actual rank of countries.

4. A Year scrolling feature to understand trends in our data.

### Limitations and areas for improvement

1. At a macro level, to better understand our evolving world, one thing that could be done to improve this is understanding correlations between the three variables. This would involve adding to the backend to make this possible and setting up additional screens or charts to display this.

2. Right now, our dashboard allows changing years manually. It would be optimal to have an animated scrolling time series with a simple "Play button".

3. In the map, the countries values could be presented as a heatmap which would make the visual even more appealing.

4. A tooltip could be added to the "World Trend" chart to display values at each point of the graph.

5. Whilst a herculean task, it would be nice to have two separate levels of analysis: one at the regional level, and another at the country level. At present our charts are fixed to either being at the country or regional level. It would be beneficial for the user to select this unit of analysis.

6. On a micro level, we could try and figure out new designs that would improve the aesthetic layout of the graph across different machines (PC/Mac/Linux/Android/Apple) so that the dimensions are customized by device, prevented crowding and more user-friendly navigability and display. 

7. The bubbles for life expectancy on the map look very similar for a given year, but vary across years. Perhaps bubble sizes should be adjusted to different ranges.

8. Finally, the field of global development is vast, and the Sustainable Development Goals track over 300 indicators. In an ideal world, we would have more indicators to further enhance our understanding of the world that we live in!
