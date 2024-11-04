import yfinance as yf
from bcb import sgs
import datetime

def get_cotacoes(tickers):
  cotacoes = yf.download(tickers, start=(datetime.date.today() - datetime.timedelta(days=5)))

  cotacoes = cotacoes['Close']
  cotacoes = cotacoes.iloc[-1, :]
  cotacoes = cotacoes.reset_index()
  cotacoes.columns = ['Ticker', 'Preco']

  cotacoes['Preco'] = cotacoes['Preco'].astype(float).round(2)
  return cotacoes

def get_cotacao(ticker, periodo=5):
  dados = yf.download(ticker, start=(datetime.date.today() - datetime.timedelta(days=periodo)))

  return dados

def get_dados_bc(indicador, periodo):
  dados_inflacao = sgs.get({'ipca': 433,
                        'igp-m': 189})
  dados_inflacao = dados_inflacao.dropna()

  dados_inflacao = dados_inflacao/100
  dados_inflacao = dados_inflacao.iloc[-(int(periodo)):, :]

  if indicador == "IPCA":

      dados_inflacao = dados_inflacao['ipca']

  elif indicador == 'IGP-M':

      dados_inflacao = dados_inflacao['igp-m']

  return dados_inflacao