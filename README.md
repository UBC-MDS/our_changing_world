Our Changing World!
================

![license
status](https://img.shields.io/github/license/UBC-MDS/our_changing_world)

## Contributors

-   Vera Cui
-   John Lee
-   Rakesh Pandey
-   Nagraj Rao

## Motivation

Our role: Data scientist consultancy firm <br> *Target audience:
Governments, International Organizations, Researchers, and Policymakers*

The world as we know today has dramatically changed over the past
several decades. Global population has increased from 2.4 billion to 6.3
billion between 1952 and 2007. Median global life expectancy, which
stood at 45.1 years in 1952 has dramatically risen to 71.9 years in
2007. Between the same time period, global per-capita Gross Domestic
Product (GDP) has also grown from USD 1,969 to USD 6,124.

However, the world still faces important challenges. There are
significant differences in several global development indicators across
regions. For example, the median life expectancy in Africa stood at 52.9
years, compared to Europe at 78.6 years in 2007. Despite significant
growth in per-capita GDP over the years, there continues to be an
unequal distribution of wealth, with Democratic Republic of Congo having
a per-capita GDP of USD 277.5, compared to Norway which had a per-capita
GDP of 49,357.19 in 2007.

In order to tackle global level problems of poverty, inequality, and
access to health, there needs to be an improved understanding of our
world through data. Within the ambit of the Sustainable Development
Goals (SDGs), there is a growing need for production, usage, and
understanding of statistics and other information about socio-economic
development at national, regional, and global levels.

This dashboard was created with the objective of making such pertinent
fact-based data available to the world in a comprehensible format using
customizable visualization of global development statistics using data
from the **Gapminder Foundation**. The goal is to help governments,
international organizations, researchers, and policymakers draw
evidence-based conclusions about the state of the world as a first step
towards addressing global challenges outlined in the SDGs.

## Data Description

The dataset used is [`gapminder`](https://www.gapminder.org/) which
includes 1704 rows of entries and 6 features (`country`, `continent`,
`year`, `lifeExp`, `pop`, `gdpPercap`). Basically, it describes how the
globe (142 countries) has changed spanning from 1952 to 2007 in the
aspects of life expectancy, population and economy. As shown in
`Tabel 1`, the summarized statics of the dataset tell of huge gaps in
all of 3 dimensions.

|         | Life expectancy | Population | GDP per capita |
|:--------|:---------------:|:----------:|:--------------:|
| Min.    |      23.60      | 6.001e+04  |     241.2      |
| 1st Qu. |      48.20      | 2.794e+06  |     1202.1     |
| Median  |      60.71      | 7.024e+06  |     3531.8     |
| Mean    |      59.47      | 2.960e+07  |     7215.3     |
| 3rd Qu. |      70.85      | 1.959e+07  |     9325.5     |
| Max.    |      82.60      | 1.319e+09  |    113523.1    |

Table 1: Summary of numeric features of the dataset

`Figure 1` also shows the tremendous changes of these 3 features over
last 50 years. To be more specific, all the continents have extended
longevity and experienced population and economic booms.

![EDA analysis of Gapminder](README_files/figure-gfm/eda2-1.png)

Figure 1: EDA analysis on `Gapminder`

## Research Questions being explored

Salma is an economist with the World Bank, a large multi-lateral
international development organization who wants to answer three
research questions:

1.  How has global population grown between 1952 and 2007 across
    different geographies (both country and continent level)?
2.  How has per-capita GDP (in USD) changed across the world, and is
    there a skewed distribution across geographies (both country and
    continent level), indicating inequality?
3.  How has median life expectancy (in years) evolved over time across
    the world, and has the growth rate been different across geographies
    (both country and continent level)?

While her overall objective is to identify factors that explain growth
and inequities for these three variables and devise global policies that
can address these inequalities, the three research questions stated
above serve as a starting point, permitting the conduct exploratory data
analysis to understand general trends over time.

When Salma logs onto the “Our Changing World!” app, she will be able to
see a dynamic visualization of the evolution of these three indicators
across countries and by continent. By filtering across countries and
years, she can conduct country-level or continent-level comparisons
which will facilitate ranking countries on these indicators. Noticing
inequalities across regions, she hypothesizes that growth in GDP and
life expectancy is slower in some economies due to poor governance and
corruption. Given that information on poor governance and corruption are
not captured in her research dataset, Salma decides that she needs to
conduct a follow-on data collection activity on these two variables to
estimate a causal impact of poor governance and corruption on population
growth, increase in GDP per capita, and rise in median life expectancy.

## Running locally

To run a development instance locally, create a virtualenv, install the
requirements from `requirements.txt` and launch `app.py` using the
Python executable from the virtualenv.

## Deploying on Heroku

Use `make image` to create a Docker image. Then, follow [these
instructions](link_to_url) to deploy the image on Heroku.
