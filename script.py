import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Cours du Doge Coin", className='title'),
    html.P("Ce graphique donne l'évolution du cours du Doge Coin", className='description'),
    dcc.Graph(id='live-graph', className='graph'),
    dcc.Interval(
        id='interval-component',
        interval=2*60*1000, # 2 minutes
        n_intervals=0
    ),
    dcc.Store(id='data-store')
], className="container")

@app.callback(
    Output('data-store', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_data(n):
    # Lecture du CSV
    data = pd.read_csv("history.csv")
    return data.to_dict()

@app.callback(
    Output('live-graph', 'figure'),
    Input('data-store', 'data')
)
def update_graph(data):
    # Plotly Express
    df = pd.DataFrame(data)
    fig = px.line(df, x='date', y='doge', title='Cours du Doge Coin')
    return fig

# Lancement
if __name__ == '__main__':
    app.run_server(debug=True, port=4070, host="0.0.0.0")
