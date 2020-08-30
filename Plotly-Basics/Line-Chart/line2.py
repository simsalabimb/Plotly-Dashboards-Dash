import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../SourceData/nst-est2017-alldata.csv', index_col=0)

#5 rows x 120 columns

df2 = df[df['DIVISION'] == '1']

#set index to NAME column, use "inplace" to keep change
df2.set_index('NAME',inplace=True)

#Filter for Population data. Columns are POPESTIMATE 2016, POPESTIMATE2017, etc so looking for any text ="POP"
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]

df2 = df2[list_of_pop_col]

#for builds the multiple plots
data = [ go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines',
                    name=name) for name in df2.index]

pyo.plot(data, filename='linechart2.html')