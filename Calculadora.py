import streamlit as st

# Título do aplicativo
st.title("Calculadora de Bons Negócios")
st.write("<p style='color: red;'>Essa é apenas uma visão comparativa com a taxa SELIC, não leva em consideração outros fatores administrativos</p>", unsafe_allow_html=True)
# Entrada da Previsão de Ganho Anual
ganho_anual = st.number_input("Previsão de Ganho em % Anual", min_value=0.0)

# Entrada do Nível de Risco
niveis_de_risco = ["Baixo Risco", "Médio Risco", "Alto Risco"]
nivel_risco = st.selectbox("Nível de Risco", niveis_de_risco)

# Taxa SELIC
selic = st.number_input("Taxa SELIC %", min_value=0.0)

# Função para verificar o critério de alto risco
def critico_medio_risco(ganho_anual, selic):
    return ganho_anual >= 1,5 * selic

# Função para verificar o critério de alto risco
def critico_alto_risco(ganho_anual, selic):
    return ganho_anual >= 2,5 * selic

# Botão para Calcular
if st.button("Calcular"):
    if nivel_risco == "Alto Risco" and not critico_alto_risco(ganho_anual, selic):
        st.write("Para investimentos de alto risco, o ganho anual deve ser pelo menos 2,5 vezes a SELIC, devido a proximidade de retorno financeiro.")
    if nivel_risco == "Médio Risco" and not critico_medio_risco(ganho_anual, selic):
        st.write("Considerar possibilidade de investir na renda fixa, devido a proximidade de retorno financeiro.")
    elif ganho_anual > selic:
        st.write("É um bom investimento!")
    else:
        st.write("Considere outras opções.")

# Dica informativa
st.info("Insira a previsão de ganho anual, a taxa SELIC e selecione o nível de risco para calcular se é um bom investimento.")


