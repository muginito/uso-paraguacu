import streamlit as st
import pandas as pd

def filtrar(df, label, coluna):
    filtro = st.multiselect(label, df[coluna].unique())
    if filtro:
        return df[df[coluna].isin(filtro)]
    return df

st.title("Uso Paraguaçu")

url = "https://raw.githubusercontent.com/muginito/uso-paraguacu/refs/heads/main/dados/USO_PARAGUACU.CSV"

df = pd.read_csv(url)

filtro_cidades = filtrar(df, "Cidades", "MUNICIPIO")

st.dataframe(filtro_cidades,
             width=1000,
             height=700,
             column_config={
                "Ano": st.column_config.NumberColumn(format="%d"),
                "Codigo": st.column_config.NumberColumn(format="%d")
             },
             hide_index=True
             )
