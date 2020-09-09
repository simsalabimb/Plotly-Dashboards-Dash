import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label': 'New York City',
                            'value': 'NYC'},
                            {'label': 'San Francisico',
                            'value': 'SF'}],
                            #default value right now
                            value='SF'),

    html.Label('Slider'),
    dcc.Slider(min=-10,max=10,step=0.5,value=0,
                marks={i: i for i in range(-10,10)}),
    
    #Labels were overlapping so we could:
    #use html.P() which is paragraph to add breakline or
    #could add individual div's so there is no overlap and add margins to styles
    html.P(),

    html.Label('Some Radio Items'),
    dcc.RadioItems(options=[{'label': 'New York City',
                            'value': 'NYC'},
                            {'label': 'San Francisico',
                            'value': 'SF'}],
                            #default value right now
                            value='SF')
])

if __name__ == '__main__':
    app.run_server()