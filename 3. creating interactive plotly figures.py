
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('./project/dash dashboard/world_happiness.csv')

line_fig = px.line(happiness[happiness['country']== 'United States'],
                   x = 'year', y = 'happiness_score',
                   title = 'Happiness Score in the USA')

app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldshappiness.report',
                   target='_blank')]),
    dcc.RadioItems(options=happiness['region'].unique(),
                   value=['North America']),
    dcc.Checklist(options=happiness['region'].unique(),
                  value=['North America']),
    dcc.Dropdown(id='country_dropdown',
                 options=happiness['country'].unique(),
                 value=['United States']),
    dcc.Graph(id='happiness_graph', figure={})   
])

@app.callback(
    Output('happiness_graph','figure'),
    Input('country_dropdown','value')
)
def update_graph(selected_country):
    filtered_happiness = happiness[happiness['country']== selected_country]
    line_fig = px.line(filtered_happiness,
                       x='year', y='happiness_score',
                       title = f'Happiness Score in the {selected_country}')
    return line_fig

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
