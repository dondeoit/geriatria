import streamlit as st
import plotly.graph_objects as go

# Configuração de página
st.set_page_config(
    page_title="Calculadora de Risco Human Care Brasil",
    page_icon="👴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar menu e rodapé do Streamlit e ajustar estilos
ocultar_estilo = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Estilos para alinhar os itens */
    .nao-sim-container {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;  /* Garante que não quebre o layout */
        gap: 10px;
        width: 100%;
    }

    .nao-sim-container > div {
        text-align: center;
        flex: 1; /* Permite ajuste automático da largura */
    }

    /* Ajuste para o toggle */
    .stToggle {
        margin: 0;
        transform: scale(1.3);
    }

    /* Remover "False" da tela */
    .st-bo {
        display: none !important;
    }

    /* Responsividade */
    @media (max-width: 768px) {
        .nao-sim-container {
            flex-direction: row;
            gap: 5px;
        }

        .nao-sim-container > div {
            flex: 1;
        }
    }
    </style>
"""
st.markdown(ocultar_estilo, unsafe_allow_html=True)

# Lista de perguntas e seus pesos
perguntas_pesos = [
	("1.1 Precisa de auxílio para se levantar cama da cama?", 1),
	("1.2 Tem dificuldades para se vestir sozinho?", 1),
	("1.3 Preciso de apoio ao tomar banho?", 1),
	("1.4 Suas refeições e lanches precisam ser preparadas por outra pessoa?", 1),
	("1.5 Possui alguma dificuldade em realzi0ar compras de casa (supermercado) sozinho?", 1),
	("2.1 Gostaria de morar sozinho, mas não pode?", 1),
	("2.2 Necessita ou tem algum tipo de acompanhamento durante o dia e/ou à noite?", 1),
	("2.3 Faz uso de medicações todos os dias? Qual o número de medicamentos?", 1),
	("2.4 Já sofreu alguma queda nos últimos 5 anos?", 1),
	("2.5 Já esteve hospitalizado nos ultimos 12 meses?", 1),
	("3.1 Tem alguma deficiência auditiva?", 1),
	("3.2 Tem alguma deficiência visual?", 1),
	("3.3 Apresenta falta de equilíbrio ou tem mobilidade reduzida?", 1),
	("3.4 Usa bengala ou andador?", 2),
	("3.5 Usa cadeira de rodas?", 3),
	("3.6 Está acamado?", 4),
	("3.7 Tem algum sinal de desânimo, tristeza ou depressão?", 1),
	("3.8 Tem algum sinal de perda de memória?", 1),
	("3.9 Acorda à noite para ida(s) ao banheiro?", 1),
	("3.10 Tem algum sinal de incontinência urinária?", 1),
	("3.11 Tem algum sinal de incontinência fecal?", 1),
	("3.12 Faz tempo que não recebe visitas (ou sai de casa) regulares de amigos ou familiares?", 1),
	("3.13 Você acha que não precisa adaptar sua casa (banheiro, corrimão, luz de emergência)?", 1),
	("3.14 Se sente ocioso, ou seja, evita a prática regular de exercícios físicos?", 1),
]

# Título e subtítulo
st.title("👵👴 CALCULADORA DE DECLÍNIO E RISCO CLÍNICO/FUNCIONAL")
st.write("**Responda 'Sim' ou 'Não' para cada pergunta abaixo.**")

score = 0
for i, (pergunta, peso) in enumerate(perguntas_pesos):
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"**{pergunta}**")

    with col2:
        # Criando a estrutura correta para alinhar "NÃO", Toggle e "SIM"
        col_nao, col_toggle, col_sim = st.columns([1, 1, 1])

        with col_nao:
            st.write("NÃO")

        with col_toggle:
            resposta = st.toggle("", key=f"toggle_{i}")

        with col_sim:
            st.write("SIM")

    # Soma a pontuação se a resposta for SIM
    if resposta:
        score += peso

# Define o risco com base no score
if score <= 10:
    cor = "green"
    risco = "Baixo"
elif score <= 15:
    cor = "orange"
    risco = "Moderado"
else:
    cor = "darkred"
    risco = "Alto"

# Criar velocímetro
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': "Nível de Risco"},
    gauge={
        'axis': {'range': [0, 25]},
        'bar': {'color': cor},
        'steps': [
            {'range': [0, 10], 'color': "lightgreen"},
            {'range': [10, 15], 'color': "yellow"},
            {'range': [15, 25], 'color': "red"}
        ]
    }
))

# Exibe velocímetro e classificação
st.plotly_chart(fig)
st.write(f"**Classificação do risco:** {risco}")
