"""
Titanic Insights - Análise de Sobrevivência no Titanic
"""

__version__ = "0.1.0"
__author__ = "Lucas"


def main():
    """Função principal para executar o CLI"""
    from .cli import main as cli_main

    cli_main()


if __name__ == "__main__":
    main()
