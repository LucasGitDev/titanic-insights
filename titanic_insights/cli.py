#!/usr/bin/env python3
"""
CLI profissional para o projeto Titanic Insights
Usando Click e Rich para uma interface moderna
"""

import os
import sys
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

# Configuração do console Rich
console = Console()


def print_banner():
    """Imprime o banner do projeto"""
    banner_text = Text()
    banner_text.append("🚢 ", style="bold blue")
    banner_text.append("TITANIC INSIGHTS", style="bold white on blue")
    banner_text.append(" 🚢", style="bold blue")
    banner_text.append("\nAnálise de Sobrevivência no Titanic", style="italic cyan")

    panel = Panel(banner_text, border_style="blue", box=box.DOUBLE, padding=(1, 2))
    console.print(panel)


def print_menu():
    """Imprime o menu principal usando Rich"""
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
        ("3", "🧹 Pré-processar dados", "🔄 Em desenvolvimento"),
        ("4", "🤖 Treinar modelo", "🔄 Em desenvolvimento"),
        ("5", "📊 Avaliar modelo", "🔄 Em desenvolvimento"),
        ("6", "📈 Gerar insights", "🔄 Em desenvolvimento"),
        ("7", "📝 Abrir Jupyter Lab", "✅ Disponível"),
        ("0", "❌ Sair", "✅ Disponível"),
    ]

    for option, description, status in menu_items:
        table.add_row(option, description, status)

    console.print(table)


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """🚢 Titanic Insights - Análise de Sobrevivência no Titanic"""
    if ctx.invoked_subcommand is None:
        # Modo interativo
        interactive_mode()


def interactive_mode():
    """Modo interativo do CLI"""
    while True:
        console.clear()
        print_banner()
        print_menu()

        try:
            choice = Prompt.ask(
                "\n[bold cyan]Escolha uma opção[/bold cyan]",
                choices=["0", "1", "2", "3", "4", "5", "6", "7"],
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

        except KeyboardInterrupt:
            console.print("\n[green]👋 Obrigado por usar o Titanic Insights![/green]")
            sys.exit(0)


@cli.command()
@click.option("--interactive", "-i", is_flag=True, help="Modo interativo")
def download(interactive):
    """📥 Download dos dados do Titanic"""
    download_data()


def download_data():
    """Executa o download dos dados"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("📥 Iniciando download dos dados...", total=None)

        try:
            # Importa e executa o módulo de download
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
    """🔍 Explorar dados do Titanic"""
    explore_data()


def explore_data():
    """Abre o notebook de exploração"""
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
    """🧹 Pré-processar dados"""
    preprocess_data()


def preprocess_data():
    """Executa o pré-processamento dos dados"""
    console.print("\n[yellow]⚠️  Funcionalidade em desenvolvimento[/yellow]")
    console.print("Esta funcionalidade será implementada em breve!")


@cli.command()
def train():
    """🤖 Treinar modelo de ML"""
    train_model()


def train_model():
    """Executa o treinamento do modelo"""
    console.print("\n[yellow]⚠️  Funcionalidade em desenvolvimento[/yellow]")
    console.print("Esta funcionalidade será implementada em breve!")


@cli.command()
def evaluate():
    """📊 Avaliar modelo de ML"""
    evaluate_model()


def evaluate_model():
    """Executa a avaliação do modelo"""
    console.print("\n[yellow]⚠️  Funcionalidade em desenvolvimento[/yellow]")
    console.print("Esta funcionalidade será implementada em breve!")


@cli.command()
def insights():
    """📈 Gerar insights e relatórios"""
    generate_insights()


def generate_insights():
    """Gera insights e relatórios"""
    console.print("\n[yellow]⚠️  Funcionalidade em desenvolvimento[/yellow]")
    console.print("Esta funcionalidade será implementada em breve!")


@cli.command()
@click.option("--interactive", "-i", is_flag=True, help="Modo interativo")
def jupyter(interactive):
    """📝 Abrir Jupyter Lab"""
    open_jupyter()


def open_jupyter():
    """Abre o Jupyter Lab"""
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
def version():
    """📋 Mostrar versão do projeto"""
    console.print(
        f"[bold blue]Titanic Insights[/bold blue] versão [green]0.1.0[/green]"
    )


@cli.command()
def info():
    """ℹ️  Informações do projeto"""
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


if __name__ == "__main__":
    cli()
