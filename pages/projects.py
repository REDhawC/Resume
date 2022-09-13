import dash
from dash import html, dcc, Input, Output, State, callback
import dash_gif_component as gif
import dash_bootstrap_components as dbc
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__, title='Financial Information Visualization Dashboard', order=1)

df = pd.read_csv('assets/Berlin_crimes.csv')



def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Financial Information Visualization Dashboard', style={'textAlign':'center'}),

                    html.Hr(),

                    gif.GifPlayer(
                        gif='assets/gif1.gif',
                        still='assets/pause.png',
                        autoplay=True,
                    ),
                    dcc.Markdown('[click here to visit the website of this dashboard](https://redhawc-fd.onrender.com)',
                                 style={'textAlign': 'center', 'fontSize': 18}),
                    dcc.Markdown('(Sorry for the slow loading! Please refresh for a few times!)',
                                 style={'textAlign': 'center', 'fontSize': 18}),

                    dcc.Markdown(
                        '[click here to see the code on github](https://github.com/REDhawC/financial-dashboard)',
                        style={'textAlign': 'center', 'fontSize': 18}),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])


