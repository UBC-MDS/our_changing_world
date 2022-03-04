import numpy as np
import pandas as pd
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

import altair as alt
import plotly_express as px
from vega_datasets import data

# stylesheet with the .dbc class
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL, dbc_css])

# create filters
# gapminder datset
gapminder = px.data.gapminder()
years = gapminder.year.unique()

###### Header ########
header = html.H4(
    "Our Changing World",
    className="h1 bg-secondary bg-gradient-secondary text-white p-2 mb-2 text-center",
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
            inline=False,
            labelCheckedClassName="text-success",
            inputCheckedClassName="border border-success bg-success",
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
)

## Plot layout

world_map = html.Iframe(
    id="world-map",
    className="dbc",
    style={"width": "200%", "height": "500px", "padding-right": "10px"},
)


world_ranking = dbc.Card(
    [
        html.Div(
            [
                html.H2("World Ranking"),
                html.Br(),
                html.Iframe(
                    id="world-ranking",
                    style={"width": "200%", "height": "500px", "padding-left": "10px"},
                ),
            ]
        )
    ]
)


world_trend = dbc.Card(
    [
        html.Div(
            [
                ### Plot 4 goes here
                html.H2("World Trend"),
                html.Br(),
                html.Iframe(
                    id="world-trend",
                    style={"width": "200%", "height": "500px", "padding-right": "10px"},
                ),
            ]
        )
    ]
)

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                header,
                dbc.Col([filter_layout, ThemeChangerAIO(aio_id="theme")], width=4),
                dbc.Col(world_map),
            ],
            justify="evenly",
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(world_ranking, width=6),
                dbc.Col(world_trend),
            ],
            justify="evenly",
            className="mb-4",
            align="start",
        ),
    ],
    className="pad-row",
    fluid=True,
)

# Set up callback for World Trend
@app.callback(
    Output("world-trend", "srcDoc"),
    Input("year-slider", "value"),
    Input("target-filter", "value"),
)
def plot_world_trend(year, y_axis):
    if y_axis == "pop":
        df = gapminder.groupby(["year", "continent"]).sum().reset_index()
    else:
        df = gapminder.groupby(["year", "continent"]).mean().reset_index()
    line = (
        alt.Chart(df)
        .mark_line()
        .encode(
            alt.X("year", scale=alt.Scale(domain=(1950, 2007)), title="Year", axis=alt.Axis(format='')),
            alt.Y(
                y_axis,
                type="quantitative",
                title="Population"
                if y_axis == "pop"
                else ("Life Expectancy (years)" if y_axis == "lifeExp" else "GDP per Capita (USD)"),
                axis=alt.Axis(format='$.0f')
                if y_axis == "gdpPercap"
                else (alt.Axis(format='.0f')),
            ),
            color="continent",
        )
    )
    vline = (
        alt.Chart(pd.DataFrame({"year": [year]}))
        .mark_rule(strokeDash=[10, 10])
        .encode(x="year")
    )
    chart = line + vline
    chart_final = chart.configure_axis(
        labelFontSize=14, titleFontSize=20
    ).configure_legend(titleFontSize=14)

    return chart_final.to_html()


# Set up callback for World Ranking
@app.callback(
    Output("world-ranking", "srcDoc"),
    Input("year-slider", "value"),
    Input("target-filter", "value"),
)
def plot_world_ranking(year, y_axis):
    year = year
    df = gapminder.query("year == @year").sort_values(by=y_axis, ascending=False)
    df["ranking"] = [f"#{i+1}" for i in range(142)]
    bar = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            alt.X(
                y_axis,
                title="pop"
                if y_axis == "pop"
                else ("Life Expectancy" if y_axis == "lifeExp" else "GDP per Capita"),
            ),
            alt.Y(
                "country",
                sort=alt.EncodingSortField("value", op="min", order="descending"),
                title="Country",
            ),
            color=alt.Color("continent", legend=None),
            tooltip=y_axis,
        )
    )

    text = bar.mark_text(align="left", baseline="middle", dx=3).encode(text="ranking")

    chart = bar + text
    chart_final = chart.configure_axis(labelFontSize=14, titleFontSize=20)

    return chart_final.to_html()


def get_para(year, col):
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
    world_map = alt.topo_feature(data.world_110m.url, "countries")
    background = (
        alt.Chart(world_map)
        .mark_geoshape(fill="lightgray", stroke="white")
        .properties(width=1000, height=400)
        .project(type="equalEarth")
    )

    df_pos = pd.read_csv("data/world_country.csv")
    df_pos = df_pos.iloc[:, 1:4]
    df_pos.rename(columns={"latitude": "lat", "longitude": "lon"}, inplace=True)

    gapminder_pos = gapminder.merge(df_pos)
    para, max_scale = get_para(year, col)

    points = (
        alt.Chart(gapminder_pos[gapminder_pos["year"] == year])
        .mark_circle()
        .encode(
            longitude="lon:Q",
            latitude="lat:Q",
            size=alt.Size(col, legend=None, scale=alt.Scale(range=[0, max_scale])),
            color=alt.Color("continent", legend=None),
        )
    )

    text_year = (
        alt.Chart({"values": [{}]})
        .mark_text(align="left", baseline="top")
        .encode(
            x=alt.value(870),
            y=alt.value(10),
            size=alt.value(50),
            color=alt.value("lightgray"),
            text=alt.value(str(year)),
        )
    )

    text_para = (
        alt.Chart({"values": [{}]})
        .mark_text(align="left", baseline="top")
        .encode(
            x=alt.value(70),
            y=alt.value(10),
            size=alt.value(15),
            color=alt.value("gray"),
            text=alt.value(para),
        )
    )

    return (background + points + text_year + text_para).to_html()


if __name__ == "__main__":
    app.run_server(debug=True, port=9091)
