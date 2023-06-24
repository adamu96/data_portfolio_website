import plotly
import plotly.express as px
import json
import pandas as pd


graph_color = '#FFFFFF'


def line_graph(df):
     
    # Create Bar chart
    # fig = px.line(df, x='t', y='c', title='Stock Closing Price')
    
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG", title='Stock Price Historic', template='simple_white')

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
     
    return graphJSON