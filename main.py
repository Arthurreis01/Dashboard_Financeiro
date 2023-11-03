import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("`Painel de controle financeiro da Empresa X`")

# Adicionando conteúdo ao sidebar

#coletar a base de dados
df = pd.read_csv("relatorio (4).csv", sep=";")
#separar a data da hora criando uma nova coluna #criar uma coluna só com os dias
df['Data']=pd.to_datetime(df['Data'])
#nova coluna
df['Data'] = df['Data'].dt.date
df_line= {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'],
    'Valor': [1916.70] * 9
}


#excluir colunas desnecessárias e excluir colunas canceladas
colunas_para_excluir = ['Código','N. Fiscal', 'Dispositivo']
df = df.drop(colunas_para_excluir, axis=1)
df= df.sort_values('Data')

#excluir linhas com cancelada

#colocar datas em formato de periodo mensal
df["Dia"] = df["Data"].apply(lambda x: str(x.month) + "-" + str(x.day))
df= df.sort_values('Dia')

df["Data"]= df["Data"].apply(lambda x: str(x.month) + "-" + str(x.year))

#criar base lateral com filtro de datas, categorias de vendas e categorias de despesas
st.sidebar.header('Painel de controle')

st.sidebar.subheader('Escolha o período')
Periodo = st.sidebar.select_slider("Mês", df["Data"].unique())
df_filtered = df[df["Data"] == Periodo]

st.sidebar.subheader('Veja se sua ideia vale um bom negócio com a calculadora automática !')
st.sidebar.markdown("[**Calculadora de bons negócios**](Calculador.py)")


#colocar em modo visual (vendas, ranking de categorias (despesas e receitas), indicadores, orçamento x realizado)
#vendas por mês
st.markdown('### INDICADORES DA EMPRESA')
col1, col2, col3 = st.columns(3)
col1.metric("Valor em caixa","RS 5.000,00", "R$ 5.600,00")
col2.metric("ROI", "5 ANOS", "2 ANOS")
col3.metric("PONTO DE EQULIBRIO", "R$ 1.950,00", "R$ 2.600,00")



col3, col4 = st.columns(2)

fig_vendas_mes = px.bar(df, x=df["Data"], y="Valor", title= "Vendas em cada mês em 2023")
st.write(fig_vendas_mes)

fig_line = px.line(df_line, x='Mês', y='Valor', title='Gráfico de Linhas com Valor Constante')
fig = make_subplots(rows=2, cols=1)

# Adicionar o gráfico de barras na primeira linha
fig.add_trace(go.Bar(x=df["Data"], y=df["Valor"], name="Vendas (Barras)"), row=1, col=1)

# Adicionar o gráfico de linhas na segunda linha
fig.add_trace(go.Scatter(x=df["Data"], y=df["Valor"], mode="lines", name="Vendas (Linhas)"), row=2, col=1)



fig_vendas = px.bar(df_filtered, x="Dia", y="Valor", title= "Vendas por dia em cada mês")
col3.plotly_chart(fig_vendas,use_container_width=True)

fig_receitas = px.bar(df_filtered,x="Valor",y="Vendedor",orientation="h", title="Vendas por categoria", color="Vendedor")
col4.plotly_chart(fig_receitas, use_container_width=True)
