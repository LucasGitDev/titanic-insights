#!/usr/bin/env python3

import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

import click
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text

console = Console()

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def print_banner():
    banner_text = Text()
    banner_text.append("🚢 ", style="bold blue")
    banner_text.append("TITANIC INSIGHTS", style="bold white on blue")
    banner_text.append(" 🚢", style="bold blue")
    banner_text.append("\nAnálise de Sobrevivência no Titanic", style="italic cyan")

    panel = Panel(banner_text, border_style="blue", box=box.DOUBLE, padding=(1, 2))
    console.print(panel)


def print_menu():
    table = Table(
        title="📋 Menu Principal",
        box=box.ROUNDED,
        border_style="blue",
        title_style="bold white",
    )

    table.add_column("Opção", style="cyan", no_wrap=True)
    table.add_column("Descrição", style="white")
    table.add_column("Status", style="green")

    menu_items = [
        ("1", "📥 Download dos dados", "✅ Disponível"),
        ("2", "🔍 Explorar dados", "✅ Disponível"),
        ("3", "🧹 Pré-processar dados", "✅ Disponível"),
        ("4", "🤖 Treinar modelo", "✅ Disponível"),
        ("5", "📊 Avaliar modelo", "✅ Disponível"),
        ("6", "📈 Gerar insights", "🔄 Em desenvolvimento"),
        ("7", "📝 Abrir Jupyter Lab", "✅ Disponível"),
        ("8", "🚀 Iniciar API", "✅ Disponível"),
        ("9", "🧪 Teste Visual da API", "✅ Disponível"),
        ("0", "❌ Sair", "✅ Disponível"),
    ]

    for option, description, status in menu_items:
        table.add_row(option, description, status)

    console.print(table)


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        interactive_mode()


def interactive_mode():
    while True:
        console.clear()
        print_banner()
        print_menu()

        try:
            choice = Prompt.ask(
                "\n[bold cyan]Escolha uma opção[/bold cyan]",
                choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                default="0",
            )

            if choice == "0":
                if Confirm.ask("Tem certeza que deseja sair?"):
                    console.print(
                        "\n[green]👋 Obrigado por usar o Titanic Insights![/green]"
                    )
                    sys.exit(0)
            elif choice == "1":
                download_data()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "2":
                explore_data()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "3":
                preprocess_data()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "4":
                train_model()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "5":
                evaluate_model()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "6":
                generate_insights()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "7":
                open_jupyter()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "8":
                start_api()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")
            elif choice == "9":
                test_suite()
                Prompt.ask("\n[dim]Pressione Enter para continuar...[/dim]")

        except KeyboardInterrupt:
            console.print("\n[green]👋 Obrigado por usar o Titanic Insights![/green]")
            sys.exit(0)


@cli.command()
@click.option("--interactive", "-i", is_flag=True, help="Modo interativo")
def download(interactive):

    download_data()


def download_data():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("📥 Iniciando download dos dados...", total=None)

        try:
            from src.data.download import main

            main()
            progress.update(task, description="✅ Download concluído com sucesso!")
            console.print("\n[green]✅ Download concluído com sucesso![/green]")
        except ImportError:
            progress.update(
                task, description="❌ Erro: Módulo de download não encontrado"
            )
            console.print("\n[red]❌ Erro: Módulo de download não encontrado[/red]")
        except Exception as e:
            progress.update(task, description=f"❌ Erro durante o download")
            console.print(f"\n[red]❌ Erro durante o download: {e}[/red]")


@cli.command()
@click.option("--interactive", "-i", is_flag=True, help="Modo interativo")
def explore(interactive):
    explore_data()


