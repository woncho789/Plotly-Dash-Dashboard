"""10. Creating a Grid Layout.py

# A user can add multiple elements in the same row or col using dbc

# A user can adjust the size of elements, align or stack them
"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('./project/dash dashboard/fifa_soccer_players.csv')

app = Dash(external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard',
            style={'textAlign':'center',
            'fontFamily':'fantasy',
            'fontSize':'50px',
            'color':'blue'}),
    dbc.Row([
        dbc.Col(
            html.P([
                'Source: ',
                html.A('Sofifa',
                    href='https://sofifa.com',
                    target='_blank')]),
            width=5
        ),
        dbc.Col([
            html.Label('Player name: '),
            dcc.Dropdown(
                options=soccer['long_name'].unique(),
                value=soccer['long_name'].unique()[0],
                style={'backgroundColor':'lightblue'})
        ])
    ])
])


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3000, debug=True)
