#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer",
#     "rich",
#     "platformdirs",
#     "readchar",
#     "httpx",
# ]
# ///
"""
Specify CLI - Specifyプロジェクトのセットアップツール

【使い方】
    uvx specify-cli.py init <プロジェクト名>
    uvx specify-cli.py init --here

またはグローバルインストール:
    uv tool install --from specify-cli.py specify-cli
    specify init <プロジェクト名>
    specify init --here
"""

import os
import subprocess
import sys
import zipfile
import tempfile
import shutil
import json
from pathlib import Path
from typing import Optional

import typer
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.live import Live
from rich.align import Align
from rich.table import Table
from rich.tree import Tree
from typer.core import TyperGroup

# For cross-platform keyboard input
import readchar

# Constants
AI_CHOICES = {
    "copilot": "GitHub Copilot",
    "claude": "Claude Code",
    "gemini": "Gemini CLI"
}

# ASCII Art Banner
BANNER = """
███████╗██████╗ ███████╗ ██████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝█████╗  ██║     ██║█████╗   ╚████╔╝
╚════██║██╔═══╝ ██╔══╝  ██║     ██║██╔══╝    ╚██╔╝
███████║██║     ███████╗╚██████╗██║██║        ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝╚═╝        ╚═╝
"""

TAGLINE = "Spec-Driven Development Toolkit"
class StepTracker:
    """
    ステップの進捗を階層的に管理・表示するクラス（絵文字なし、Claude Code風ツリー出力）。
    コールバックによるライブ自動リフレッシュ対応。
    """
    def __init__(self, title: str):
        self.title = title
        self.steps = []  # list of dicts: {key, label, status, detail}
        self.status_order = {"pending": 0, "running": 1, "done": 2, "error": 3, "skipped": 4}
        self._refresh_cb = None  # callable to trigger UI refresh

    def attach_refresh(self, cb):
        self._refresh_cb = cb  # UIリフレッシュ用コールバックを登録

    def add(self, key: str, label: str):
        if key not in [s["key"] for s in self.steps]:
            self.steps.append({"key": key, "label": label, "status": "pending", "detail": ""})
            self._maybe_refresh()  # ステップ追加時にリフレッシュ

    def start(self, key: str, detail: str = ""):
        self._update(key, status="running", detail=detail)

    def complete(self, key: str, detail: str = ""):
        self._update(key, status="done", detail=detail)

    def error(self, key: str, detail: str = ""):
        self._update(key, status="error", detail=detail)

    def skip(self, key: str, detail: str = ""):
        self._update(key, status="skipped", detail=detail)

    def _update(self, key: str, status: str, detail: str):
        for s in self.steps:
            if s["key"] == key:
                s["status"] = status
                if detail:
                    s["detail"] = detail
                self._maybe_refresh()
                return
        # If not present, add it
        self.steps.append({"key": key, "label": key, "status": status, "detail": detail})
        self._maybe_refresh()

    def _maybe_refresh(self):
        if self._refresh_cb:
            try:
                self._refresh_cb()
            except Exception:
                pass


    def render(self):
        tree = Tree(f"[bold cyan]{self.title}[/bold cyan]", guide_style="grey50")
        for step in self.steps:
            label = step["label"]
            detail_text = step["detail"].strip() if step["detail"] else ""

            # ステータスごとに記号を色分け
            status = step["status"]
            if status == "done":
                symbol = "[green]●[/green]"
            elif status == "pending":
                symbol = "[green dim]○[/green dim]"
            elif status == "running":
                symbol = "[cyan]○[/cyan]"
            elif status == "error":
                symbol = "[red]●[/red]"
            elif status == "skipped":
                symbol = "[yellow]○[/yellow]"
            else:
                symbol = " "

            if status == "pending":
                # pendingは全体を薄いグレーで表示
                if detail_text:
                    line = f"{symbol} [bright_black]{label} ({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [bright_black]{label}[/bright_black]"
            else:
                # 完了・実行中などはラベル白、詳細は薄グレー
                if detail_text:
                    line = f"{symbol} [white]{label}[/white] [bright_black]({detail_text})[/bright_black]"
                else:
                    line = f"{symbol} [white]{label}[/white]"

            tree.add(line)
        return tree



