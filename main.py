import plotly.express as px
import pandas as pd

# Оператори кольору карти:
visited_color = 'tan'
unvisited_color = 'white'
border_color = 'darkgray'
ocean_color = 'lightblue'
# Список країн, які я відвідав або мешкав:
countries_visited = ['Australia', 'Portugal', 'United States', 'Canada',
                     'Mexico', 'Bahamas', 'Scotland', 'England', 'France',
                     'Spain', 'Norway', 'Italy', 'Greece', 'Turkey',
                     'New Zealand',  'Kazakhstan', 'Hungary', 'Egypt', 'Nigeria',
                     'Qatar', 'Bahrain', 'United Arab Emirates', 'Malaysia',
                     'United Kingdom', 'Ukraine']

# Перетворення списку на датафрейм для Plotly Express:
df = pd.DataFrame({'Country': countries_visited})
df.head()
# Визначення зображення:
fig = px.choropleth(df,
                    width=1000, height=700,
                    locations='Country',
                    locationmode='country names',
                    color_discrete_sequence=[visited_color])

# Вибір проекції, елементів картки, кольору:
fig.update_geos(projection_type="natural earth",
                showcountries=True,
                countrycolor=border_color,
                showland=True, landcolor=unvisited_color,
                showocean=True, oceancolor=ocean_color,
                showlakes=False,
                showrivers=False,
                showframe=True)

# Відключення легенди та форматування заголовка Title:
fig.update_layout(showlegend=False,
                  title={'text': "Країни в яких я бував",
                         'y': 0.90,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top',
                         'font': {'size': 45,
                                  'family': 'Times New Roman'}})
# Сортування датафрейму для перерахування країн у легенді згідно із заданим порядком.
df = df.sort_values(by='Country', ascending=True)

# Встановлення кольору за допомогою стовпця "Country" та застосування дискретної колірної послідовності:
fig = px.choropleth(df,
                    width=1000, height=700,
                    locations='Country',
                    locationmode='country names',
                    color='Country',
                    color_discrete_sequence=px.colors.qualitative.Light24)

fig.update_geos(projection_type="natural earth",
                showcountries=True,
                countrycolor=border_color,
                showland=True, landcolor=unvisited_color,
                showocean=True, oceancolor=ocean_color,
                showlakes=False,
                showrivers=False,
                showframe=True)

# Включення легенди та зміна положення заголовка Title:
fig.update_layout(showlegend=True,
                  title={'text': "Країни в яких я бував",
                         'y': 0.85,
                         'x': 0.445,
                         'xanchor': 'center',
                         'yanchor': 'top',
                         'font': {'size': 40}})