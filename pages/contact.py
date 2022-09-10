import dash
from dash import  dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Hao Chen', className='mt-3'),
  #  dcc.Markdown('### FC Barcelona Forward', className='mb-5'),
    dcc.Markdown('### Personal info', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Nanjing, China 210000'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('+0086-1732-700-6835'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('redhawc1@gmail.com'),

        ], width={'size':6, 'offset':2})
], justify='center')