def explore_data():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("🔍 Abrindo notebook de exploração...", total=None)

        notebook_path = Path("notebooks/00_exploracao.ipynb")
        if notebook_path.exists():
            try:
                os.system(f"jupyter lab {notebook_path}")
                progress.update(task, description="✅ Notebook aberto com sucesso!")
                console.print("\n[green]✅ Notebook aberto com sucesso![/green]")
            except Exception as e:
                progress.update(task, description="❌ Erro ao abrir notebook")
                console.print(f"\n[red]❌ Erro ao abrir notebook: {e}[/red]")
        else:
            progress.update(task, description="❌ Notebook não encontrado")
            console.print("\n[red]❌ Notebook de exploração não encontrado[/red]")


@cli.command()
def preprocess():
    preprocess_data()


def preprocess_data():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(
            "🧹 Iniciando pré-processamento dos dados...", total=None
        )

        try:
            from src.processing.preprocessing import main as preprocess_main

            preprocess_main()
            progress.update(task, description="✅ Dados pré-processados com sucesso!")
            console.print("\n[green]✅ Dados pré-processados com sucesso![/green]")
            console.print("[dim]Arquivos salvos em data/processed/[/dim]")
        except ImportError:
            progress.update(
                task, description="❌ Erro: Módulo de pré-processamento não encontrado"
            )
            console.print(
                "\n[red]❌ Erro: Módulo de pré-processamento não encontrado[/red]"
            )
        except FileNotFoundError:
            progress.update(
                task, description="❌ Erro: Arquivos de dados brutos não encontrados"
            )
            console.print(
                "\n[red]❌ Erro: Arquivos de dados brutos não encontrados em data/raw.[/red]"
            )
            console.print("[dim]Execute o download dos dados primeiro (opção 1).[/dim]")
        except Exception as e:
            progress.update(task, description=f"❌ Erro durante o pré-processamento")
            console.print(f"\n[red]❌ Erro durante o pré-processamento: {e}[/red]")


@cli.command()
def train():
    train_model()


def train_model():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("🤖 Iniciando treinamento do modelo...", total=None)
        try:
            from src.model.train import train_and_evaluate

            train_and_evaluate()
            progress.update(task, description="✅ Modelo treinado com sucesso!")
            console.print("\n[green]✅ Modelo treinado e salvo com sucesso![/green]")
        except ImportError:
            progress.update(
                task, description="❌ Erro: Módulo de treinamento não encontrado"
            )
            console.print("\n[red]❌ Erro: Módulo de treinamento não encontrado[/red]")
        except FileNotFoundError:
            progress.update(
                task,
                description="❌ Erro: Arquivo de dados pré-processados não encontrado",
            )
            console.print(
                "\n[red]❌ Erro: Arquivo de dados não encontrado em data/processed.[/red]"
            )
            console.print(
                "[dim]Execute o pré-processamento dos dados primeiro (opção 3).[/dim]"
            )
        except Exception as e:
            progress.update(task, description=f"❌ Erro durante o treinamento")
            console.print(f"\n[red]❌ Erro durante o treinamento: {e}[/red]")


@cli.command()
def evaluate():
    evaluate_model()


def evaluate_model():
    model_path = "models/logreg_titanic.joblib"
    if not Path(model_path).exists():
        console.print(f"\n[red]❌ Modelo não encontrado em {model_path}[/red]")
        console.print("[dim]Treine um modelo primeiro (opção 4).[/dim]")
        return

    from joblib import load

    model = load(model_path)

    console.print(f"\n[green]✅ Modelo carregado de {model_path}[/green]")

    panel = Panel(
        Text(str(model), justify="left"),
        title="🔎 Detalhes do Modelo",
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2),
    )
    console.print(panel)


@cli.command()
def insights():
    generate_insights()


def generate_insights():
    console.print("\n[yellow]⚠️  Funcionalidade em desenvolvimento[/yellow]")
    console.print("Esta funcionalidade será implementada em breve!")


@cli.command()
@click.option("--interactive", "-i", is_flag=True, help="Modo interativo")
def jupyter(interactive):
    open_jupyter()


