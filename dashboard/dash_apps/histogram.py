import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
import dash_table

# Load the data
url = 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv'
df = pd.read_csv(url)

# Map the 'Outcome' column to 'Dead' and 'Alive'
df['Survival Status'] = df['Outcome'].map({1: 'Dead', 0: 'Alive'})

# Initialize the Dash app
app = DjangoDash('histogram')

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='feature-dropdown',
        options=[{'label': i, 'value': i} for i in df.columns if i in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']],
        value='Glucose'
    ),
    dcc.Graph(id='histogram',className='cursor-pointer'),
    dash_table.DataTable(id='click-data', columns=[{"name": i, "id": i} for i in df.columns])
])

# Define the callback to update the graph
@app.callback(
    Output('histogram', 'figure'),
    [Input('feature-dropdown', 'value')]
)
def update_histogram(feature):
    fig = px.histogram(df, x=feature, color='Survival Status', nbins=50, 
                   color_discrete_map={'Dead': 'red', 'Alive': 'green'})
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    return fig

# Define the callback to update the click-data table
@app.callback(
    Output('click-data', 'data'),
    [Input('histogram', 'clickData'), Input('feature-dropdown', 'value')]
)
def display_click_data(clickData, feature):
    if clickData is None:
        return df.iloc[0:0].to_dict('records')  # return empty DataFrame in the correct format
    else:
        # Extract the value of the clicked bar
        clicked_value = clickData['points'][0]['x']
        # Filter the DataFrame to this value
        filtered_df = df[df[feature] == clicked_value]
        return filtered_df.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)