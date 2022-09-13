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
            dcc.Markdown('I have known Hao for over two years. '
                         'He enrolled in my courses Research and Innovation Training, Auditing, and Non-Profit Organization Accounting.  '
                         'He was an intelligent and diligent student and finished all of the assignments with high quality.',
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
            dcc.Markdown('Hao Chen was a conscientious member of the class and had a positive and mature attitude towards his learning. '
                         'He sat in the front row and frequently interacted with me. '
                         'It is worth mentioning that he was always willing to take on more difficult topics for coursework and handled them well.',
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
            dcc.Markdown('Hao was always willing to learn new stuff and had an insight into discovering ways to automate and simplify working procedures. That was pretty impressive. ',
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])
