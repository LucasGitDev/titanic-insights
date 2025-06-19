# 🚢 Titanic Insights

Pipeline de Machine Learning para análise de sobrevivência no Titanic.

## 📋 Sobre o Projeto

Este projeto implementa um pipeline completo de Machine Learning para analisar e prever a sobrevivência de passageiros do Titanic. Inclui:

- 📥 Download automático dos dados
- 🔍 Exploração e análise dos dados
- 🧹 Pré-processamento
- 🤖 Treinamento de modelos
- 📊 Avaliação e métricas
- 📈 Geração de insights

## 🚀 Como Iniciar o Projeto

### Pré-requisitos

- Python 3.11+
- Poetry (gerenciador de dependências)

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
cd titanic-insights
```

### 2. Instale as Dependências

```bash
# Instalar Poetry (se não tiver)
curl -sSL https://install.python-poetry.org | python3 -

# Instalar dependências do projeto
poetry install
```

### 3. Configure a API do Kaggle (Obrigatório para Download)

Para baixar os dados automaticamente, você precisa configurar a API do Kaggle:

#### Opção A: Configuração Automática
```bash
# O CLI irá guiar você através do processo
poetry run titanic-cli download
```

#### Opção B: Configuração Manual
1. Acesse [Kaggle.com](https://www.kaggle.com) e crie uma conta
2. Vá para [Settings > Account](https://www.kaggle.com/settings/account)
3. Clique em "Create New API Token"
4. Baixe o arquivo `kaggle.json`
5. Configure:
```bash
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

📖 **Instruções detalhadas**: Veja [KAGGLE_SETUP.md](KAGGLE_SETUP.md)

### 4. Baixe os Dados

#### Usando o CLI (Recomendado)
```bash
# Modo interativo
poetry run titanic-cli

# Ou comando direto
poetry run titanic-cli download
```

#### Download Manual (Alternativo)
Se preferir não configurar a API do Kaggle:
1. Acesse: https://www.kaggle.com/c/titanic/data
2. Baixe `train.csv` e `test.csv`
3. Coloque os arquivos em `data/raw/`

### 5. Explore o Projeto

```bash
# Abrir Jupyter Lab
poetry run titanic-cli jupyter

# Ou abrir notebook específico
jupyter lab notebooks/00_exploracao.ipynb
```

## 🛠️ Uso do CLI

O projeto inclui um CLI interativo e profissional para facilitar o uso:

### Modo Interativo
```bash
poetry run titanic-cli
```

### Comandos Diretos
```bash
# Download dos dados
poetry run titanic-cli download

# Explorar dados (abre Jupyter)
poetry run titanic-cli explore

# Abrir Jupyter Lab
poetry run titanic-cli jupyter

# Ver informações do projeto
poetry run titanic-cli info

# Ver versão
poetry run titanic-cli version
```

### Scripts Disponíveis
```bash
# Download direto via script
poetry run download-data
```

## 📁 Estrutura do Projeto

```
titanic-insights/
├── data/
│   ├── raw/              # Dados brutos (train.csv, test.csv)
│   └── processed/        # Dados pré-processados
├── models/               # Modelos treinados salvos
├── reports/              # Relatórios e insights gerados
├── notebooks/
│   └── 00_exploracao.ipynb  # Notebook de exploração
├── src/
│   ├── data/
│   │   └── download.py   # Script de download
│   ├── features/         # Engenharia de features
│   ├── models/           # Treinamento e avaliação
│   └── visualization/    # Visualizações e gráficos
├── titanic_insights/
│   ├── __init__.py
│   └── cli.py           # CLI interativo
├── tests/
├── pyproject.toml       # Configuração do Poetry
├── README.md
└── KAGGLE_SETUP.md      # Guia de configuração do Kaggle
```

## 🔧 Desenvolvimento

### Adicionar Novas Dependências
```bash
poetry add nome-do-pacote
poetry add --group dev nome-do-pacote-dev
```

### Executar Testes
```bash
poetry run pytest
```

### Formatação de Código
```bash
poetry run black .
poetry run isort .
```

## 📊 Funcionalidades

- ✅ **Download Automático**: Baixa dados do Kaggle automaticamente
- ✅ **CLI Interativo**: Interface amigável para todas as operações
- ✅ **Exploração de Dados**: Notebooks para análise exploratória
- 🔄 **Pré-processamento**: Em desenvolvimento
- 🔄 **Treinamento de Modelos**: Em desenvolvimento
- 🔄 **Avaliação**: Em desenvolvimento
- 🔄 **Geração de Insights**: Em desenvolvimento

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Lucas** - [devlucasteles@gmail.com](mailto:devlucasteles@gmail.com)

## 🙏 Agradecimentos

- [Kaggle](https://www.kaggle.com) pelos dados do Titanic
- [Poetry](https://python-poetry.org/) pelo gerenciamento de dependências
- [Click](https://click.palletsprojects.com/) e [Rich](https://rich.readthedocs.io/) pelo CLI profissional
