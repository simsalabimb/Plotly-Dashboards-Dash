import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
import config


app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),

    html.Div([
         html.H3('Enter a stock symbol: ', style={'paddingRight':'30px'}),
         dcc.Input(id = 'my_stock_picker', value='SPY', style={'fontSize':24, 'width':75}),
    ], style = {'display':'inline-block', 'verticalAlign':'top'}),

    html.Div([
        html.H3('Select a start and end date: '),
        dcc.DatePickerRange(id='my_date_picker', 
                            min_date_allowed=datetime(2019,1,1),
                            max_date_allowed = datetime.today(),
                            start_date = datetime(2020,1,1),
                            end_date = datetime.today())
    ], style = {'display':'inline-block'}),

    html.Div([
        html.Button(id='submit-button',
                    n_clicks=0,
                    children='Submit',
                    style={'fontSize':24, 'marginLeft':'30px'}
                    )
    ], style={'display':'inline-block'}),
   
    dcc.Graph(
        id='my_graph',
        figure = {
            'data':[
                {'x':[1,2],'y':[3,1]}
            ],
            'layout':
                {'title': 'Default Title'}
        }
    )
])


@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button','n_clicks')],
    # dont update until submit is complete
    [State('my_stock_picker','value'),
     State('my_date_picker', 'start_date'),
     State('my_date_picker', 'end_date')
    ])

#variables need to passed in order of the callback function 
def update_graph(n_clicks,stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end = datetime.strptime(end_date[:10],'%Y-%m-%d')

    df = web.get_data_tiingo(stock_ticker, start, end, api_key= config.TIINGO_API_KEY)

    fig = {
        'data':[
            {'x':df.index.get_level_values(1),'y':df.close}
        ], 
        'layout':
            {'title':stock_ticker}
    }

    return fig


if __name__ == '__main__':
    app.run_server()

