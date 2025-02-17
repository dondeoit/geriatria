import streamlit as st
import plotly.graph_objects as go

# Definição das perguntas
perguntas = [
	"Levanta-se da cama sozinho?",
	"Consegue vestir-se sozinho?",
	"Consegue tomar banho sozinho?",
	"Consegue preparar refeiçoes ou lanches sozinho?",
	"Faz compras de casa (supermercado) sozinho?",
	"Mora sozinho?",
	"Necessita ou tem algum tipo de acompanhamento durante o dia e/ou à noite?",
	"Faz uso de medicações todos os dias? Qual o número de medicamentos?",
	"Já sofreu alguma queda nos últimos 5 anos?",
	"Já esteve hospitalizado nos ultimos 12 meses?",
	"Tem alguma deficiência auditiva?",
	"Tem alguma deficiência visual?",
	"Apresenta falta de equilíbrio ou tem mobilidade reduzida?",
	"Usa bengala ou andador?",
	"Usa cadeira de rodas?",
	"Está acamado?",
	"Tem algum sinal de desânimo, tristeza ou depressão?",
	"Tem algum sinal de perda de memória?",
	"Acorda à noite para ida(s) ao banheiro?",
	"Tem algum sinal de incontinência urinária?",
	"Tem algum sinal de incontinência fecal?",
	"Recebe visitas (ou faz saídas) regulares de amigos ou familiares?",
	"Mora junto de familiares (esposa, filhos, parentes)?",
	"Mora numa casa adaptada (banheiro, corrimão, luz de emergência)?",
	"Pratica regularmente exercícios físicos (caminhada, academias, fisioterapia)?"
]

# Interface do Usuário
st.title("🧓🏼👴🏻 Avaliação de Risco de Queda para Idosos")

# Criando checkboxes para as perguntas
respostas = [st.checkbox(q) for q in perguntas]

# Calculando a pontuação
score = sum(respostas)

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
               {'range': [16, 30], 'color': "red"}
           ]}
))

# Exibindo o velocímetro no Streamlit
st.plotly_chart(fig)

# Exibindo a classificação final
st.write(f"**Classificação do risco:** {risco}")