def open_jupyter():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("📝 Abrindo Jupyter Lab...", total=None)

        try:
            os.system("jupyter lab")
            progress.update(task, description="✅ Jupyter Lab aberto!")
            console.print("\n[green]✅ Jupyter Lab aberto![/green]")
        except Exception as e:
            progress.update(task, description="❌ Erro ao abrir Jupyter Lab")
            console.print(f"\n[red]❌ Erro ao abrir Jupyter Lab: {e}[/red]")


@cli.command()
def api():
    start_api()


def start_api():
    console.print("\n[bold green]🚀 Iniciando a API de predição...[/bold green]")
    console.print(
        "Acesse a documentação interativa em: [cyan]http://127.0.0.1:8000/docs[/cyan]"
    )
    try:
        import uvicorn

        uvicorn.run("src.api.api:app", host="127.0.0.1", port=8000, reload=True)
    except ImportError:
        console.print("\n[red]❌ Erro: Uvicorn não está instalado.[/red]")
        console.print(
            "[dim]Por favor, execute 'poetry install' ou 'pip install uvicorn'.[/dim]"
        )
    except Exception as e:
        console.print(f"\n[red]❌ Erro ao iniciar a API: {e}[/red]")


@cli.command()
def version():
    console.print(
        f"[bold blue]Titanic Insights[/bold blue] versão [green]0.1.0[/green]"
    )


@cli.command()
def info():
    info_table = Table(title="ℹ️  Informações do Projeto", box=box.ROUNDED)
    info_table.add_column("Propriedade", style="cyan")
    info_table.add_column("Valor", style="white")

    info_table.add_row("Nome", "Titanic Insights")
    info_table.add_row("Versão", "0.1.0")
    info_table.add_row("Autor", "Lucas")
    info_table.add_row(
        "Descrição", "Pipeline de ML para análise de sobrevivência no Titanic"
    )
    info_table.add_row("Python", "^3.11")

    console.print(info_table)


@cli.command("test-suite")
def test_suite_command():
    """🧪 Teste Visual da API/Frontend com Streamlit"""
    test_suite()


def test_suite():
    console.print("\n[bold green]🧪 Iniciando suíte de testes visuais...[/bold green]")
    console.print("Iniciando a API de predição em segundo plano...")
    api_command = [
        "uvicorn",
        "src.api.api:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
    ]
    api_process = None

    try:
        api_process = subprocess.Popen(
            api_command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE
        )
        console.print("Aguardando a API ficar online (5s)...")
        time.sleep(5)
        if api_process.poll() is not None:
            stderr_output = api_process.stderr.read().decode("utf-8")
            console.print("[red]❌ Falha ao iniciar a API em segundo plano.[/red]")
            console.print(f"[dim]Erro: {stderr_output}[/dim]")
            return

        console.print("API online! Iniciando a aplicação Streamlit...")
        console.print("A aplicação Streamlit será aberta no seu navegador.")
        console.print(
            "[bold yellow]Pressione Ctrl+C no terminal para encerrar tudo.[/bold yellow]"
        )

        test_app_path = "src/streamlit/app.py"
        if not Path(test_app_path).exists():
            console.print(
                f"\n[red]❌ Erro: Arquivo da aplicação de teste não encontrado em {test_app_path}[/red]"
            )
            return

        streamlit_command = ["streamlit", "run", test_app_path]
        subprocess.run(streamlit_command)

    except FileNotFoundError:
        console.print("\n[red]❌ Erro: `uvicorn` ou `streamlit` não encontrado.[/red]")
        console.print(
            "[dim]Certifique-se de que todas as dependências estão instaladas com 'poetry install'.[/dim]"
        )
    except Exception as e:
        console.print(f"\n[red]❌ Erro inesperado: {e}[/red]")
    finally:
        if api_process:
            console.print(
                "\n[bold yellow]Encerrando a API em segundo plano...[/bold yellow]"
            )
            api_process.terminate()
            api_process.wait()
            console.print("API encerrada.")


if __name__ == "__main__":
    cli()
