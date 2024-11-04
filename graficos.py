from helper import get_cotacao, get_dados_bc
import plotly.graph_objects as go

def cria_dados_candle(ticker, periodo):
    cotacoes_candle = get_cotacao(ticker, periodo)

    layout = go.Layout(yaxis=dict(tickfont=dict(color='#d3d6df'), showline=False),
                    xaxis=dict(tickfont=dict(color='#d3d6df'), showline=False))

    fig_candle = go.Figure(data=[go.Candlestick(x=cotacoes_candle.index,
                                                open=cotacoes_candle['Open'],
                                                high=cotacoes_candle['High'],
                                                low=cotacoes_candle['Low'],
                                                close=cotacoes_candle['Close']
    )], layout=layout)
    
    return fig_candle

def criando_grafico_infla(indicador, periodo):

    dados_inflacao = get_dados_bc(indicador,periodo)

    layout = go.Layout(yaxis=dict(tickformat=".1%", tickfont=dict(color="black")),
                            xaxis=dict(tickfont=dict(color="black")))

    fig_inflacao = go.Figure(layout = layout)

    fig_inflacao.add_trace(go.Bar(x=dados_inflacao.index, y=dados_inflacao.values,
                          marker_color = 'blue', name = 'IPCA'
                         ))        

    return fig_inflacao