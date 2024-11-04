from helper import get_cotacao
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

