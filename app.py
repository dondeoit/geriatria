import streamlit as st
import plotly.graph_objects as go

# Configuração de página
st.set_page_config(
    page_title="Avaliação de Risco de Queda",
    page_icon="👴🏻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ocultar menu e rodapé do Streamlit
ocultar_estilo = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(ocultar_estilo, unsafe_allow_html=True)

# Lista de perguntas (com pesos)
perguntas_pesos = [
    ("Levanta-se da cama sozinho?", 1),
    ("Consegue vestir-se sozinho?", 1),
    ("Consegue tomar banho sozinho?", 1),
    ("Consegue preparar refeições ou lanches sozinho?", 1),
    ("Faz compras de casa (supermercado) sozinho?", 1),
    ("Mora sozinho?", 1),
    ("Necessita ou tem algum tipo de acompanhamento durante o dia e/ou à noite?", 1),
    ("Faz uso de medicações todos os dias? Qual o número de medicamentos?", 1),
    ("Já sofreu alguma queda nos últimos 5 anos?", 1),
    ("Já esteve hospitalizado nos últimos 12 meses?", 1),
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
    ("Pratica regularmente exercícios físicos (caminhada, academia, fisioterapia)?", 1),	]

# Título e subtítulo
st.title("👵👴 Avaliação de Risco de Queda para Idosos")
st.write("**Responda 'Sim' ou 'Não' para cada pergunta abaixo.**")

score = 0
for pergunta, peso in perguntas_pesos:
    # Cria duas colunas horizontais: 
    #   1) Pergunta 
    #   2) "NÃO", Toggle, "SIM"
    col_esq, col_dir = st.columns([3, 2])
    
    # Coluna da Esquerda: Exibe a pergunta
    col_esq.write(f"**{pergunta}**")
    
    # Coluna da Direita: Divide em 3 subcolunas para alinhar "NÃO", Toggle e "SIM"
    with col_dir:
        sub1, sub2, sub3 = st.columns([1,1,1])
        
        with sub1:
            st.write("NÃO")
        
        with sub2:
            resposta = st.toggle("", key=pergunta)
        
        with sub3:
            st.write("SIM")
    
    # Soma a pontuação se a resposta for SIM
    if resposta:
        score += peso

# Define o risco com base no score
if score <= 10:
    cor = "green"
    risco = "Baixo"
elif score <= 15:
    cor = "yellow"
    risco = "Moderado"
else:
    cor = "red"
    risco = "Alto"

# Cria o velocímetro
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': "Nível de Risco"},
    gauge={
        'axis': {'range': [0, 20]},
        'bar': {'color': cor},
        'steps': [
            {'range': [0, 10], 'color': "lightgreen"},
            {'range': [11, 15], 'color': "yellow"},
            {'range': [16, 20], 'color': "red"}
        ]
    }
))

# Exibe o velocímetro
st.plotly_chart(fig)

# Exibe a classificação
st.write(f"**Classificação do risco:** {risco}")
