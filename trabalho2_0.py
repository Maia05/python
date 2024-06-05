import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Carregar os dados da campanha de marketing (arquivo CSV)
dados_campanha = pd.read_csv('dados_campanha.csv')

# Configurar as páginas do Streamlit
st.sidebar.title('Campanha de marketing')
pagina = st.sidebar.selectbox("Selecione a página:", ["Visão Geral", "Conversões por Canal", "Custo por Canal", "Receita por Canal"])

# Página de Visão Geral
if pagina == "Visão Geral":
    st.title('Análise da Campanha de Marketing - Visão Geral')
    st.subheader('Dados da Campanha')

    # Exibir os dados da campanha em uma tabela interativa
    st.dataframe(dados_campanha)

    # Análise dos dados
    st.subheader('Análise dos Dados')

    # Calcular o total de clientes alcançados pela campanha
    total_clientes = dados_campanha.shape[0]
    st.write(f'Total de Clientes Alcançados: {total_clientes}')

    # Calcular a taxa de conversão
    total_conversoes = dados_campanha['conversao'].sum()
    taxa_conversao = (total_conversoes / total_clientes) * 100
    st.write(f'Taxa de Conversão: {taxa_conversao:.2f}%')

    # Calcular o custo por conversão
    custo_total = dados_campanha['custo'].sum()
    custo_por_conversao = custo_total / total_conversoes
    st.write(f'Custo por Conversão: R${custo_por_conversao:.2f}')

    # Calcular a receita gerada pela campanha
    receita_total = dados_campanha['receita'].sum()
    st.write(f'Receita Total: R${receita_total:.2f}')

    # Calcular o ROI (Return on Investment)
    roi = ((receita_total - custo_total) / custo_total) * 100
    st.write(f'ROI: {roi:.2f}%')

# Página de Conversões por Canal
elif pagina == "Conversões por Canal":
    st.title('Análise da Campanha de Marketing - Conversões por Canal')
    st.subheader('Gráfico de Conversões por Canal')

    # Calcular as conversões por canal
    conversoes_por_canal = dados_campanha.groupby('canal')['conversao'].sum()

    # Exibir o gráfico utilizando a biblioteca Matplotlib
    fig, ax = plt.subplots()
    ax.bar(conversoes_por_canal.index, conversoes_por_canal.values)
    ax.set_xlabel('canal')
    ax.set_ylabel('conversao')
    ax.set_title('Conversões por Canal')
    st.pyplot(fig)

# Página de Custo por Canal
elif pagina == "Custo por Canal":
    st.title('Análise da Campanha de Marketing - Custo por Canal')
    st.subheader('Gráfico de Custo por Canal')

    # Calcular o custo por canal
    custo_por_canal = dados_campanha.groupby('canal')['custo'].sum()

    # Exibir o gráfico utilizando a biblioteca Matplotlib
    fig, ax = plt.subplots()
    ax.bar(custo_por_canal.index, custo_por_canal.values)
    ax.set_xlabel('canal')
    ax.set_ylabel('custo')
    ax.set_title('Custo por Canal')
    st.pyplot(fig)

# Página de Receita por Canal
elif pagina == "Receita por Canal":
    st.title('Análise da Campanha de Marketing - Receita por Canal')
    st.subheader('Gráfico de Receita por Canal')

    # Calcular a receita por canal
    receita_por_canal = dados_campanha.groupby('canal')['receita'].sum()

    # Exibir o gráfico utilizando a biblioteca Matplotlib
    fig, ax = plt.subplots()
    ax.bar(receita_por_canal.index, receita_por_canal.values)
    ax.set_xlabel('canal')
    ax.set_ylabel('receita')
    ax.set_title('Receita por Canal')
    st.pyplot(fig)