MINI_BANNER = """
╔═╗╔═╗╔═╗╔═╗╦╔═╗╦ ╦
╚═╗╠═╝║╣ ║  ║╠╣ ╚╦╝
╚═╝╩  ╚═╝╚═╝╩╚   ╩
"""

def get_key():
    """
    readcharを使ってクロスプラットフォームで1キー入力を取得
    """
    key = readchar.readkey()

    # Arrow keys
    if key == readchar.key.UP:
        return 'up'
    if key == readchar.key.DOWN:
        return 'down'

    # Enter/Return
    if key == readchar.key.ENTER:
        return 'enter'

    # Escape
    if key == readchar.key.ESC:
        return 'escape'

    # Ctrl+C
    if key == readchar.key.CTRL_C:
        raise KeyboardInterrupt

    return key



def select_with_arrows(options: dict, prompt_text: str = "オプションを選択", default_key: str = None) -> str:
    """
    矢印キーで選択肢を選ぶインタラクティブUI（Rich Live使用）

    Args:
        options: 選択肢（key:値）
        prompt_text: 上部に表示するテキスト
        default_key: デフォルト選択キー

    Returns:
        選択されたkey
    """
    option_keys = list(options.keys())
    if default_key and default_key in option_keys:
        selected_index = option_keys.index(default_key)
    else:
        selected_index = 0

    selected_key = None

    def create_selection_panel():
        """現在の選択肢をハイライトしたパネルを生成"""
        table = Table.grid(padding=(0, 2))
        table.add_column(style="bright_cyan", justify="left", width=3)
        table.add_column(style="white", justify="left")

        for i, key in enumerate(option_keys):
            if i == selected_index:
                table.add_row("▶", f"[bright_cyan]{key}: {options[key]}[/bright_cyan]")
            else:
                table.add_row(" ", f"[white]{key}: {options[key]}[/white]")

        table.add_row("", "")
        table.add_row("", "[dim]↑/↓で移動、Enterで決定、Escでキャンセル[/dim]")

        return Panel(
            table,
            title=f"[bold]{prompt_text}[/bold]",
            border_style="cyan",
            padding=(1, 2)
        )

    console.print()

    def run_selection_loop():
        nonlocal selected_key, selected_index
        with Live(create_selection_panel(), console=console, transient=True, auto_refresh=False) as live:
            while True:
                try:
                    key = get_key()
                    if key == 'up':
                        selected_index = (selected_index - 1) % len(option_keys)
                    elif key == 'down':
                        selected_index = (selected_index + 1) % len(option_keys)
                    elif key == 'enter':
                        selected_key = option_keys[selected_index]
                        break
                    elif key == 'escape':
                        console.print("\n[yellow]選択をキャンセルしました[/yellow]")
                        raise typer.Exit(1)

                    live.update(create_selection_panel(), refresh=True)

                except KeyboardInterrupt:
                    console.print("\n[yellow]選択をキャンセルしました[/yellow]")
                    raise typer.Exit(1)

    run_selection_loop()


    if selected_key is None:
        console.print("\n[red]選択に失敗しました[/red]")
        raise typer.Exit(1)

    # Suppress explicit selection print; tracker / later logic will report consolidated status
    return selected_key



console = Console()



class BannerGroup(TyperGroup):
    """
    ヘルプ表示前にバナーを表示するカスタムグループ
    """

    def format_help(self, ctx, formatter):
        # Show banner before help
        show_banner()
        super().format_help(ctx, formatter)


app = typer.Typer(
    name="specify",
    help="Specify仕様駆動開発プロジェクトのセットアップツール",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)


def show_banner():
    """
    ASCIIアートバナーを表示
    """
    banner_lines = BANNER.strip().split('\n')
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]

    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)

    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()


@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    # Show banner only when no subcommand and no help flag
    # (help is handled by BannerGroup)
    if ctx.invoked_subcommand is None and "--help" not in sys.argv and "-h" not in sys.argv:
        show_banner()
        console.print(Align.center("[dim]'specify --help' で使い方を表示[/dim]"))
        console.print()


