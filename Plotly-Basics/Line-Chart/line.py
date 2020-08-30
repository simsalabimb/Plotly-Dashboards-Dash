import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

#Showcasing 3 different ways to plot
#adding numbers to 5 so they are on different y-axis to easily see different styles

trace0 = go.Scatter(x=x_values, y=y_values+5, 
                    mode='markers', name='markers')

trace1 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='mylines')

trace2 = go.Scatter(x=x_values, y=y_values-5,
                    mode='lines+markers', name='mylines+markers')                   

#add list of plots to add multiple plots on same figure
data = [trace0, trace1,trace2]

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data)

pyo.plot(fig, filename='linechart.html')