from dash import Dash, html, dcc, callback, Output, Input, dash_table
from helper import get_cotacoes

tickers = ['WEGE3.SA', 'ABEV3.SA', 'PETR4.SA', 'VALE3.SA', 'MGLU3.SA', 'PCAR3.SA', 'ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']

cotacoes = get_cotacoes(tickers)

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
            ]
        )
    
    ],className='container'
)

if __name__ == '__main__': 
    app.run(debug=True)