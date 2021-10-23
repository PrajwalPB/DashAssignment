import pandas as pd
from pandas._config.config import options
import plotly
import plotly 
import plotly.express as px
import dash
import dash_core_components as dcc
from dash import dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input , Output

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["Mumbai", "Mumbai", "Mumbai", "Nagpur", "Nagpur", "Nagpur"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Assignment'),

    html.Div(children='''
        Dash:Assignment with dummy graph
    '''),
   dcc.Checklist(
       options=[
             {'label': 'Mumbai', 'value': 'MU'},
        {'label': 'Banglore', 'value': 'BL'},
        {'label': 'Nagpur', 'value': 'Na'}
    ],
    value=['MU', 'BL']

       
   ),
   dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Mumbai', 'value': 'MU'},
            {'label': 'Banglore', 'value': 'BL'},
            {'label': 'Nagpur', 'value': 'Na'}
        ],
        value='MU'
    ),
    html.Div(id='dd-output-container'),


     dcc.Graph(
       id='example-graph',
       figure=fig
    )
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)




