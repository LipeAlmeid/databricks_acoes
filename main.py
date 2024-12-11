# Importar bibliotecas 

import streamlit as st
import pandas as pd
import yfinance as yf 

# Criar as funções do carregamento de dados
    # Cotação de algumas ações no periodo de 2010 a 2024 

@st.cache_data
def carregar_dados(empresa):
    texto_tickers = " ".join(empresa)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

acoes = ["ITUB4.SA", "PETRA4.SA", "MGLU3.SA", "VALE3.SA", "GGBR4.SA"]
dados = carregar_dados(acoes)


# Criar interface streamlit 
st.write("""
 -- App preço de açoes --
         O Gráfico abaixo representa a evolucao do preço das ações selecionadas no período de 2010 até 2024
"""   
)


# Prepara os filtros de visualizaçao 
lista_acoes = st.multiselect("Escolha as ações para visualizar o gráfico", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})
    else: 
        dados = dados[lista_acoes]

# Criar grafico
st.line_chart(dados)

st.write(
    """
Fim do App 
"""
)
