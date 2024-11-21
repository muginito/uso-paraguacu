import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def filtrar_multi(df, label, coluna, **kwargs):
    filtro = st.multiselect(label, df[coluna].unique(), **kwargs)
    if filtro:
        return df[df[coluna].isin(filtro)]
    return df

def filtrar(df, label, coluna, **kwargs):
    filtro = st.selectbox(label, np.insert(df[coluna].unique(), 0, "Todos"), **kwargs)
    if filtro and filtro != "Todos":
        return df[df[coluna] == filtro]
    return df

def pie_graph(ano):
    fig = px.pie(
        filtro_tipos[filtro_tipos["Ano"] == ano],
        names="Município",
        values="Área (Ha)",
        title=f"Uso para {filtro_tipos["Uso para"].unique()[0]} em {ano}",
        width=300
    )
    return fig

def filtrar_grafico(df, label, coluna, **kwargs):
    filtro = st.multiselect(label, df[coluna].unique(), **kwargs)
    if filtro:
        df_filtrado = df[df[coluna].isin(filtro)]

        fig = px.bar(
            df_filtrado,
            x='Ano',
            y='Área (Ha)',
            color='Município',
            barmode='group',
            title='Medidas de Áreas por Ano e Município',
            height=500
        )

        return fig


st.header("Tabela")

url = st.secrets["USOPARAGUACU"]

df = pd.read_csv(url)

df.rename(columns={
            "Nome" : "Uso para",
            "Area" : "Área (Ha)",
            "Codigo" : "Código",
            "MUNICIPIO" : "Município",
            "BACIA" : "Bacia"
        },
        inplace=True
        )

# df["Ano"] = pd.to_datetime(df["Ano"], format="%Y")
with st.container(key="tabela"):

    filtro_cidades = filtrar_multi(df, "Municípios", "Município")

    filtro_tipos = filtrar(filtro_cidades, "Tipos de uso", "Uso para")

    st.dataframe(filtro_tipos,
                use_container_width=True,
                height=500,
                column_config={
                    "Ano": st.column_config.NumberColumn(format="%d"),
                    "Código": st.column_config.NumberColumn(format="%d"),
                    "Área (Ha)": st.column_config.NumberColumn(format="%.2f")
                },
                hide_index=True
                )


# TODO Decidir como insrir essa tabela. Talvez usando streamlit tabs. Ou não usar

# Tabela com área por ano
# df_pivot = df.pivot_table(values='Área (Ha)', index=['Município', 'Código', 'Uso para', 'Bacia'], columns='Ano', fill_value=0)
# df_pivot.columns = ['Área (Ha) 2000', 'Área (Ha) 2010', 'Área (Ha) 2022']
# df_final = df_pivot.reset_index()

# st.dataframe(df_final[['Município', 'Código', 'Uso para', 'Área (Ha) 2000', 'Área (Ha) 2010', 'Área (Ha) 2022','Bacia']],
#              column_config={
#                 "Código": st.column_config.NumberColumn(format="%d")
#              },
#              hide_index=True
#              )


# df_grafico = filtrar(df, "Municípios", "Município")

# fig = filtrar_grafico(df_grafico, "Uso para", "Uso para")

with st.container(border=True, key="graficos"):
    if len(filtro_tipos["Município"].unique()) < 8 and len(filtro_tipos["Uso para"].unique()) == 1:

        st.write(f"### Uso para {filtro_tipos["Uso para"].unique()[0]}")

        # TODO usar plotlyd para esse gráfico e desabilitar algumas interações com o mouse
        st.bar_chart(filtro_tipos, x='Ano', y='Área (Ha)', color="Município", stack=False)


        col1, col2, col3 = st.columns(3, vertical_alignment="center")

        with col1:
            st.plotly_chart(pie_graph(2000))

        with col2:
            st.plotly_chart(pie_graph(2010))

        with col3:
            st.plotly_chart(pie_graph(2022))
    else:
        st.info('''**Para exibir gráficos**:

- Selecione até sete municípios
- "Tipos de uso" deve ser diferente de "Todos"
''', icon=":material/info:")
