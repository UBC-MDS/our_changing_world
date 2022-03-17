import altair as alt
from gapminder import gapminder
import pandas as pd
from dash import Dash, html, dcc, Input, Output, State

    
gapminder1 = gapminder
gapminder1 = gapminder1[gapminder1.country != 'Kuwait']


def plot_altair(xmax):
    if xmax == 1952:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1957: 
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1962:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1967:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1972:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1977:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1982:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1987:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1992:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 1997:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    elif xmax == 2002:
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    else: 
        chart = alt.Chart(gapminder1[gapminder1['year'] == xmax]).mark_point().encode(
            alt.X('lifeExp', title = "Life Expectancy"),
            alt.Y('gdpPercap', title = "GDP per capita"),
            color='continent',
            fill='continent',
            tooltip=['country', 'continent', 'lifeExp', 'gdpPercap']).interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            srcDoc=plot_altair(xmax=1952),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=1952, max=2007, step=5, value=1952, marks={
        1952: '1952',
        1957: '1957',
        1962: '1962',
        1967: '1967',
        1972: '1972',
        1977: '1977',
        1982: '1982',
        1987: '1987',
        1992: '1992',
        1997: '1997',
        2002: '2002',
        2007: '2007'
    }
)])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xmax):
    return plot_altair(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)