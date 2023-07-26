import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
)]
layout = go.Layout(
    title='Random Data Scatter plot',  # Graph title
    xaxis=dict(title='Some random X_values'),  # X axis label
    yaxis=dict(title='Some random Y_values'),  # Y axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter2.html')

