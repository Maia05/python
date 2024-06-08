import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

# Carregando os dados
data = pd.read_csv('dados.csv')

# Configurando o título do sistema

st.sidebar.title('Ánalise de vendas da MOB')

# Criando as páginas do sistema
pages = {
    'Vendedor': 'vendedor',
    'Faixa Etária': 'faixa_etaria',
    'Cidade': 'cidade',
    'Produto': 'produto',
    'Velocidade': 'velocidade',
    'Valor': 'valor',
    'Promoções': 'promocoes',
    'Forma de Cobrança': 'forma_cobranca',
    'Forma de Captação': 'forma_captacao',
    'Turno do Agendamento': 'turno_agendamento'
}

page = st.sidebar.selectbox('Selecione a página', list(pages.keys()))

# Função para plotar gráficos
def plot_graph(data, column, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    st.pyplot()

# Página de Vendedor
if pages[page] == 'vendedor':
    st.title('Ánalise de quem vendeu mais')
    plot_graph(data, 'VENDEDOR', 'Contratos por Vendedor', 'Vendedor', 'Quantidade de Contratos')

# Página de Faixa Etária
elif pages[page] == 'faixa_etaria':
    # Calcular a idade a partir da data de nascimento
    data['IDADE'] = pd.to_datetime('now').year - pd.to_datetime(data['DATA DE NASCIMENTO']).dt.year
    st.title('Ánalise de faixa etária')
    plot_graph(data, 'IDADE', 'Faixa Etária dos Clientes', 'Idade', 'Quantidade de Clientes')

# Página de Cidade
elif pages[page] == 'cidade':
    st.title('Ánalise das cidades')
    plot_graph(data, 'CIDADE', 'Clientes por Cidade', 'Cidade', 'Quantidade de Clientes')

# Página de Produto
elif pages[page] == 'produto':
    st.title('Ánalise dos produtos mais vendidos')
    plot_graph(data, 'PRODUTO', 'Produtos Vendidos', 'Produto', 'Quantidade Vendida')

# Página de Velocidade
elif pages[page] == 'velocidade':
    st.title('Ánalise das velocidades de internet mais vendidas')
    plot_graph(data, 'VELOCIDADE', 'Velocidades de Internet Contratadas', 'Velocidade', 'Quantidade Contratada')

# Página de Valor
elif pages[page] == 'valor':
    st.title('Ánalise dos valores dos planos vendidos')
    plot_graph(data, 'VALOR', 'Valores dos Planos Vendidos', 'Valor', 'Quantidade Vendida')

# Página de Promoções
elif pages[page] == 'promocoes':
    st.title('Ánalise das promoções')
    plot_graph(data, 'PROMOÇÕES', 'Promoções Aplicadas', 'Promoção', 'Quantidade Aplicada')

# Página de Forma de Cobrança
elif pages[page] == 'forma_cobranca':
    st.title('Ánalise da forma de cobrança')
    plot_graph(data, 'FORMA DE COBRANÇA', 'Formas de Cobrança Utilizadas', 'Forma de Cobrança', 'Quantidade Utilizada')

# Página de Forma de Captação
elif pages[page] == 'forma_captacao':
    st.title('Ánalise da forma que foi captada cada cliente')
    plot_graph(data, 'FORMA DA CAPTAÇÃO', 'Formas de Captação dos Clientes', 'Forma de Captação', 'Quantidade de Clientes')

# Página de Turno do Agendamento
elif pages[page] == 'turno_agendamento':
    st.title('Ánalise dos agendamentos')
    plot_graph(data, 'TURNO DO AGENDAMENTO', 'Turnos Mais Escolhidos para Instalação', 'Turno', 'Quantidade Escolhida')
    
    
