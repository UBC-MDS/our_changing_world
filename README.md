# Our Changing World!

![license
status](https://img.shields.io/github/license/UBC-MDS/our_changing_world)

***Learn more about how global population, life expectancy and per-capita Gross Domestic Product (GDP) have evolved over time***

Link to the dashboard: https://our-changing-world.herokuapp.com/

## Welcome!

First and foremost, a big warm welcome! :balloon::tada: :confetti_ball: :balloon::balloon:

Thank you for visiting the Our Changing World app project repository.

This document (the README file) is a hub to give you some information about the project. You can either get straight to one of the sections below, or simply scroll down to find out more.

* [About this project](#about-this-project)
* [Contributors](#contributors)
* [Description of "Our Changing World" App](#description-of-our-changing-world-app)
* [Downloading and Running locally](#downloading-and-running-locally)
* [Get Involved](#get-involved)

## About this project

### The problem
The world that we live in has dramatically changed over the past several decades. Global population, average life expectancy, and GDP per-capita have increased significantly across the globe. Yet, we continue to face important challenges such as inequity in growth rate of average life expectancy or GDP per-capita across different regions of the world. 

### The solution
To tackle the global scale problems of poverty, inequality, and access to health, there needs to be a nuanced understanding of our world through data. Within the ambit of the Sustainable Development Goals (SDGs), there is a growing need for production, usage, and understanding of statistics and other information about socio-economic
development at national, regional, and global levels.

This dashboard was created with the objective of making such pertinent fact-based data available to the world in a comprehensible format using customizable visualization of global development statistics using data from Gapminder Foundation: gapminder. ***The goal is to help governments, international organizations, researchers, and policymakers understand basic trends about the state of the world as a first step towards addressing global challenges outlined in the SDGs.*** A more detailed proposal of this project could be found [here](https://github.com/UBC-MDS/our_changing_world/blob/main/docs/proposal.md).

## Contributors

-   Vera Cui
-   John Lee
-   Rakesh Pandey
-   Nagraj Rao

## Description of "Our Changing World" App

The [dashboard](https://our-changing-world.herokuapp.com/) consists of 4 main sections: 

(i) "What do you want to know" panel on the upper left: Here, the user can choose a topic that they are interested in learning more about out of three choices: Population, Life Expectancy, and GDP per Capita. The user can also specify the year by using the scroll bar, which is available in 5 year intervals between 1952 and 2007.

(ii) A bubble map chart panel on the upper right: Here, a world map with data for each country is presented for the options selected in the "What do you want to know" panel.

(iii) A "World Ranking" panel on the bottom left: Here, a bar chart at the country level for the options selected in the "What do you want to know" panel is displayed in decreasing rank order. 

(iv) A "World Trend" panel on the bottom right: Here, a time-series plot is presented for each region of the world for the options selected in the "What do you want to know" panel.

All plots are automatically updated when new selections are made in the "What do you want to know" panel.  

![](https://github.com/UBC-MDS/our_changing_world/blob/documentation/img/gif_app.gif)

## Downloading and Running Locally

To download the contents of this GitHub page on to your local machine follow these steps:

1. Copy and paste the following link: `git clone https://github.com/UBC-MDS/our_changing_world.git` to your Terminal. 

2. On your terminal, type: `cd our_changing_world`.

3. To run a development instance locally, first create a virtualenv by typing: `conda create --name myenv_ourchangingworld`

4. Install the requirements from ***requirements.txt*** by typing: `pip install -r requirements.txt` 

5. Type the following command if the environment isn't automatically activated after Step 3: `conda activate myenv_ourchangingworld`

6. Launch ***app.py*** using the Python executable from the virtualenv: `python src/app.py`

7. Using any modern web browser, visit http://127.0.0.1:9090/ to access the app.

**Note that for Steps 3 - 6 to work smoothly, you have to be in the our_changing_world directory.**

## Get involved

If you have feedback for improvement (and we bet you do) or suggestions on any areas that we haven't yet thought of (and here we are certain you can), then please check out our [Contributing Guidelines](https://github.com/UBC-MDS/our_changing_world/blob/main/CONTRIBUTING.md).

If you want to report a problem or suggest an enhancement we would appreciate if you could `Open an Issue` on this github repository because then we can get right on it.

Please note that it's very important to us that we maintain a positive and supportive environment for everyone who wants to participate. When you join us we ask that you follow our [code of conduct](https://github.com/UBC-MDS/our_changing_world/blob/main/CONDUCT.md) in all interactions.

