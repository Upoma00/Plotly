import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(56)

x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

trace0 = go.Scatter(
    x=x_values,
    y=y_values + 5,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=x_values,
    y=y_values - 5,
    mode='lines',
    name='lines'
)
data = [trace0, trace1, trace2]

layout = go.Layout(
    title='Line charts showing three different modes'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
