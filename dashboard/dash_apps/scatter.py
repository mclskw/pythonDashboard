import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash

# Load the data
url = 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv'
df = pd.read_csv(url)

# Create a Dash application
app = DjangoDash('scatter')

# Define the layout
app.layout = html.Div([
    dcc.Dropdown(
        id='outcome-dropdown',
        options=[
            {'label': 'Dead', 'value': 1},
            {'label': 'Alive', 'value': 0}
        ],
        value=0
    ),
    dcc.Graph(id='scatter-plot')
])

# Define the callback
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('outcome-dropdown', 'value')]
)
def update_scatter_plot(outcome):
    filtered_df = df[df['Outcome'] == outcome]
    fig = px.scatter(filtered_df, x='BloodPressure', y='BMI', color='Age')
    return fig