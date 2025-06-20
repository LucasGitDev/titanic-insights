import pandas as pd
import requests

import streamlit as st

# API endpoint
API_URL = "http://127.0.0.1:8000/predict"

# --- Page Configuration ---
st.set_page_config(
    page_title="Titanic Insights - Test Suite",
    page_icon="🚢",
    layout="wide",
)


# --- Functions ---
def get_prediction(passenger_data):
    """Faz uma requisição para a API e retorna a predição."""
    try:
        response = requests.post(API_URL, json=passenger_data)
        response.raise_for_status()  # Gera uma exceção para códigos de status ruins
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def display_prediction(prediction, header):
    """Exibe o resultado da predição em um formato agradável."""
    st.subheader(header)
    if "error" in prediction:
        st.error(f"Erro ao conectar com a API: {prediction['error']}")
        st.warning(
            "Certifique-se de que a API está rodando. Use o comando `titanic-insights api` em outro terminal."
        )
    elif "survival_probability" in prediction:
        prob = prediction["survival_probability"]
        st.metric(label="Probabilidade de Sobrevivência", value=f"{prob:.0%}")

        # Converte a probabilidade para float para a barra de progresso
        progress_val = (
            float(prob)
            if isinstance(prob, (int, float))
            else float(prob.replace("%", "")) / 100
        )
        st.progress(progress_val)

        if progress_val > 0.5:
            st.success("Alta chance de sobreviver.")
        else:
            st.error("Baixa chance de sobreviver.")
    else:
        st.error("Resposta inesperada da API.")


# --- Casos de Teste Pré-definidos ---
predefined_cases = {
    "Rose (Mulher, 1ª Classe, Jovem)": {
        "Pclass": 1,
        "Sex": "female",
        "Age": 17.0,
        "SibSp": 1,
        "Parch": 2,
        "Fare": 150.0,
        "Embarked": "S",
    },
    "Jack (Homem, 3ª Classe, Jovem)": {
        "Pclass": 3,
        "Sex": "male",
        "Age": 20.0,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 8.0,
        "Embarked": "S",
    },
    "Criança da 2ª Classe": {
        "Pclass": 2,
        "Sex": "male",
        "Age": 4.0,
        "SibSp": 1,
        "Parch": 1,
        "Fare": 30.0,
        "Embarked": "S",
    },
    "Homem de Negócios (1ª Classe, Meia-idade)": {
        "Pclass": 1,
        "Sex": "male",
        "Age": 45.0,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 50.0,
        "Embarked": "C",
    },
    "Família Grande (3ª Classe)": {
        "Pclass": 3,
        "Sex": "female",
        "Age": 35.0,
        "SibSp": 1,
        "Parch": 5,
        "Fare": 31.0,
        "Embarked": "S",
    },
}

# --- Layout Principal da Aplicação ---
st.title("🚢 Teste de Integração Visual - Titanic Insights")
st.markdown(
    """
Esta aplicação é uma suíte de testes visuais para a API de predição de sobrevivência do Titanic.
Ela envia requisições para a API rodando em `http://127.0.0.1:8000` e exibe os resultados.

**Use o menu na barra lateral para criar e testar seu próprio passageiro!**
"""
)

