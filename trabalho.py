import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Analise de cancelamentos")
    uploadded_file = st.file_uploader("Coloque seu arquivo aqui")
    
if uploadded_file is not None:
    df = pd.read_csv(uploadded_file)
    
    with st.sidebar:
        distinct_ages = df["Age"].unique().tolist()
        ages_selected = st.selectbox("Idade específica", distinct_ages)
        
        city_selected = st.radio("Vendedor", ["A", "B", "C"], index=None)
        
        if ages_selected:
            df = df[df["Age"]== ages_selected]
            
        if city_selected:
            df = df[df["City_Category"]== city_selected]
                
    st.write("Análise de vendas")
    
    st.bar_chart(df, x="Product_Category_2", y="Purchase")
    st.dataframe(df, use_container_width=True)