import numpy as np
import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO

import altair as alt
import plotly_express as px
from vega_datasets import data

# stylesheet with the .dbc class
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

app = Dash(
    __name__, external_stylesheets=[dbc.themes.SKETCHY, dbc.themes.CERULEAN, dbc_css]
)

app.title = "Our Changing World!"

# create server for heroku
server = app.server

# set altair theme
alt.themes.enable("urbaninstitute")

# create filters
# gapminder datset
gapminder = px.data.gapminder()
years = gapminder.year.unique()

###### Header ########
header = html.H4(
    "Our Changing World!",
    className="h1 bg-secondary bg-gradient-secondary p-2 mb-2 text-white text-center",
)
###### App Layout #######

## Filter Layout
target_filter = html.Div(
    [
        dbc.Label("What do you want to know?", html_for="dropdown", className="h4"),
        dbc.RadioItems(
            id="target-filter",
            options=[
                {"label": "Population", "value": "pop"},
                {"label": "Life Expectancy", "value": "lifeExp"},
                {"label": "GDP per Capita", "value": "gdpPercap"},
            ],
            value="pop",
            inline=True,
        ),
    ],
    className="mb-4",
)

year_filter = html.Div(
    [
        dbc.Label("Your Year of Interest", html_for="year-slider", className="h4"),
        dcc.Slider(
            id="year-slider",
            min=years[0],
            max=years[-1],
            step=5,
            tooltip={"placement": "bottom", "always_visible": True},
            marks={int(x): {"label": str(x)} for x in list(years)},
            value=2002,
        ),
    ],
    className="mb-4",
)

filter_layout = dbc.Card(
    [
        html.Br(),
        target_filter,
        html.Br(),
        html.Hr(),
        html.Br(),
        year_filter,
        html.Br(),
    ],
    body=True,
    color="light",
    className="card border-0",
)

## Plot layout
world_map = html.Iframe(
    id="world-map",
    className="embed-responsive embed-responsive-item",
    sandbox="allow-scripts",
    style={
        "width": "100%",
        "height": "500px",
        "padding-right": "10px",
        "border-width": "0px",
    },
)


world_ranking = html.Div(
    [
        html.H2("World Ranking"),
        html.Br(),
        html.Iframe(
            id="world-ranking",
            sandbox="allow-scripts",
            className="embed-responsive embed-responsive-item",
            style={
                "width": "100%",
                "height": "500px",
                "padding-left": "10px",
                "border-width": "0px",
            },
        ),
    ]
)

world_trend = html.Div(
    [
        ### Plot 4 goes here
        html.H2("World Trend"),
        html.Br(),
        html.Iframe(
            id="world-trend",
            sandbox="allow-scripts",
            className="embed-responsive embed-responsive-item",
            style={
                "width": "100%",
                "height": "500px",
                "padding-right": "10px",
                "border-width": "0px",
            },
        ),
    ]
)


life_exp_vs_gdp = html.Div(
    [
        ### Plot 4 goes here
        html.H2("Life Expectancy vs GDP per Capita"),
        html.Br(),
        html.Iframe(
            id="life-exp-vs-gdp",
            sandbox="allow-scripts",
            className="embed-responsive embed-responsive-item",
            style={
                "width": "100%",
                "height": "500px",
                "padding-right": "10px",
                "border-width": "0px",
            },
        ),
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                header,
                dbc.Col(
                    [
                        filter_layout,
                        ThemeChangerAIO(
                            aio_id="theme", radio_props={"value": dbc.themes.SKETCHY}
                        ),
                    ],
                    className="col-sm-4",
                ),
                dbc.Col(world_map),
            ],
            justify="center",
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(life_exp_vs_gdp, className="col-sm-6"),
                dbc.Col(world_trend, className="col-sm-6"),
            ],
            justify="center",
            className="mb-4",
        ),
        dbc.Row(world_ranking, className="mb-4", align="end"),
    ],
    className="g-0",
    fluid=True,
    style={
        "height": "100vh",
        "align": "center",
        "padding-left": "10px",
        "padding-right": "10px",
    },
)