with st.expander("Clique para ver a Tese de Negócio e as Hipóteses do Projeto"):
    st.markdown(
        """
    ### A Pergunta de Negócio
    > “Como viajar em família (vs. sozinho) afeta a chance de sobrevivência, e como essa influência varia conforme a idade do passageiro?”

    Isso nos leva a duas hipóteses concretas:

    1.  **Hipótese 1:** Passageiros que viajam sozinhos (*travelling alone*) têm taxa de sobrevivência menor que os que viajam em grupos.
    2.  **Hipótese 2:** O efeito de “viajar em família” na sobrevivência é diferente para crianças, adultos e idosos.
    
    ---

    ### Fatores que Mais Influenciam a Sobrevivência

    Ao longo da análise exploratória e de modelos preditivos simples (Logistic Regression), observamos que:

    * **Sexo (Sex)**
      – Fator mais determinante: mulheres tiveram muito maior chance de sobreviver que homens ("women and children first").

    * **Classe da Cabine (Pclass)**
      – Passageiros de 1ª classe sobreviveram em proporções bem maiores que os da 2ª e 3ª classes, refletindo acesso mais fácil aos botes.

    * **Tamanho da Família (HouseholdSize / IsAlone)**
      – Grupos familiares tendem a cuidar uns dos outros, coordenar embarques e chegar juntos aos pontos de evacuação. Quem viajou sozinho ficou sem rede de apoio.

    * **Idade (Age / AgeGroup)**
      – Crianças ("Child") receberam prioridade no resgate, mas também dependem de acompanhantes; idosos ("Senior") mostram dependência mista: alguns sobreviveram protegidos por familiares, outros ficaram para trás.

    * **Tarifa (Fare)**
      – Tarifa mais alta ("Fare") normalmente correlaciona-se com cabines melhores e locais mais elevados no convés, facilitando o acesso aos botes.

    * **Porto de Embarque (Embarked)**
      – Há pequenas variações: por exemplo, quem embarcou em Cherbourg ("C") exibiu uma ligeira vantagem no dataset, possivelmente por seleção de perfil socioeconômico.

    ---

    Nosso pipeline de modelagem colocará à prova essas hipóteses, usando features de **HouseholdSize**, **IsAlone**, **AgeGroup** e demais variáveis de controle (Sexo, Pclass, Fare, Embarked). Ao final, extrairemos as importâncias das features e as métricas de performance para confirmar ou refutar cada hipótese.
    """
    )

st.header("Casos de Teste Pré-definidos")

# Verifica se a API está online antes de prosseguir
try:
    requests.get("http://127.0.0.1:8000/", timeout=3)
except requests.ConnectionError:
    st.error(
        "A API de predição não parece estar rodando. Por favor, inicie-a com o comando `titanic-insights api` em outro terminal antes de continuar."
    )
    st.stop()

# Layout em colunas para os casos
cols = st.columns(len(predefined_cases))
for i, (name, data) in enumerate(predefined_cases.items()):
    with cols[i]:
        st.info(f"**{name}**")
        prediction = get_prediction(data)

        prob_float = float(prediction.get("survival_probability", 0))
        st.metric(label="Sobrevivência", value=f"{prob_float:.0%}")
        st.progress(prob_float)

        with st.expander("Ver dados de entrada"):
            st.json(data)


# --- Barra Lateral Interativa para Passageiro Customizado ---
st.sidebar.header("Criar e Testar Passageiro")

pclass = st.sidebar.selectbox("Classe do Ticket", [1, 2, 3], key="pclass")
sex = st.sidebar.selectbox("Sexo", ["male", "female"], key="sex")
age = st.sidebar.slider("Idade", 0, 100, 30, key="age")
sibsp = st.sidebar.number_input(
    "Nº de Irmãos/Cônjuges", min_value=0, max_value=10, value=0, key="sibsp"
)
parch = st.sidebar.number_input(
    "Nº de Pais/Filhos", min_value=0, max_value=10, value=0, key="parch"
)
fare = st.sidebar.number_input(
    "Tarifa ($)", min_value=0.0, max_value=600.0, value=50.0, step=0.1, key="fare"
)
embarked = st.sidebar.selectbox("Porto de Embarque", ["S", "C", "Q"], key="embarked")

custom_passenger = {
    "Pclass": pclass,
    "Sex": sex,
    "Age": float(age),
    "SibSp": sibsp,
    "Parch": parch,
    "Fare": fare,
    "Embarked": embarked,
}

if st.sidebar.button("Verificar Sobrevivência"):
    prediction = get_prediction(custom_passenger)
    display_prediction(prediction, "Resultado da Predição para Passageiro Customizado")
