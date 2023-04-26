from dash import dcc, html
import dash_bootstrap_components as dbc

modelling_results_path = 'assets/modelling/modelling_results.html' # just put ur html in the same directory as your .py so the path is straight away the name of the file

modelling_results_graph = html.Div([
        html.Embed(src=modelling_results_path, width='1200', height='600'),
    ],
    style={'text-align':'center'}
    )

layout = dbc.Container([
    dbc.Row([
            dbc.Col(modelling_results_graph, width=12)
        ])
    ])


# remember to import relevant libraries, declare app = dash.DASH() in the beginning and also app.run_server in the end to make it runable in your pc
# and change everything necessary like using app.layout instead of just layout at line 12