# Set up callback for World Trend
@app.callback(
    Output("world-trend", "srcDoc"),
    Input("year-slider", "value"),
    Input("target-filter", "value"),
)
def plot_world_trend(year, y_axis):
    """
    Create a line plot showing world trend based on year and a category
    ("pop" or"lifeExp" or "gdpPerCap) in gapminder dataset
    
    Parameters
    ----------
    year   : int
             A year of interest
    
    y_axis : string
             A category in gapminder dataset

    Returns
    ----------
    chart_final : altair.Chart object
                  An altair object showing a line plot
    
    
    Examples
    ----------
    >>> plot_world_trend(2002, "pop")
    """
    
    if y_axis == "pop":
        df = gapminder.groupby(["year", "continent"]).sum().reset_index()
    else:
        df = gapminder.groupby(["year", "continent"]).mean().reset_index()

    selection = alt.selection_multi(fields=["continent"], bind="legend")
    line = (
        alt.Chart(df)
        .mark_line()
        .encode(
            alt.X(
                "year:N",
                title="Year",
            ),
            alt.Y(
                y_axis,
                type="quantitative",
                title="Population"
                if y_axis == "pop"
                else (
                    "Life Expectancy (years)"
                    if y_axis == "lifeExp"
                    else "GDP per Capita (USD)"
                ),
                axis=alt.Axis(format="$,d")
                if y_axis == "gdpPercap"
                else (alt.Axis(format=",d")),
            ),
            color="continent",
            opacity=alt.condition(selection, alt.value(0.6), alt.value(0.1)),
        )
    )
    vline = (
        alt.Chart(pd.DataFrame({"year": [year]}))
        .mark_rule(strokeDash=[10, 10])
        .encode(x="year:N")
    )
    chart = line + vline
    chart_final = (
        chart.configure_axis(labelFontSize=14, titleFontSize=20)
        .configure_legend(titleFontSize=14)
        .properties(width=600, height=400)
    )

    chart_final = chart_final.add_selection(selection).interactive()

    return chart_final.to_html()


# Set up callback for World Ranking
@app.callback(
    Output("world-ranking", "srcDoc"),
    Input("year-slider", "value"),
    Input("target-filter", "value"),
)
def plot_world_ranking(year, y_axis):
    """
    Create a bar chart showing world ranking based on a category
    ("pop" or"lifeExp" or "gdpPerCap) in the year of interest
    
    Parameters
    ----------
    year   : int
             A year of interest
    
    y_axis : string
             A category in gapminder dataset

    Returns
    ----------
    chart_final : altair.Chart object
                  An altair object showing a bar chart
    
    
    Examples
    ----------
    >>> plot_world_ranking(2002, "pop")
    """

    year = year
    df = gapminder.query("year == @year").sort_values(by=y_axis, ascending=False)
    df["ranking"] = [f"#{i+1}" for i in range(142)]
    selection = alt.selection_multi(fields=["continent"], bind="legend")
    bar = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X(
                y_axis,
                title="Population"
                if y_axis == "pop"
                else (
                    "Life Expectancy (years)"
                    if y_axis == "lifeExp"
                    else "GDP per Capita (USD)"
                ),
                axis=alt.Axis(format="$,d", orient="top")
                if y_axis == "gdpPercap"
                else (alt.Axis(format=",d", orient="top")),
            ),
            alt.Y(
                "country",
                sort=alt.EncodingSortField("value", op="min", order="descending"),
                title=""),
            color=alt.Color("continent", legend=None),
            opacity=alt.condition(selection, alt.value(0.6), alt.value(0.1)),
            tooltip=y_axis,
        )
    )

    text = bar.mark_text(align="left", baseline="middle", dx=3).encode(text="ranking")

    chart = bar + text
    chart_final = chart.configure_axis(labelFontSize=14, titleFontSize=20)

    chart_final = chart_final.add_selection(selection).interactive()

    return chart_final.to_html()


def get_para(year, col):
    """
    Get world map parameters
    
    Parameters
    ----------
    year   : int
             A year of interest
    
    col    : string in ['pop', 'lifeExp, 'gdpPercap']
             A category in gapminder dataset
    Returns
    ----------
    set : (Full name, scale factor)
    
    
    Examples
    ----------
    >>> get_para(2002, "pop")
    """

    col_name_dict = {
        "lifeExp": "Life Expectancy",
        "pop": "Population",
        "gdpPercap": "GDP per Capita",
    }

    col_max_scale_dict = {"lifeExp": 300, "pop": 2000, "gdpPercap": 500}

    scale = (
        gapminder.groupby("year").sum()[col][year]
        / gapminder.groupby("year").sum()[col].max()
    )

    return (col_name_dict[col], int(scale * col_max_scale_dict[col]))


