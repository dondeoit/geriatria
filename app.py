import streamlit as st
import plotly.graph_objects as go

# Configuração para ocultar a barra superior do Streamlit (Fork e Menu)
st.set_page_config(
    page_title="Avaliação de Risco de Queda",
    page_icon="👴🏻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ocultar o menu superior e o rodapé do Streamlit Cloud
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Lista de perguntas e seus pesos
perguntas_pesos = [
	("Levanta-se da cama sozinho?", 1),
	("Consegue vestir-se sozinho?", 1),
	("Consegue tomar banho sozinho?", 1),
	("Consegue preparar refeiçoes ou lanches sozinho?", 1),
	("Faz compras de casa (supermercado) sozinho?", 1),
	("Mora sozinho?", 1),
	("Necessita ou tem algum tipo de acompanhamento durante o dia e/ou à noite?", 1),
	("Faz uso de medicações todos os dias? Qual o número de medicamentos?", 1),
	("Já sofreu alguma queda nos últimos 5 anos?", 1),
	("Já esteve hospitalizado nos ultimos 12 meses?", 1),
	("Tem alguma deficiência auditiva?", 1),
	("Tem alguma deficiência visual?", 1),
	("Apresenta falta de equilíbrio ou tem mobilidade reduzida?", 1),
	("Usa bengala ou andador?", 2),
	("Usa cadeira de rodas?", 3),
	("Está acamado?", 4),
	("Tem algum sinal de desânimo, tristeza ou depressão?", 1),
	("Tem algum sinal de perda de memória?", 1),
	("Acorda à noite para ida(s) ao banheiro?", 1),
	("Tem algum sinal de incontinência urinária?", 1),
	("Tem algum sinal de incontinência fecal?", 1),
	("Recebe visitas (ou faz saídas) regulares de amigos ou familiares?", 1),
	("Mora junto de familiares (esposa, filhos, parentes)?", 1),
	("Mora numa casa adaptada (banheiro, corrimão, luz de emergência)?", 1),
	("Pratica regularmente exercícios físicos (caminhada, academias, fisioterapia)?" 1),
]

# Interface do Usuário
st.title("🧓🏼👴🏻 Avaliação de Risco de Queda para Idosos")


# Criando um separador visual
st.write("**Marque 'Sim' para as condições que se aplicam ao idoso.**")

# Criando os toggles (botões liga/desliga)
score = 0
for pergunta, peso in perguntas_pesos:
    resposta = st.toggle(f"{pergunta} (Sim / Não)", value=False)  # Falso por padrão
    if resposta:  # Se for marcado como SIM, soma o peso
        score += peso

# Determinando o nível de risco e cor
if score <= 10:
    cor = "green"
    risco = "Baixo"
elif score <= 15:
    cor = "yellow"
    risco = "Moderado"
else:
    cor = "red"
    risco = "Alto"

# Criando o velocímetro
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': "Nível de Risco"},
    gauge={'axis': {'range': [0, 20]},
           'bar': {'color': cor},
           'steps': [
               {'range': [0, 10], 'color': "lightgreen"},
               {'range': [11, 15], 'color': "yellow"},
               {'range': [16, 20], 'color': "red"}
           ]}
))

# Exibindo o velocímetro no Streamlit
st.plotly_chart(fig)

# Exibindo a classificação final
st.write(f"**Classificação do risco:** {risco}")


