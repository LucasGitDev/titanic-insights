# src/data/download.py
import os
import sys
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi


def check_kaggle_config():
    """Verifica se a configuração do Kaggle está correta"""
    kaggle_dir = Path.home() / ".kaggle"
    kaggle_json = kaggle_dir / "kaggle.json"

    if not kaggle_json.exists():
        print("❌ Arquivo kaggle.json não encontrado!")
        print("\n📋 Para configurar a API do Kaggle:")
        print("1. Acesse https://www.kaggle.com/settings/account")
        print("2. Clique em 'Create New API Token'")
        print("3. Baixe o arquivo kaggle.json")
        print("4. Coloque o arquivo em ~/.kaggle/kaggle.json")
        print("5. Execute: chmod 600 ~/.kaggle/kaggle.json")
        return False

    # Verifica permissões do arquivo
    if os.stat(kaggle_json).st_mode & 0o777 != 0o600:
        print("⚠️  Ajustando permissões do arquivo kaggle.json...")
        os.chmod(kaggle_json, 0o600)

    return True


def download_titanic(dest_path="data/raw"):
    """Download dos dados do Titanic do Kaggle"""
    if not check_kaggle_config():
        return False

    try:
        api = KaggleApi()
        api.authenticate()

        # Cria o diretório de destino
        os.makedirs(dest_path, exist_ok=True)

        print(f"📥 Baixando dados para {dest_path}...")

        # Download dos arquivos
        api.competition_download_file(
            "titanic", "train.csv", path=dest_path, force=True
        )
        api.competition_download_file("titanic", "test.csv", path=dest_path, force=True)

        print(f"✅ Dados baixados com sucesso em {dest_path}")
        return True

    except Exception as e:
        print(f"❌ Erro durante o download: {e}")
        return False


def main():
    """Função principal para download dos dados"""
    success = download_titanic()
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
