# Improvements made for Milestone 4

For Milestone 4, 9 improvements were made by accommodating the comments from the TA and reviewers, and adding more functionality and consistency to the apps.


### 1. Comments from TAs

**(1) Comments:** I agree that changing the world map to a heat map with different scale for each of the variables or altering the bubble sizes might show the differences between countries a bit better.

- **Our response:** The heatmap was meant for showing association amongst the variables and not in place of the world map. However, given the few variables in our dataset, and no variation of GDP per capita and Life Expectancy with Population, we deemed it prudent to show the evolution of the association between GDP per capita and Life Expectancy as a bubble chart, adjusted by Population. @[commit 16dab](https://github.com/UBC-MDS/our_changing_world/commit/16dab20f3f32d3365d8ef35e66bb1b1869d3c8fc)

**(2) Comments:** Code is organized but could be commented better.

- **Our response:** Thank you. This has been done. @[commit fd05d](https://github.com/UBC-MDS/our_changing_world/commit/fd05d0ef8dd5dd21a3a48599909ddf99aa896124), [commit f1641](https://github.com/UBC-MDS/our_changing_world/commit/f1641477f1993209565e0ea81ca89dd75ffba417)

**(3) Comments:** Code of conduct is missing contact information in case of a violation

- **Our response:** Thank you. Contact Information has been added. @[commit 468dc ](https://github.com/UBC-MDS/our_changing_world/commit/468dcb4f325c894b9a45a1ac96555ea347470e96)

### 2. Comments from Reviewers

**(1) Comments:** Overall the text of the graphs are easy to read. One exception is for the world ranking graph, since the graph is extra long in length, it is hard to see the x-axis label at first glance.

- **Our response:** Position of X-axis of "World Ranking Chart" has been moved to the top as suggested by the reviewer. @[commit ceb6fa](https://github.com/UBC-MDS/our_changing_world/commit/ceb6fafcc535220582eabc5d4f9228176843135c)

**(2) Comments:** The world map graph lacks a clear title label and labels for the colors. (The colors are labeled in the world trend graph below but it would be nice to have them there too) 

- **Our response:** A legend was added to "World Map" as suggested by the reviewer.@[commit 39325](https://github.com/UBC-MDS/our_changing_world/commit/3932574a4ea920a1e292560ccdb6e39bad6248b4)

### 3. Other improvements

**(1)** Added more interactivities to the app @[commit f0e59](https://github.com/UBC-MDS/our_changing_world/commit/f0e59bf2a9b45a4f73b19dd0ede1c50f03c7b508)

**(2)** Modified the sizes of the graphs to make them fit better in the monitor. @[commit 3e1ce](https://github.com/UBC-MDS/our_changing_world/commit/3e1ce8ee0773fab983c3613a4d78ad6bcbbf4e9e)

**(3)** Matched the colors by country, and formated axis @[commit 0ca14](https://github.com/UBC-MDS/our_changing_world/commit/0ca1490e72a2b45192a9e04c1d0f3f7fc7c3b889)

**(4)** New GIFs were included in READMEs for both Python and R Repo @[commit 35feb](https://github.com/UBC-MDS/our_changing_world/commit/35febed918f4fbbd0ff9f431e8bff9ebc0870726), [commit d3acb](https://github.com/UBC-MDS/our_changing_world/commit/d3acb2a31ddf0b407f94cd4228a4d7ae741fe4a6)