def run_command(cmd: list[str], check_return: bool = True, capture: bool = False, shell: bool = False) -> Optional[str]:
    """
    シェルコマンドを実行し、必要に応じて出力を取得
    """
    try:
        if capture:
            result = subprocess.run(cmd, check=check_return, capture_output=True, text=True, shell=shell)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=check_return, shell=shell)
            return None
    except subprocess.CalledProcessError as e:
        if check_return:
            console.print(f"[red]Error running command:[/red] {' '.join(cmd)}")
            console.print(f"[red]Exit code:[/red] {e.returncode}")
            if hasattr(e, 'stderr') and e.stderr:
                console.print(f"[red]Error output:[/red] {e.stderr}")
            raise
        return None


def check_tool(tool: str, install_hint: str) -> bool:
    """
    ツールがインストールされているか確認
    """
    if shutil.which(tool):
        return True
    else:
        console.print(f"[yellow]⚠️  {tool} not found[/yellow]")
        console.print(f"   Install with: [cyan]{install_hint}[/cyan]")
        return False


def is_git_repo(path: Path = None) -> bool:
    """
    指定パスがgitリポジトリ内か判定
    """
    if path is None:
        path = Path.cwd()

    if not path.is_dir():
        return False

    try:
        # Use git command to check if inside a work tree
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_git_repo(project_path: Path, quiet: bool = False) -> bool:
    """
    指定パスでgitリポジトリを初期化
    quiet=Trueで出力抑制（trackerで管理）
    """
    try:
        original_cwd = Path.cwd()
        os.chdir(project_path)
        if not quiet:
            console.print("[cyan]Initializing git repository...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit from Specify template"], check=True, capture_output=True)
        if not quiet:
            console.print("[green]✓[/green] Git repository initialized")
        return True

    except subprocess.CalledProcessError as e:
        if not quiet:
            console.print(f"[red]Error initializing git repository:[/red] {e}")
        return False
    finally:
        os.chdir(original_cwd)


def download_template_from_github(ai_assistant: str, download_dir: Path, *, verbose: bool = True, show_progress: bool = True):
    """
    GitHubから最新テンプレートリリースをダウンロード
    戻り値: (zip_path, metadata_dict)
    """
    repo_owner = "github"
    repo_name = "spec-kit"

    if verbose:
        console.print("[cyan]Fetching latest release information...[/cyan]")
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    try:
        response = httpx.get(api_url, timeout=30, follow_redirects=True)
        response.raise_for_status()
        release_data = response.json()
    except httpx.RequestError as e:
        if verbose:
            console.print(f"[red]Error fetching release information:[/red] {e}")
        raise typer.Exit(1)

    # Find the template asset for the specified AI assistant
    pattern = f"spec-kit-template-{ai_assistant}"
    matching_assets = [
        asset for asset in release_data.get("assets", [])
        if pattern in asset["name"] and asset["name"].endswith(".zip")
    ]

    if not matching_assets:
        if verbose:
            console.print(f"[red]Error:[/red] No template found for AI assistant '{ai_assistant}'")
            console.print(f"[yellow]Available assets:[/yellow]")
            for asset in release_data.get("assets", []):
                console.print(f"  - {asset['name']}")
        raise typer.Exit(1)

    # Use the first matching asset
    asset = matching_assets[0]
    download_url = asset["browser_download_url"]
    filename = asset["name"]
    file_size = asset["size"]

    if verbose:
        console.print(f"[cyan]Found template:[/cyan] {filename}")
        console.print(f"[cyan]Size:[/cyan] {file_size:,} bytes")
        console.print(f"[cyan]Release:[/cyan] {release_data['tag_name']}")

    # Download the file
    zip_path = download_dir / filename
    if verbose:
        console.print(f"[cyan]Downloading template...[/cyan]")

    try:
        with httpx.stream("GET", download_url, timeout=30, follow_redirects=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get('content-length', 0))

            with open(zip_path, 'wb') as f:
                if total_size == 0:
                    # No content-length header, download without progress
                    for chunk in response.iter_bytes(chunk_size=8192):
                        f.write(chunk)
                else:
                    if show_progress:
                        # Show progress bar
                        with Progress(
                            SpinnerColumn(),
                            TextColumn("[progress.description]{task.description}"),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                            console=console,
                        ) as progress:
                            task = progress.add_task("Downloading...", total=total_size)
                            downloaded = 0
                            for chunk in response.iter_bytes(chunk_size=8192):
                                f.write(chunk)
                                downloaded += len(chunk)
                                progress.update(task, completed=downloaded)
                    else:
                        # Silent download loop
                        for chunk in response.iter_bytes(chunk_size=8192):
                            f.write(chunk)

    except httpx.RequestError as e:
        if verbose:
            console.print(f"[red]Error downloading template:[/red] {e}")
        if zip_path.exists():
            zip_path.unlink()
        raise typer.Exit(1)
    if verbose:
        console.print(f"Downloaded: {filename}")
    metadata = {
        "filename": filename,
        "size": file_size,
        "release": release_data["tag_name"],
        "asset_url": download_url
    }
    return zip_path, metadata


