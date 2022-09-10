import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

def layout():
    return html.Div([
    html.H3("People that I've had the pleasure to work with", style={'textAlign':'center'}, className='my-3'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Xiaojian Tang'),
            dcc.Markdown('Director of the Department of Accounting, College of Finance, Nanjing Agricultural University')
        ], width=4),
        dbc.Col([
            dcc.Markdown('Hao is very professional. I really appreciate his quick thinking '
                         'and great teamwork. I know a coach is not supposed to say this, but '
                         'although O. Dembélé is a great player, Hao is my Forward Favorito.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Liang He'),
            dcc.Markdown('Associate Professor of the Department of Investment, College of Finance, Nanjing Agricultural University')
        ], width=4),
        dbc.Col([
            dcc.Markdown('Hao is so good with the ball. Every time he has the ball, I can see the stadium rise to its feet.'
                         ' And he always shares goal opportunities with his teammates. The opposite of selfish. I know it is not '
                         'appropriate for a player to say this, but I wish Hao was our coach instead of Xavier.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Xiaodan Zhang'),
            dcc.Markdown('Finance Manager of Bigo Technology Pte. Ltd.')
        ], width=4),
        dbc.Col([
            dcc.Markdown('xxxxxxxxxxxx',
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])
