from dash import Dash, html, dcc, callback, Output, Input, dash_table
from helper import get_cotacoes
from graficos import cria_dados_candle

tickers = ['WEGE3.SA', 'ABEV3.SA', 'PETR4.SA', 'VALE3.SA', 'MGLU3.SA', 'PCAR3.SA', 'ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']

cotacoes = get_cotacoes(tickers)

options_periodo = [{'label': f'{i} dias', 'value': i} for i in range(5, 31, 5)]

app = Dash(__name__)

app.layout = html.Main(
    children=[
        html.Div(
            children=[
                html.Div(
                    html.H1(children='Cotações de Ontem', className='titulos-dash'),
                    style={'display': 'flex', 'justify-content': 'center' }
                ),
                html.Div(
                    children=dash_table.DataTable(
                        cotacoes.to_dict('records'),
                        id='table-cotacoes', 
                        style_header={
                            'background-color': '#333E66',
                            'font-weight': 'bold',
                            'border': '0px',
                            'color': '#D3D6Df',
                            'border-radius': '8px'
                        },
                         style_cell={
                            'text-align': 'center',
                            'padding': '4px 4px',
                            'background-color': '#212946',
                            'color': '#D3D6Df'
                        },
                        style_data={
                            'border': '0px',
                            'font-size': '12px'
                        },
                        style_table={
                            'border-radius': '8px',
                            'overflow': 'hidden'
                        },
                        style_data_conditional=[
                            {
                                'if': {
                                    'filter_query': '{Preco} > 20',
                                    'column_id': 'Preco'
                                },
                                'color': '#33E633'
                            },
                            {
                                'if': {
                                    'filter_query': '{Preco} < 20',
                                    'column_id': 'Preco'
                                },
                                'color': '#FF4D4D'
                            }
                        ]
                    ),
                    style={'margin': '0 100px' }
                )
            ],
            style = {'grid-columns': '1', 'grid-row': '1', 'height': '50vh'}
        ),
        html.Div(
            children=[
                html.Div(
                    html.H1(children = "Gráfico de Candle", className='titulos-dash'
                    ),
                    style={'display': 'flex', 'justify-content': 'center'}
                ),
                html.Div(
                    [
                        dcc.Dropdown(tickers, 'WEGE3.SA', id='drop_candle'),
                        dcc.Dropdown(options_periodo, 5, id='drop_candle_periodo')
                    ]
                ),
                html.Div(

                    children= dcc.Graph(
                        id='grafico_candle',
                        style={'margin' : '0 100px', 'height': '400px'})
                )
            ],
            style = { 'grid-columns': '1', 'grid-row': '2', 'height': '50vh'}
        )
    ],className='container'
)

@app.callback(
    
    [Output('grafico_candle', 'figure')],
    [Input('drop_candle', 'value'),
     Input('drop_candle_periodo', 'value')]   
)

def update_graficos(candle_value,candle_periodo):
    return cria_dados_candle(candle_value, candle_periodo)

if __name__ == '__main__': 
    app.run(debug=True)