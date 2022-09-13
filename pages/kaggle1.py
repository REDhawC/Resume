import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_gif_component as gif
from .side_bar import sidebar

dash.register_page(__name__)

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
                    html.H3('Kaggle competition: H&M Personalized Fashion Recommendations', style={'textAlign': 'center'}),

                    html.Hr(),

                    gif.GifPlayer(
                        gif='assets/gif3.gif',
                        still='assets/pause.png',
                        autoplay=True,
                    ),
                    dcc.Markdown('[click here to visit the competition website on Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations)',
                                 style={'textAlign': 'center', 'fontSize': 18}),
                    dcc.Markdown(
                        '[click here to check my Kaggle profile](https://www.kaggle.com/redhawc)',
                        style={'textAlign': 'center', 'fontSize': 18}),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])