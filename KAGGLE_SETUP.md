# 🔑 Configuração da API do Kaggle

Para usar o download automático dos dados do Titanic, você precisa configurar a API do Kaggle.

## 📋 Passos para Configuração

### 1. Criar Conta no Kaggle

- Acesse [Kaggle.com](https://www.kaggle.com)
- Crie uma conta gratuita

### 2. Gerar Token da API

1. Faça login no Kaggle
2. Acesse: https://www.kaggle.com/settings/account
3. Role até a seção "API"
4. Clique em **"Create New API Token"**
5. Isso baixará um arquivo `kaggle.json`

### 3. Configurar o Token

1. Crie o diretório `.kaggle` na sua pasta home:

   ```bash
   mkdir ~/.kaggle
   ```
2. Mova o arquivo `kaggle.json` para o diretório:

   ```bash
   mv ~/Downloads/kaggle.json ~/.kaggle/
   ```
3. Configure as permissões corretas (importante!):

   ```bash
   chmod 600 ~/.kaggle/kaggle.json
   ```

### 4. Verificar Configuração

Teste se a configuração está funcionando:

```bash
kaggle competitions list
```

## 🚀 Usando o CLI

Após configurar a API, você pode usar:

```bash
# Modo interativo
poetry run titanic-cli

# Comando direto
poetry run titanic-cli download
```

## 🔧 Estrutura do arquivo kaggle.json

O arquivo deve conter:

```json
{
  "username": "seu_usuario_kaggle",
  "key": "sua_chave_api_kaggle"
}
```

## ❗ Problemas Comuns

### Erro: "Could not find kaggle.json"

- Verifique se o arquivo está em `~/.kaggle/kaggle.json`
- Verifique se as permissões estão corretas (600)

### Erro: "403 Forbidden"

- Verifique se o username e key estão corretos
- Verifique se a conta do Kaggle está ativa

### Erro: "Permission denied"

- Execute: `chmod 600 ~/.kaggle/kaggle.json`

## 📞 Suporte

Se tiver problemas, consulte a [documentação oficial do Kaggle API](https://github.com/Kaggle/kaggle-api).
