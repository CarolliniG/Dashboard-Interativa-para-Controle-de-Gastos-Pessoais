import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('gastos.csv', encoding='UTF-8', parse_dates=['data'])

# Verificar as colunas disponíveis (sempre uma boa prática)
print(df.columns)

# Criar a interface do usuário
st.title('Dashboard de Gastos Pessoais')

# Filtro por categoria
categoria = st.selectbox('Selecione a categoria', df['categoria'].unique())

# Filtrar os dados
df_filtrado = df[df['categoria'] == categoria]

# Criar um gráfico de barras
fig = px.bar(df_filtrado, x='data', y='valor', color='categoria', title='Gastos por categoria')
st.plotly_chart(fig)

# Adicionar um filtro de data
data_inicial = st.date_input("data inicial")
data_final = st.date_input("data final")

# Converter as datas de entrada para o formato datetime
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)

# Filtrar os dados com as datas convertidas
df_filtrado = df[(df['data'] >= data_inicial) & (df['data'] <= data_final)]

# Criar um gráfico de linha para mostrar a evolução dos gastos ao longo do tempo
fig_linha = px.line(df_filtrado, x='data', y='valor', title='Evolução dos Gastos')
st.plotly_chart(fig_linha)