def download_and_extract_template(project_path: Path, ai_assistant: str, is_current_dir: bool = False, *, verbose: bool = True, tracker: StepTracker | None = None) -> Path:
    """
    最新リリースをダウンロードし展開して新規プロジェクト作成
    tracker指定時は進捗を記録
    戻り値: project_path
    """
    current_dir = Path.cwd()

    # Step: fetch + download combined
    if tracker:
        tracker.start("fetch", "contacting GitHub API")
    try:
        zip_path, meta = download_template_from_github(
            ai_assistant,
            current_dir,
            verbose=verbose and tracker is None,
            show_progress=(tracker is None)
        )
        if tracker:
            tracker.complete("fetch", f"release {meta['release']} ({meta['size']:,} bytes)")
            tracker.add("download", "Download template")
            tracker.complete("download", meta['filename'])  # already downloaded inside helper
    except Exception as e:
        if tracker:
            tracker.error("fetch", str(e))
        else:
            if verbose:
                console.print(f"[red]Error downloading template:[/red] {e}")
        raise

    if tracker:
        tracker.add("extract", "Extract template")
        tracker.start("extract")
    elif verbose:
        console.print("Extracting template...")

    try:
        # Create project directory only if not using current directory
        if not is_current_dir:
            project_path.mkdir(parents=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files in the ZIP for debugging
            zip_contents = zip_ref.namelist()
            if tracker:
                tracker.start("zip-list")
                tracker.complete("zip-list", f"{len(zip_contents)} entries")
            elif verbose:
                console.print(f"[cyan]ZIP contains {len(zip_contents)} items[/cyan]")

            # For current directory, extract to a temp location first
            if is_current_dir:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    zip_ref.extractall(temp_path)

                    # Check what was extracted
                    extracted_items = list(temp_path.iterdir())
                    if tracker:
                        tracker.start("extracted-summary")
                        tracker.complete("extracted-summary", f"temp {len(extracted_items)} items")
                    elif verbose:
                        console.print(f"[cyan]Extracted {len(extracted_items)} items to temp location[/cyan]")

                    # Handle GitHub-style ZIP with a single root directory
                    source_dir = temp_path
                    if len(extracted_items) == 1 and extracted_items[0].is_dir():
                        source_dir = extracted_items[0]
                        if tracker:
                            tracker.add("flatten", "Flatten nested directory")
                            tracker.complete("flatten")
                        elif verbose:
                            console.print(f"[cyan]Found nested directory structure[/cyan]")

                    # Copy contents to current directory
                    for item in source_dir.iterdir():
                        dest_path = project_path / item.name
                        if item.is_dir():
                            if dest_path.exists():
                                if verbose and not tracker:
                                    console.print(f"[yellow]Merging directory:[/yellow] {item.name}")
                                # Recursively copy directory contents
                                for sub_item in item.rglob('*'):
                                    if sub_item.is_file():
                                        rel_path = sub_item.relative_to(item)
                                        dest_file = dest_path / rel_path
                                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                                        shutil.copy2(sub_item, dest_file)
                            else:
                                shutil.copytree(item, dest_path)
                        else:
                            if dest_path.exists() and verbose and not tracker:
                                console.print(f"[yellow]Overwriting file:[/yellow] {item.name}")
                            shutil.copy2(item, dest_path)
                    if verbose and not tracker:
                        console.print(f"[cyan]Template files merged into current directory[/cyan]")
            else:
                # Extract directly to project directory (original behavior)
                zip_ref.extractall(project_path)

                # Check what was extracted
                extracted_items = list(project_path.iterdir())
                if tracker:
                    tracker.start("extracted-summary")
                    tracker.complete("extracted-summary", f"{len(extracted_items)} top-level items")
                elif verbose:
                    console.print(f"[cyan]Extracted {len(extracted_items)} items to {project_path}:[/cyan]")
                    for item in extracted_items:
                        console.print(f"  - {item.name} ({'dir' if item.is_dir() else 'file'})")

                # Handle GitHub-style ZIP with a single root directory
                if len(extracted_items) == 1 and extracted_items[0].is_dir():
                    # Move contents up one level
                    nested_dir = extracted_items[0]
                    temp_move_dir = project_path.parent / f"{project_path.name}_temp"
                    # Move the nested directory contents to temp location
                    shutil.move(str(nested_dir), str(temp_move_dir))
                    # Remove the now-empty project directory
                    project_path.rmdir()
                    # Rename temp directory to project directory
                    shutil.move(str(temp_move_dir), str(project_path))
                    if tracker:
                        tracker.add("flatten", "Flatten nested directory")
                        tracker.complete("flatten")
                    elif verbose:
                        console.print(f"[cyan]Flattened nested directory structure[/cyan]")

    except Exception as e:
        if tracker:
            tracker.error("extract", str(e))
        else:
            if verbose:
                console.print(f"[red]Error extracting template:[/red] {e}")
        # Clean up project directory if created and not current directory
        if not is_current_dir and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)
    else:
        if tracker:
            tracker.complete("extract")
    finally:
        if tracker:
            tracker.add("cleanup", "Remove temporary archive")
        # Clean up downloaded ZIP file
        if zip_path.exists():
            zip_path.unlink()
            if tracker:
                tracker.complete("cleanup")
            elif verbose:
                console.print(f"Cleaned up: {zip_path.name}")

    return project_path


