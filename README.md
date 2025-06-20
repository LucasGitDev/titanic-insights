# Titanic Insights 🚢

Análise completa e pipeline de Machine Learning para o clássico desafio do Kaggle: prever a sobrevivência de passageiros no desastre do Titanic. Este projeto implementa um fluxo de trabalho de ponta a ponta, desde o download dos dados até a implantação de uma API de predição.

![Interface da CLI](https://raw.githubusercontent.com/lucasgitdev/titanic-insights/main/reports/figures/cli_screenshot.png)

## ✨ Funcionalidades

- **CLI Interativa:** Uma interface de linha de comando moderna e amigável construída com `Click` e `Rich` para gerenciar todo o pipeline.
- **Pipeline de ML:** Etapas bem definidas para download, pré-processamento, treinamento e avaliação de modelos.
- **Engenharia de Features:** Criação de novas features para melhorar a performance do modelo.
- **API de Predição:** Uma API FastAPI com documentação Swagger interativa para realizar predições em tempo real.
- **Ambiente Reproduzível:** Gerenciamento de dependências com `Poetry` para garantir a consistibilidade.
- **Jupyter Lab Integrado:** Fácil acesso ao ambiente de exploração de dados.

## 🚀 Começando

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

- Python 3.11 ou superior
- [Poetry](https://python-poetry.org/docs/#installation) para gerenciamento de dependências.

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/lucasgitdev/titanic-insights.git
   cd titanic-insights
   ```
2. **Instale as dependências:**
   Use o Poetry para criar um ambiente virtual e instalar todos os pacotes necessários.

   ```bash
   poetry install
   ```
3. **Ative o ambiente virtual:**

   ```bash
   poetry shell
   ```

## 💻 Uso

A principal forma de interagir com o projeto é através da CLI.

### CLI Interativa

Para uma experiência guiada, execute o modo interativo:

```bash
titanic-insights
```

Você verá um menu com todas as opções disponíveis:

```
📋 Menu Principal
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Opção ┃ Descrição                ┃ Status      ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1     │ 📥 Download dos dados    │ ✅ Disponível │
│ 2     │ 🔍 Explorar dados        │ ✅ Disponível │
│ 3     │ 🧹 Pré-processar dados   │ ✅ Disponível │
│ 4     │ 🤖 Treinar modelo        │ ✅ Disponível │
│ 5     │ 📊 Avaliar modelo        │ ✅ Disponível │
│ 6     │ 📈 Gerar insights        │ 🔄 Em desenvolvimento │
│ 7     │ 📝 Abrir Jupyter Lab     │ ✅ Disponível │
│ 8     │ 🚀 Iniciar API           │ ✅ Disponível │
│ 0     │ ❌ Sair                  │ ✅ Disponível │
└───────┴──────────────────────────┴─────────────┘
```

### Comandos Diretos

Você também pode executar cada etapa do pipeline como um comando direto:

- **Download dos dados do Kaggle:**

  ```bash
  titanic-insights download
  ```

  *(Requer configuração do `kaggle.json`. Veja `KAGGLE_SETUP.md`)*
- **Pré-processar os dados:**

  ```bash
  titanic-insights preprocess
  ```
- **Treinar o modelo:**

  ```bash
  titanic-insights train
  ```
- **Avaliar o modelo salvo:**

  ```bash
  titanic-insights evaluate
  ```
- **Iniciar a API de predição:**

  ```bash
  titanic-insights api
  ```
- **Abrir o Jupyter Lab:**

  ```bash
  titanic-insights jupyter
  ```

## 🌐 API de Predição

Para iniciar o servidor da API, execute o comando:

```bash
titanic-insights api
```

A API estará disponível em `http://127.0.0.1:8000`.

A documentação interativa do Swagger UI, onde você pode testar os endpoints diretamente do navegador, está em:
[**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs)

## 📁 Estrutura do Projeto

```
.
├── data/                    # Dados brutos, processados e externos
├── models/                  # Modelos treinados (.joblib)
├── notebooks/               # Notebooks Jupyter para exploração e experimentação
├── reports/                 # Relatórios e figuras geradas
├── src/                     # Código fonte do projeto
│   ├── api/                 # Módulo da API FastAPI
│   ├── data/                # Scripts para download e manipulação de dados
│   ├── model/               # Scripts para treinamento e avaliação de modelos
│   └── processing/          # Scripts para pré-processamento e engenharia de features
├── tests/                   # Testes automatizados
├── titanic_insights/        # Módulo da CLI
└── poetry.toml              # Arquivo de configuração do Poetry
```

## 🛠️ Ferramentas Utilizadas

- **Linguagem:** Python 3.11
- **CLI:** Click, Rich
- **API:** FastAPI, Uvicorn
- **Machine Learning:** Scikit-learn, Pandas
- **Dependências:** Poetry
- **Notebooks:** Jupyter Lab

---

Desenvolvido por Teles, Goulart e Ross.
