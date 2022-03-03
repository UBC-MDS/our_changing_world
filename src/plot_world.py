import altair as alt
import pandas as pd
from vega_datasets import data
from gapminder import gapminder


def get_para(year, col):
    col_name_dict = {'lifeExp': 'Life Expectancy',
                     'pop': 'Population',
                     'gdpPercap': 'GDP per Capita'
                    }
    
    col_max_scale_dict = {'lifeExp': 300,
                          'pop': 2000,
                          'gdpPercap': 500
                         }
    
    scale = gapminder.groupby('year').sum()[col][year]/gapminder.groupby('year').sum()[col].max()
    
    return (col_name_dict[col], int(scale*col_max_scale_dict[col]))


def plot_world(year, col): # col = ['lifeExp', 'pop', 'gdpPercap']
    world_map = alt.topo_feature(data.world_110m.url, 'countries')
    background = alt.Chart(world_map).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        width=1000,
        height=400
    ).project(type='equalEarth')
    
    df_pos = pd.read_csv('../data/world_country.csv')
    df_pos = df_pos.iloc[:, 1:4]
    df_pos.rename (columns = {'latitude': 'lat', 'longitude': 'lon'}, inplace=True)
    
    gapminder_pos = gapminder.merge(df_pos)
    para, max_scale = get_para(year, col)
    
    points = alt.Chart(gapminder_pos[gapminder_pos['year'] == year]).mark_circle().encode(
        longitude='lon:Q',
        latitude='lat:Q',
        size = alt.Size(col, legend=None, scale=alt.Scale(range=[0, max_scale])),
        color = alt.Color('continent', legend=None)
    )
    
    text_year = alt.Chart({'values':[{}]}).mark_text(
        align='left', baseline='top'
    ).encode(
        x=alt.value(870),
        y=alt.value(10),
        size=alt.value(50),
        color=alt.value('lightgray'),
        text=alt.value(str(year))
    )

    text_para = alt.Chart({'values':[{}]}).mark_text(
        align='left', baseline='top'
    ).encode(
        x=alt.value(70),
        y=alt.value(10),
        size=alt.value(15),
        color=alt.value('gray'),
        text=alt.value(para)
    )

    return (background + points + text_year + text_para)


if __name__ == '__main__':
    plot_world(2007, 'pop').show()