@app.command()
def init(
    project_name: str = typer.Argument(None, help="Name for your new project directory (optional if using --here)"),
    ai_assistant: str = typer.Option(None, "--ai", help="AI assistant to use: claude, gemini, or copilot"),
    ignore_agent_tools: bool = typer.Option(False, "--ignore-agent-tools", help="Skip checks for AI agent tools like Claude Code"),
    no_git: bool = typer.Option(False, "--no-git", help="Skip git repository initialization"),
    here: bool = typer.Option(False, "--here", help="Initialize project in the current directory instead of creating a new one"),
):
    """
    最新テンプレートから新しいSpecifyプロジェクトを初期化します。

    このコマンドは以下を行います:
    1. 必要なツールのインストール確認（gitは任意）
    2. AIアシスタント（Claude Code, Gemini CLI, GitHub Copilot）を選択
    3. GitHubから該当テンプレートをダウンロード
    4. 新規ディレクトリまたはカレントディレクトリに展開
    5. gitリポジトリ初期化（--no-git指定や既存リポジトリ時はスキップ）
    6. 必要に応じAIアシスタントコマンドのセットアップ

    【例】
        specify init my-project
        specify init my-project --ai claude
        specify init my-project --ai gemini
        specify init my-project --ai copilot --no-git
        specify init --ignore-agent-tools my-project
        specify init --here --ai claude
        specify init --here
    """

    # まずバナー表示
    show_banner()


    # 引数バリデーション
    if here and project_name:
        console.print("[red]エラー:[/red] --hereとプロジェクト名は同時指定できません")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print("[red]エラー:[/red] プロジェクト名指定か--hereフラグが必要です")
        raise typer.Exit(1)


    # プロジェクトディレクトリ決定
    if here:
        project_name = Path.cwd().name
        project_path = Path.cwd()

        # カレントディレクトリに既存ファイルがあるか確認
        existing_items = list(project_path.iterdir())
        if existing_items:
            console.print(f"[yellow]警告:[/yellow] カレントディレクトリが空ではありません（{len(existing_items)}件）")
            console.print("[yellow]テンプレートファイルは既存内容とマージされ、上書きされる場合があります[/yellow]")

            # 続行確認
            response = typer.confirm("続行しますか？")
            if not response:
                console.print("[yellow]操作をキャンセルしました[/yellow]")
                raise typer.Exit(0)
    else:
        project_path = Path(project_name).resolve()
        # 既存ディレクトリがある場合はエラー
        if project_path.exists():
            console.print(f"[red]エラー:[/red] ディレクトリ '{project_name}' は既に存在します")
            raise typer.Exit(1)

    console.print(Panel.fit(
        "[bold cyan]Specifyプロジェクトセットアップ[/bold cyan]\n"
        f"{'カレントディレクトリで初期化:' if here else '新規プロジェクト作成:'} [green]{project_path.name}[/green]"
        + (f"\n[dim]パス: {project_path}[/dim]" if here else ""),
        border_style="cyan"
    ))


    # gitが必要な場合のみチェック
    git_available = True
    if not no_git:
        git_available = check_tool("git", "https://git-scm.com/downloads")
        if not git_available:
            console.print("[yellow]gitが見つかりません - リポジトリ初期化をスキップします[/yellow]")


    # AIアシスタント選択
    if ai_assistant:
        if ai_assistant not in AI_CHOICES:
            console.print(f"[red]エラー:[/red] 無効なAIアシスタント '{ai_assistant}'。選択肢: {', '.join(AI_CHOICES.keys())}")
            raise typer.Exit(1)
        selected_ai = ai_assistant
    else:
        # 矢印キー選択UI
        selected_ai = select_with_arrows(
            AI_CHOICES,
            "AIアシスタントを選択:",
            "copilot"
        )


    # AIエージェントツールの有無を確認（--ignore-agent-toolsでスキップ可）
    if not ignore_agent_tools:
        agent_tool_missing = False
        if selected_ai == "claude":
            if not check_tool("claude", "https://docs.anthropic.com/en/docs/claude-code/setup からインストール"):
                console.print("[red]エラー:[/red] Claude CLIが必要です")
                agent_tool_missing = True
        elif selected_ai == "gemini":
            if not check_tool("gemini", "https://github.com/google-gemini/gemini-cli からインストール"):
                console.print("[red]エラー:[/red] Gemini CLIが必要です")
                agent_tool_missing = True
        # Copilotは通常IDEに同梱のためチェック不要

        if agent_tool_missing:
            console.print("\n[red]必要なAIツールが見つかりません！[/red]")
            console.print("[yellow]ヒント:[/yellow] --ignore-agent-tools でこのチェックをスキップできます")
            raise typer.Exit(1)

    # Download and set up project
    # New tree-based progress (no emojis); include earlier substeps
    tracker = StepTracker("Initialize Specify Project")
    # Flag to allow suppressing legacy headings
    sys._specify_tracker_active = True
    # Pre steps recorded as completed before live rendering
    tracker.add("precheck", "Check required tools")
    tracker.complete("precheck", "ok")
    tracker.add("ai-select", "AIアシスタント選択")
    tracker.complete("ai-select", f"{selected_ai}")
    for key, label in [
        ("fetch", "リリース情報取得"),
        ("download", "テンプレートDL"),
        ("extract", "テンプレート展開"),
        ("zip-list", "アーカイブ内容"),
        ("extracted-summary", "展開サマリ"),
        ("cleanup", "一時ファイル削除"),
        ("git", "git初期化"),
        ("final", "完了")
    ]:
        tracker.add(key, label)


    # Liveツリーはtransientで最後に静的ツリーへ置換
    with Live(tracker.render(), console=console, refresh_per_second=8, transient=True) as live:
        tracker.attach_refresh(lambda: live.update(tracker.render()))
        try:
            download_and_extract_template(project_path, selected_ai, here, verbose=False, tracker=tracker)

            # gitステップ
            if not no_git:
                tracker.start("git")
                if is_git_repo(project_path):
                    tracker.complete("git", "既存リポジトリ検出")
                elif git_available:
                    if init_git_repo(project_path, quiet=True):
                        tracker.complete("git", "初期化完了")
                    else:
                        tracker.error("git", "初期化失敗")
                else:
                    tracker.skip("git", "git未インストール")
            else:
                tracker.skip("git", "--no-git指定")

            tracker.complete("final", "プロジェクト準備完了")
        except Exception as e:
            tracker.error("final", str(e))
            if not here and project_path.exists():
                shutil.rmtree(project_path)
            raise typer.Exit(1)
        finally:
            pass

    # 静的ツリー表示
    console.print(tracker.render())
    console.print("\n[bold green]プロジェクトの準備ができました[/bold green]")

    # 次のステップ案内
    steps_lines = []
    if not here:
        steps_lines.append(f"1. [bold green]cd {project_name}[/bold green]")
        step_num = 2
    else:
        steps_lines.append("1. 既にプロジェクトディレクトリ内です！")
        step_num = 2

    if selected_ai == "claude":
        steps_lines.append(f"{step_num}. Open in Visual Studio Code and start using / commands with Claude Code")
        steps_lines.append("   - Type / in any file to see available commands")
        steps_lines.append("   - Use /specify to create specifications")
        steps_lines.append("   - Use /plan to create implementation plans")
        steps_lines.append("   - Use /tasks to generate tasks")
    elif selected_ai == "gemini":
        steps_lines.append(f"{step_num}. Gemini CLIで / コマンドを使う")
        steps_lines.append("   - gemini /specify で仕様作成")
        steps_lines.append("   - gemini /plan で計画作成")
        steps_lines.append("   - 詳細は GEMINI.md を参照")
    elif selected_ai == "copilot":
        steps_lines.append(f"{step_num}. VS Codeで [bold cyan]/specify[/], [bold cyan]/plan[/], [bold cyan]/tasks[/] コマンドをGitHub Copilotで使う")

    step_num += 1
    steps_lines.append(f"{step_num}. [bold magenta]CONSTITUTION.md[/bold magenta] にプロジェクトの原則を記載")

    steps_panel = Panel("\n".join(steps_lines), title="次のステップ", border_style="cyan", padding=(1,2))
    console.print()
    console.print(steps_panel)

    # Removed farewell line per user request