@app.callback(
    Output("world-map", "srcDoc"),
    Input("year-slider", "value"),
    Input("target-filter", "value"),
)
def plot_world(year, col):  # col = ['lifeExp', 'pop', 'gdpPercap']
    """
    Plot world map
    
    Parameters
    ----------
    year   : int
             A year of interest
    
    col    : string in ['pop', 'lifeExp, 'gdpPercap']
             A category in gapminder dataset
    Returns
    ----------
    map chart   : altair.Chart object
                  An altair object showing a world map
    
    
    Examples
    ----------
    >>> plot_world(2002, "pop")
    """
    
    # plot the globe as the background
    world_map = alt.topo_feature(data.world_110m.url, "countries")
    background = (
        alt.Chart(world_map)
        .mark_geoshape(fill="lightgray", stroke="white", color='continent:N')
        .properties(width=1000, height=400)
        .project(type="equalEarth")
    )
    
    # join lat and lon to gapminder respect to countries
    df_pos = pd.read_csv("data/world_country.csv")
    df_pos = df_pos.iloc[:, 1:4]
    df_pos.rename(columns={"latitude": "lat", "longitude": "lon"}, inplace=True)

    gapminder_pos = gapminder.merge(df_pos)
    para, max_scale = get_para(year, col)

    # plot mark_circle
    selection = alt.selection_multi(fields=["continent"], bind="legend")
    points = (
        alt.Chart(gapminder_pos[gapminder_pos["year"] == year])
        .mark_circle()
        .encode(
            longitude="lon:Q",
            latitude="lat:Q",
            size=alt.Size(col, legend=None, scale=alt.Scale(range=[0, max_scale])),
            color=alt.Color("continent", legend=alt.Legend(title="Continent")),
            tooltip=["country", col],
            opacity=alt.condition(selection, alt.value(0.6), alt.value(0.1)),
        )
        .add_selection(selection)
    )

    text_year = (
        alt.Chart({"values": [{}]})
        .mark_text(align="left", baseline="top")
        .encode(
            x=alt.value(850),
            y=alt.value(10),
            size=alt.value(50),
            color=alt.value("lightgray"),
            text=alt.value(str(year)),
        )
    )

    text = "World Overview of " + para
    text_para = (
        alt.Chart({"values": [{}]})
        .mark_text(align="left", baseline="top")
        .encode(
            x=alt.value(20),
            y=alt.value(10),
            size=alt.value(20),
            color=alt.value("gray"),
            text=alt.value(text),
        )
    )

    return (background + points + text_year + text_para).to_html()


@app.callback(Output("life-exp-vs-gdp", "srcDoc"), Input("year-slider", "value"))
def bubble_chart(year):
    """
    Create bubble chart from gapminder data
    
    Parameters
    ----------
    year   : int
             A year of interest
    
    Returns
    ----------
    map chart   : altair.Chart object
                  An altair object showing a bubble on world map
    
    Examples
    ----------
    >>> bubble_chart(2002)
    """
    
    df = gapminder[gapminder.year == year].drop("year", axis=1)

    df = (
        df.assign(gdpPercap=round(df.gdpPercap, 0))
        .assign(pop=round(df["pop"] / 1000000, 2))
        .assign(lifeExp=round(df.lifeExp, 1))
        .sort_values("pop", ascending=False)
    )

    selection = alt.selection_multi(fields=["continent"], bind="legend")
    plot = (
        alt.Chart(df)
        .mark_point(
            filled=True,
        )
        .encode(
            alt.X(
                "gdpPercap:Q",
                title="GDP per Capita [USD]",
                scale=alt.Scale(zero=False),
                axis=alt.Axis(format="$,d")),
            alt.Y(
                "lifeExp:Q",
                title="Life Expectancy [Years]",
                scale=alt.Scale(zero=False),
            ),
            alt.Size("pop:Q", scale=alt.Scale(range=[100, 2000]), legend=None),
            alt.Order("pop:Q", sort="descending"),
            alt.Color("continent:N"),
            opacity=alt.condition(selection, alt.value(0.6), alt.value(0.1)),
            tooltip=[
                alt.Tooltip("country:N", title="Country"),
                alt.Tooltip("pop:Q", title="Population (M)"),
                alt.Tooltip("gdpPercap:Q", title="GDP per Capita (USD)"),
            ],
        )
        .properties(width=600, height=400)
        .add_selection(selection)
        .interactive()
    )
    return plot.to_html()


if __name__ == "__main__":
    app.run_server(debug=True, port=9091)
