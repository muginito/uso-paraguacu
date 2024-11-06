import streamlit as st
import pandas as pd

st.title("Uso Paraguaçu")

df = pd.read_csv(r".\dados\USO_PARAGUACU.CSV")

filtro_cidades = st.multiselect("Cidades", df["MUNICIPIO"].unique())

if filtro_cidades:
    df_filtrado = df[df["MUNICIPIO"].isin(filtro_cidades)]
else:
    df_filtrado = df

st.dataframe(df_filtrado,
             width=1000,
             height=700,
             column_config={
                "Ano": st.column_config.NumberColumn(format="%d"),
                "Codigo": st.column_config.NumberColumn(format="%d")
             },
             hide_index=True
             )
