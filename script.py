import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Img(src="assets/Dogecoin_Logo.png", width="100"),
    html.H1("Cours du Doge Coin", className='title'),
    html.P("Évolution du cours du Doge Coin au cours du temps", className='description'),
    html.Div(dcc.Graph(id='live-graph', className='graph'), className="box-container"),
    html.P("Rapport quotidien", className='description'),
    html.Div(html.Table(id="stats"), className="box-container"),
    html.Div([
        html.Hr(),
        html.Span("Thomas COUDREAU, IF2")
    ], className="footer"),
    dcc.Interval(
        id='interval-component',
        interval=2*60*1000, # 2 minutes
        n_intervals=0
    ),
    dcc.Store(id='data-store')
], className="container")

@app.callback(
    Output('data-store', 'data'),
    Output('stats', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_data(n):
    # Lecture du CSV
    data = pd.read_csv("history.csv")

    # Affichage du rapport quotidien
    with open("/home/thomas/projet/stats.json", "r") as infile:
        stats = json.load(infile)
    children = [html.Tr(children=[html.Td(x) , html.Td(stats[x])]) for x in stats.keys()]

    return data.to_dict(), children

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