@app.command()
def check():
    """
    必要なツールが全て揃っているかチェック
    """
    show_banner()
    console.print("[bold]Specify要件をチェック中...[/bold]\n")

    # インターネット接続確認（GitHub API到達）
    console.print("[cyan]インターネット接続を確認中...[/cyan]")
    try:
        response = httpx.get("https://api.github.com", timeout=5, follow_redirects=True)
        console.print("[green]✓[/green] インターネット接続OK")
    except httpx.RequestError:
        console.print("[red]✗[/red] インターネット未接続 - テンプレートDLに必須")
        console.print("[yellow]ネットワーク設定を確認してください[/yellow]")

    console.print("\n[cyan]オプションツール:[/cyan]")
    git_ok = check_tool("git", "https://git-scm.com/downloads")

    console.print("\n[cyan]AIツール（任意）:[/cyan]")
    claude_ok = check_tool("claude", "https://docs.anthropic.com/en/docs/claude-code/setup からインストール")
    gemini_ok = check_tool("gemini", "https://github.com/google-gemini/gemini-cli からインストール")

    console.print("\n[green]✓ Specify CLIは利用可能です！[/green]")
    if not git_ok:
        console.print("[yellow]リポジトリ管理にはgitのインストールを推奨[/yellow]")
    if not (claude_ok or gemini_ok):
        console.print("[yellow]AIアシスタント導入で体験向上[/yellow]")


def main():
    app()


if __name__ == "__main__":
    main()
