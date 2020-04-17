import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import dash_table
import matplotlib.image as mpimg
import base64
import numpy as np
import pickle
from dash.dependencies import Input, Output, State


def generate_table(dataframe,page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[{
            "name": i,
            "id":i
        }for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action="native",
        page_current=0,
        page_size=page_size,
    )
image_1 = 'Number of Loan in USD issued by Year (BHMD)-350x350.png'
encoded_image_1 = base64.b64encode(open(image_1, 'rb').read())
image_2 = "Number of Loan issued by Year-350x350.png"
encoded_image_2 = base64.b64encode(open(image_2, 'rb').read())
image_3 = "Loan based on Customer's Purposes (BHMD)-450x300.png"
encoded_image_3 = base64.b64encode(open(image_3, 'rb').read())
image_4 = "Distribution of Interest Rate by Sub Grade (BHMD).png"
encoded_image_4 = base64.b64encode(open(image_4, 'rb').read())
image_5 = "Funded Amount in USD by U.S State.png"
encoded_image_5 = base64.b64encode(open(image_5, 'rb').read())
image_6 = "c_emp_length-400x400.png"
encoded_image_6 = base64.b64encode(open(image_6, 'rb').read())
image_7 = "c_home-400x400.png"
encoded_image_7 = base64.b64encode(open(image_7, 'rb').read())
image_8 = "c_purpose-400x400.png"
encoded_image_8 = base64.b64encode(open(image_8, 'rb').read())
image_9 = "c_state-400x400.png"
encoded_image_9 = base64.b64encode(open(image_9, 'rb').read())
image_10 = "c_sub_grade-400x400.png"
encoded_image_10 = base64.b64encode(open(image_10, 'rb').read())
image_11 = "c_term-400x400.png"
encoded_image_11 = base64.b64encode(open(image_11, 'rb').read())
image_12 = "small-400x100.png"
encoded_image_12 = base64.b64encode(open(image_12, 'rb').read())


# df_EDA = pd.read_csv('cleandata_loan_test4.csv')
# df = pd.read_csv('cleanVIF_loan_test4.csv')
external_stylesheets=['https://codepen.io/chriddyp/pen/bWlwgP.css']

app=dash.Dash(__name__, external_stylesheets=external_stylesheets) 

app.layout =html.Div(children=[
    html.Img(src='data:image/png;base64,{}'.format(encoded_image_12.decode())),

    html.P('Created By : Sapto Aji Pamungkas'),
    html.P('Class      : Job Connector Data Science and Machine Learning Batch 7'),
    html.Br(),
    html.H1(children='''
        About Lending Club :
    '''),
    html.P(children='''
        Lending Club is the world's largest peer-to-peer lending platform which the product is enable borrowers to create unsecured personal loan between $1,000 and $40,000. Since 2007, Lending Club been bringing borrowers and investors together, transforming the way people access credit. Over the last 10 years, Lending Club helped millions of people take control of their debt, grow their small businesses, and invest for the future
    '''),
    html.Br(),

    dcc.Tabs(children=[
        dcc.Tab(value='tab-1', label='Highlight', children=[
            html.Div(children=[
                html.Div(children=[
                    html.Div(children=[
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_1.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_2.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_3.decode())),
                    ],className='row')
                ])
            ]),
            html.Br(),
            html.Br(),
            html.Div(children=[
                html.Div(children=[
                    html.Div(children=[
                           html.Img(src='data:image/png;base64,{}'.format(encoded_image_5.decode()))
                    ],className='row')
                ])
            ])
            
        ]),

        dcc.Tab(value='tab-2', label='Loan Statistic', children=[
            html.Div(children=[
                html.Div(children=[
                    html.P('Loan Statistic based on Categorical Data-1'),
                    html.Div([
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_6.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_7.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_8.decode()))
                    ],className='row'),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.P('Loan Statistic based on Categorical Data-2'),
                    html.Div([
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_9.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_10.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_11.decode()))
                    ],className='row'),
                ])
            ])
        ]),

        dcc.Tab(value='tab-3', label='Calculate Customer Credit Risk', children=[
            html.Div([
                html.P('How much recovery fee are paid off by customer during vintage?'),
                dcc.Input(id='s_recovery_fee',
                type='number',
                value='recovery_fee')],className='col-3'),
            html.Div([
                html.P("How much did customer pay on their last billing statement?"),
                dcc.Input(id='s_last_payment',
                type='number',
                value='last_payment')],className='col-3'),
            html.Div([
                html.P("Did the customer pay this month's billing statement?"),
                dcc.Dropdown(value='this_month',
                id='this_month',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Div([
                html.P("Did the customer pay last month's billing statement?"),
                dcc.Dropdown(value='last_month',
                id='last_month',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Div([
                html.P("Did the customer pay two months prior to the current month's billing statement?"),
                dcc.Dropdown(value='last_2_month',
                id='last_2_month',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Div([
                html.P("Did the customer pay three months prior to the current month's billing statement?"),
                dcc.Dropdown(value='last_3_month',
                id='last_3_month',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Div([
                html.P('Was last month the statements due? '),
                dcc.Dropdown(value='last_month_due',
                id='last_month_due',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Div([
                html.P('Was two months prior to the current month statements due?'),
                dcc.Dropdown(value='last_2_month_due',
                id='last_2_month_due',
                options=[{'label':'No','value':'0'},
                         {'label':'Yes','value':'1'}])],className='col-3'),
            html.Br(),
            html.Button('Search', id='filter'),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(id='predicted-values'),
            html.Br(),
        ])
    ],className='row',
            ### Tabs Content Style
        content_style={
            'fontFamily': 'Times-New-Roman',
            'borderBottom':'1px solid #d6d6d6',
            'borderLeft':'1px solid #d6d6d6',
            'borderRight':'1px solid #d6d6d6',
            'padding':'10px'} 
    )
])


@app.callback(
    Output('predicted-values', 'children'),
	[Input(component_id='filter',component_property='n_clicks')],
    [State('s_recovery_fee', 'value'),
     State('s_last_payment', 'value'),
     State('this_month', 'value'),
     State('last_month', 'value'),
     State('last_2_month', 'value'),
     State('last_3_month', 'value'),
     State('last_month_due', 'value'),
     State('last_2_month_due', 'value')])

def set_display_children(n_clicks, recovery_size, last_payment, this_month, last_month, last_2_month, last_3_month, last_month_due, last_2_month_due):
    file = []
    file.append(float(recovery_size))
    file.append(float(last_payment))
    file.append(this_month)
    file.append(last_month)
    file.append(last_2_month)
    file.append(last_3_month)
    file.append(last_month_due)
    file.append(last_2_month_due)
    file1 = np.array(file)
    loadModel = pickle.load(open('loan_rfc_model_DFI.sav', 'rb'))
    result = loadModel.predict(file1.reshape(1,8))
    if result == 1:
        return '\n Customer is a bad borrower/ loan'
    else:
        return '\n Customer is be a good borrower/ loan'

if __name__ =='__main__':
    app.run_server(debug=True)
        
