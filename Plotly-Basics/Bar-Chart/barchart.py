import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../Data/2018WinterOlympics.csv')

#print(df.head())

'''
#This works for basic bar chart
data = [ go.Bar(x=df["NOC"], y=df["Total"])]
layout = go.Layout(title='Medals')
fig = go.Figure(data,layout)
pyo.plot(fig, filename='barchart.html')
'''

trace1 = go.Bar(x=df["NOC"], y=df["Gold"], 
                name='Gold', marker=dict(color='#FFD700'))

trace2 = go.Bar(x=df["NOC"], y=df["Silver"], 
                name='Silver', marker=dict(color='#9ea0a1'))

trace3 = go.Bar(x=df["NOC"], y=df["Bronze"], 
                name='Bronze', marker=dict(color='#cd7f32'))

data = [trace1, trace2, trace3]

#barmode = stack to make stacked barc chart, put in layout parameter
layout = go.Layout(title='Medals')

fig = go.Figure(data,layout)

pyo.plot(fig, filename='barchart.html')

