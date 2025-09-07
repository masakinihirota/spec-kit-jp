<div align="center">
    <img src="./media/logo_small.webp"/>
    <h1>🌱 Spec Kit</h1>
    <h3><em>高品質なソフトウェアをより速く構築。</em></h3>
</div>

<p align="center">
    <strong>Spec-Driven Development の助けを借りて、組織が製品シナリオに集中し、差別化されていないコードを書くことを避けるための取り組み。</strong>
</p>

[![Release](https://github.com/github/spec-kit/actions/workflows/release.yml/badge.svg)](https://github.com/github/spec-kit/actions/workflows/release.yml)

---

## 目次

- [🤔 Spec-Driven Development とは何ですか？](#-what-is-spec-driven-development)
- [⚡ 始めましょう](#-get-started)
- [📚 コア哲学](#-core-philosophy)
- [🌟 開発フェーズ](#-development-phases)
- [🎯 実験目標](#-experimental-goals)
- [🔧 前提条件](#-prerequisites)
- [📖 詳細を見る](#-learn-more)
- [詳細プロセス](#detailed-process)
- [トラブルシューティング](#troubleshooting)

## 🤔 Spec-Driven Development とは何ですか？

Spec-Driven Development は、伝統的なソフトウェア開発の**脚本を逆転**させます。何十年もの間、コードが王様でした — 仕様はコーディングの「本番作業」が始まると捨てられる足場のようなものでした。Spec-Driven Development はこれを変えます：**仕様が実行可能**になり、単にガイドするのではなく、直接動作する実装を生成します。

## ⚡ 始めましょう

### 1. Specify をインストール

使用しているコーディングエージェントに応じてプロジェクトを初期化します：

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

### 2. 仕様を作成

`/specify` コマンドを使用して、構築したいものを説明します。技術スタックではなく、**何を**と**なぜ**に焦点を当てます。

```bash
/specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums never other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 3. 技術実装計画を作成

`/plan` コマンドを使用して、技術スタックとアーキテクチャの選択を提供します。

```bash
/plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 4. ブレークダウンと実装

`/tasks` を使用して実行可能なタスクリストを作成し、エージェントに機能を実装するよう依頼します。

詳細なステップバイステップの手順については、[包括的なガイド](./spec-driven.md) を参照してください。

## 📚 コア哲学

Spec-Driven Development は、以下の点を強調する構造化されたプロセスです：

- **意図駆動開発** 仕様が "_何を_" を "_どのように_" の前に定義する
- **豊富な仕様作成** ガードレールと組織原則を使用
- **多段階の洗練** プロンプトからのワンショットコード生成ではなく
- **高度な AI モデル能力への重い依存** 仕様解釈のため

## 🌟 開発フェーズ

| フェーズ | 焦点 | 主な活動 |
|-------|-------|----------------|
| **0-to-1 開発** ("Greenfield") | ゼロから生成 | <ul><li>高レベルの要件から始める</li><li>仕様を生成</li><li>実装ステップを計画</li><li>本番対応アプリケーションを構築</li></ul> |
| **創造的探索** | 並行実装 | <ul><li>多様なソリューションを探求</li><li>複数の技術スタックとアーキテクチャをサポート</li><li>UX パターンを実験</li></ul> |
| **反復強化** ("Brownfield") | Brownfield 近代化 | <ul><li>機能を反復的に追加</li><li>レガシーシステムを近代化</li><li>プロセスを適応</li></ul> |

## 🎯 実験目標

私たちの研究と実験は以下の点に焦点を当てています：

### 技術独立性

- 多様な技術スタックを使用してアプリケーションを作成
- Spec-Driven Development が特定の技術、プログラミング言語、フレームワークに縛られないプロセスであるという仮説を検証

### エンタープライズ制約

- ミッションクリティカルなアプリケーション開発を実証
- 組織的制約（クラウドプロバイダー、技術スタック、エンジニアリングプラクティス）を組み込む
- エンタープライズデザインシステムとコンプライアンス要件をサポート

### ユーザー中心開発

- 異なるユーザーコホートと好みに合わせてアプリケーションを構築
- さまざまな開発アプローチをサポート（vibe-coding から AI-native 開発まで）

### 創造的・反復プロセス

- 並行実装探索の概念を検証
- 堅牢な反復機能開発ワークフローを提供
- アップグレードと近代化タスクを処理するプロセスを拡張

## 🔧 前提条件

- **Linux/macOS** (または Windows の WSL2)
- AI コーディングエージェント: [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://code.visualstudio.com/), または [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [uv](https://docs.astral.sh/uv/) パッケージ管理用
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 📖 詳細を見る

- **[完全な Spec-Driven Development 方法論](./spec-driven.md)** - プロセスの詳細な解説
- **[詳細なウォークスルー](#detailed-process)** - ステップバイステップの実装ガイド

---

## 詳細プロセス

<details>
<summary>詳細なステップバイステップのウォークスルーを展開するにはクリック</summary>

Specify CLI を使用してプロジェクトをブートストラップし、環境に必要なアーティファクトを導入できます。実行：

```bash
specify init <project_name>
```

または現在のディレクトリで初期化：

```bash
specify init --here
```

![Specify CLI がターミナルで新しいプロジェクトをブートストラップ](./media/specify_cli.gif)

使用している AI エージェントを選択するよう促されます。また、ターミナルで直接指定することもできます：

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot
# または現在のディレクトリで：
specify init --here --ai claude
```

CLI は Claude Code または Gemini CLI がインストールされているかをチェックします。インストールされていない場合、または適切なツールのチェックなしでテンプレートを取得したい場合は、コマンドに `--ignore-agent-tools` を使用します：

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **ステップ 1:** プロジェクトをブートストラップ

プロジェクトフォルダに移動し、AI エージェントを実行します。この例では `claude` を使用します。

![Claude Code 環境のブートストラップ](./media/bootstrap-claude-code.gif)

`/specify`、`/plan`、`/tasks` コマンドが利用可能であれば、正しく構成されていることがわかります。

最初のステップは新しいプロジェクトのスキャフォールディングを作成することです。`/specify` コマンドを使用し、開発したいプロジェクトの具体的な要件を提供します。

>[!IMPORTANT]
>構築しようとしている _何を_ と _なぜ_ についてできる限り明確にしてください。**この時点では技術スタックに焦点を当てないでください**。

例のプロンプト：

```text
Taskify というチーム生産性プラットフォームを開発してください。ユーザーはプロジェクトを作成し、チームメンバーを追加し、タスクを割り当て、コメントし、タスクをカンバン形式のボード間で移動できるようにします。この機能の最初のフェーズでは「Create Taskify」と呼び、ユーザーは事前に定義された複数人とします。1人のプロダクトマネージャーと4人のエンジニア、計5人のユーザーを2つのカテゴリで用意してください。サンプルプロジェクトを3つ作成します。各タスクの状態は「To Do」「In Progress」「In Review」「Done」の標準的なカンバンカラムを持ちます。このアプリケーションにはログイン機能は不要です。これは基本機能のテスト用です。タスクカードのUIでは、タスクの状態をカンバンボードの異なるカラム間で変更できるようにしてください。各カードには無制限にコメントを残せます。また、そのタスクカードから有効なユーザーを割り当てられるようにしてください。Taskifyを起動すると、5人のユーザーリストから選択できます。パスワードは不要です。ユーザーをクリックすると、プロジェクト一覧画面に遷移します。プロジェクトをクリックすると、そのプロジェクトのカンバンボードが開きます。カラムが表示され、カードをドラッグ＆ドロップでカラム間移動できます。現在ログイン中のユーザーに割り当てられたカードは他と色分けされ、すぐに自分のカードが分かります。自分のコメントは編集・削除できますが、他人のコメントは編集・削除できません。
Develop Taskify, a team productivity platform. It should allow users to create projects, add team members,
assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature,
let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined.
I want five users in two different categories, one product manager and four engineers. Let's create three
different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do,"
"In Progress," "In Review," and "Done." There will be no login for this application as this is just the very
first testing thing to ensure that our basic features are set up. For each task in the UI for a task card,
you should be able to change the current status of the task between the different columns in the Kanban work board.
You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task
card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick
from. There will be no password required. When you click on a user, you go into the main view, which displays the list of
projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns.
You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are
assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly
see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can
delete any comments that you made, but you can't delete comments anybody else made.
```

このプロンプトを入力すると、Claude Code が計画と仕様ドラフトプロセスを開始します。Claude Code はリポジトリをセットアップするための組み込みスクリプトもトリガーします。

このステップが完了すると、新しいブランチ（例: `001-create-taskify`）と `specs/001-create-taskify` ディレクトリの新しい仕様が作成されます。

生成された仕様には、テンプレートで定義されたユーザーストーリーと機能要件のセットが含まれます。

この段階で、プロジェクトフォルダの内容は以下のようになります：

```text
├── memory
│	 ├── constitution.md
│	 └── constitution_update_checklist.md
├── scripts
│	 ├── check-task-prerequisites.sh
│	 ├── common.sh
│	 ├── create-new-feature.sh
│	 ├── get-feature-paths.sh
│	 ├── setup-plan.sh
│	 └── update-claude-md.sh
├── specs
│	 └── 001-create-taskify
│	     └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

### **ステップ 2:** 機能仕様の明確化

ベースライン仕様が作成されたら、最初の試みで適切にキャプチャされなかった要件を明確化できます。たとえば、同じ Claude Code セッション内で次のようなプロンプトを使用できます：


```text
各サンプルプロジェクトごとに、5〜15個のタスクをランダムに異なる進捗状態で割り当ててください。必ず各進捗状態（To Do、In Progress、In Review、Done）に最低1つはタスクが存在するようにしてください。
```

また、Claude Code に **レビュー & 受け入れチェックリスト** を検証するよう依頼し、要件を満たすものをチェックし、満たさないものは空のままにします。次のプロンプトを使用できます：


```text
レビューと受け入れチェックリストを読み、仕様が基準を満たしている項目にはチェックを入れてください。満たしていない場合は空欄のままにしてください。
```

Claude Code との対話を仕様を明確化し質問する機会として使用することが重要です — **最初の試みを最終的なものとして扱わないでください**。

### **ステップ 3:** 計画を生成

技術スタックとその他の技術要件を具体的に指定できます。プロジェクトテンプレートに組み込まれた `/plan` コマンドを使用し、次のようなプロンプトを使用できます：


```text
この実装は .NET Aspire を使い、データベースには Postgres を利用します。フロントエンドは Blazor サーバーで、タスクボードのドラッグ＆ドロップやリアルタイム更新に対応させてください。REST API（projects API、tasks API、notifications API）も作成してください。
```

このステップの出力にはいくつかの実装詳細ドキュメントが含まれ、ディレクトリツリーは以下のようになります：

```text
.
├── CLAUDE.md
├── memory
│	 ├── constitution.md
│	 └── constitution_update_checklist.md
├── scripts
│	 ├── check-task-prerequisites.sh
│	 ├── common.sh
│	 ├── create-new-feature.sh
│	 ├── get-feature-paths.sh
│	 ├── setup-plan.sh
│	 └── update-claude-md.sh
├── specs
│	 └── 001-create-taskify
│	     ├── contracts
│	     │	 ├── api-spec.json
│	     │	 └── signalr-spec.md
│	     ├── data-model.md
│	     ├── plan.md
│	     ├── quickstart.md
│	     ├── research.md
│	     └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

指示に基づいて正しい技術スタックが使用されていることを確認するために `research.md` ドキュメントをチェックします。コンポーネントが目立つ場合は Claude Code にそれを洗練するよう依頼したり、ローカルにインストールされたプラットフォーム/フレームワークのバージョンをチェックしたりできます（例: .NET）。

さらに、選択した技術スタックが急速に変化しているもの（例: .NET Aspire、JS フレームワーク）であれば、詳細を調査するよう Claude Code に依頼できます。次のようなプロンプトを使用できます：


```text
実装計画や詳細を確認し、.NET Aspire のような急速に変化するライブラリについて追加調査が必要な箇所を洗い出してください。追加調査が必要な箇所があれば、Taskifyアプリで使用する具体的なバージョン情報などを research ドキュメントに追記し、ウェブ調査による並列リサーチタスクも立ち上げてください。
```

このプロセス中に、Claude Code が間違ったものを調査していることに気づくかもしれません — 次のようなプロンプトで正しい方向に導けます：


```text
これを一連のステップに分解する必要があると思います。まず、実装中に不明点や追加調査が有益そうなタスクをリストアップしてください。その後、それぞれのタスクごとに個別のリサーチタスクを立ち上げ、すべての具体的な疑問点を並行して調査してください。今のままだと.NET Aspire全体を漠然と調べているように見えますが、それでは十分な成果は得られません。リサーチは必ず具体的な疑問解決に役立つものであるべきです。
```

>[!NOTE]
>Claude Code は熱心すぎて、要求していないコンポーネントを追加するかもしれません。根拠と変更のソースを明確にするよう依頼してください。

### **ステップ 4:** Claude Code に計画を検証させる

計画が整ったら、Claude Code に欠落部分がないことを確認するよう実行させます。次のようなプロンプトを使用できます：


```text
実装計画や詳細ファイルを監査し、読むだけで明らかに実施すべきタスクの流れが抜けなく記載されているか確認してください。例えばコア実装部分を見たとき、各ステップで参照すべき詳細情報の場所が明示されているとより分かりやすいです。
```

これにより実装計画が洗練され、Claude Code が計画サイクルで逃した潜在的な盲点が回避されます。初期の洗練パスが完了したら、実装に移る前にチェックリストをもう一度実行します。

また、[GitHub CLI](https://docs.github.com/en/github-cli/github-cli) がインストールされている場合、Claude Code に現在のブランチから `main` への詳細な説明付きプルリクエストを作成するよう依頼できます。

>[!NOTE]
>エージェントに実装させる前に、詳細をクロスチェックして過剰設計された部分がないか確認する価値もあります（Claude Code は熱心すぎることを覚えておいてください）。過剰設計されたコンポーネントや決定が存在する場合、Claude Code にそれらを解決するよう依頼してください。Claude Code が計画を立てる際に [constitution](base/memory/constitution.md) を基礎となる部分として遵守することを確認してください。

### ステップ 5: 実装

準備ができたら、Claude Code にソリューションを実装するよう指示します（例のパスを含む）：


```text
specs/002-create-taskify/plan.md を実装してください
```

Claude Code が動き出し、実装を開始します。

>[!IMPORTANT]
>Claude Code はローカルの CLI コマンド（例: `dotnet`）を実行します — マシンにそれらがインストールされていることを確認してください。

実装ステップが完了したら、Claude Code にアプリケーションを実行し、発生するビルドエラーを解決するよう依頼します。アプリケーションが実行されるが、CLI ログから直接利用できないランタイムエラーがある場合（例: ブラウザログにレンダリングされるエラー）、Claude Code にエラーをコピーして貼り付け、解決を試みるよう依頼します。

</details>

---

## トラブルシューティング

### Linux での Git Credential Manager

Linux で Git 認証に問題がある場合は、Git Credential Manager をインストールできます：

```bash
#!/bin/bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## メンテナー

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## サポート

サポートについては、[GitHub イシュー](https://github.com/github/spec-kit/issues/new) を開いてください。バグ報告、機能リクエスト、Spec-Driven Development の使用に関する質問を歓迎します。

## 謝辞

このプロジェクトは [John Lam](https://github.com/jflam) の作業と研究に大きく影響を受けています。

## ライセンス

このプロジェクトは MIT オープンソースライセンスの条件の下でライセンスされています。完全な条件については [LICENSE](./LICENSE) ファイルを参照してください。


## 🤔 Spec-Driven Development とは？

Spec-Driven Development（仕様駆動開発）は、従来のソフトウェア開発の「常識」を覆します。何十年もの間、コードが主役であり、仕様は「本番のコーディング」が始まると捨てられる足場のようなものでした。Spec-Driven Development では、**仕様が実行可能**となり、単なるガイドではなく、直接動作する実装を生成します。


## ⚡ はじめに

### 1. Specify のインストール

利用するコーディングエージェントに応じてプロジェクトを初期化します：

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

### 2. 仕様を作成

`/specify` コマンドを使って、作りたいものを説明します。技術スタックではなく、**何を**・**なぜ**に集中してください。

```bash
/specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums never other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 3. 技術実装計画を作成

`/plan` コマンドで技術スタックやアーキテクチャの選択を指定します。

```bash
/plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 4. ブレークダウンと実装

`/tasks` で実行可能なタスクリストを作成し、エージェントに機能実装を依頼します。

詳しい手順は[包括的なガイド](./spec-driven.md)をご覧ください。


## 📚 コア哲学

Spec-Driven Development は、以下の点を重視する構造化されたプロセスです：

- **意図駆動開発** 仕様が「_何を_」を「_どのように_」より先に定義する
- **豊富な仕様作成** ガードレールや組織原則を活用
- **多段階の洗練** プロンプトからの一発コード生成ではなく段階的に精緻化
- **高度なAIモデル能力への依存** 仕様解釈のため


## 🌟 開発フェーズ

| フェーズ | 焦点 | 主な活動 |
|-------|-------|----------------|
| **0-to-1開発**（グリーンフィールド） | ゼロから生成 | <ul><li>高レベル要件から開始</li><li>仕様を生成</li><li>実装ステップを計画</li><li>本番対応アプリケーションを構築</li></ul> |
| **創造的探索** | 並行実装 | <ul><li>多様なソリューションを探求</li><li>複数の技術スタック・アーキテクチャをサポート</li><li>UXパターンを実験</li></ul> |
| **反復強化**（ブラウンフィールド） | 既存システムの近代化 | <ul><li>機能を反復的に追加</li><li>レガシーシステムを近代化</li><li>プロセスを適応</li></ul> |


## 🎯 実験目標

私たちの研究と実験は以下に焦点を当てています：

### 技術独立性

- 多様な技術スタックでアプリケーションを作成
- Spec-Driven Development が特定の技術・言語・フレームワークに依存しないことを検証

### エンタープライズ制約

- ミッションクリティカルなアプリ開発を実証
- 組織的制約（クラウド、技術スタック、エンジニアリングプラクティス）を組み込む
- エンタープライズデザインシステムやコンプライアンス要件をサポート

### ユーザー中心開発

- 異なるユーザー層や好みに合わせてアプリを構築
- 様々な開発アプローチ（vibe-coding から AI-native まで）をサポート

### 創造的・反復プロセス

- 並行実装探索の概念を検証
- 強固な反復的機能開発ワークフローを提供
- アップグレードや近代化タスクへの対応を拡張


## 🔧 前提条件

- **Linux/macOS**（または Windows の WSL2）
- AI コーディングエージェント: [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://code.visualstudio.com/), [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [uv](https://docs.astral.sh/uv/) パッケージ管理用
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)


## 📖 詳細を見る

- **[Spec-Driven Development 完全ガイド](./spec-driven.md)** - プロセスの詳細解説
- **[詳細なウォークスルー](#detailed-process)** - ステップバイステップの実装ガイド

---


## 詳細プロセス

<details>
<summary>詳細なステップバイステップのウォークスルーを展開するにはクリック</summary>

Specify CLI を使ってプロジェクトをブートストラップし、必要なアーティファクトを環境に導入できます。実行：

```bash
specify init <project_name>
```

または現在のディレクトリで初期化：

```bash
specify init --here
```

![Specify CLI がターミナルで新しいプロジェクトをブートストラップ](./media/specify_cli.gif)

利用するAIエージェントを選択するよう促されます。ターミナルで直接指定することも可能です：

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot
# または現在のディレクトリで：
specify init --here --ai claude
```

CLIはClaude CodeやGemini CLIがインストールされているかをチェックします。インストールされていない場合や、ツールのチェックなしでテンプレートだけ取得したい場合は `--ignore-agent-tools` を付けてください：

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **ステップ1:** プロジェクトのブートストラップ

プロジェクトフォルダに移動し、AIエージェントを実行します。この例では `claude` を使用します。

![Claude Code 環境のブートストラップ](./media/bootstrap-claude-code.gif)

`/specify`、`/plan`、`/tasks` コマンドが利用可能であれば、正しく構成されています。

最初のステップは新しいプロジェクトのスキャフォールディング作成です。`/specify` コマンドで開発したいプロジェクトの具体的な要件を入力します。

>[!IMPORTANT]
>作りたい _何を_ と _なぜ_ をできるだけ明確にしてください。**この時点では技術スタックにこだわらないでください**。

例のプロンプト：

```text
Taskify というチーム生産性プラットフォームを開発してください。ユーザーはプロジェクトを作成し、チームメンバーを追加し、タスクを割り当て、コメントし、タスクをカンバン形式のボード間で移動できるようにします。この機能の最初のフェーズでは「Create Taskify」と呼び、ユーザーは事前に定義された複数人とします。1人のプロダクトマネージャーと4人のエンジニア、計5人のユーザーを2つのカテゴリで用意してください。サンプルプロジェクトを3つ作成します。各タスクの状態は「To Do」「In Progress」「In Review」「Done」の標準的なカンバンカラムを持ちます。このアプリケーションにはログイン機能は不要です。これは基本機能のテスト用です。タスクカードのUIでは、タスクの状態をカンバンボードの異なるカラム間で変更できるようにしてください。各カードには無制限にコメントを残せます。また、そのタスクカードから有効なユーザーを割り当てられるようにしてください。Taskifyを起動すると、5人のユーザーリストから選択できます。パスワードは不要です。ユーザーをクリックすると、プロジェクト一覧画面に遷移します。プロジェクトをクリックすると、そのプロジェクトのカンバンボードが開きます。カラムが表示され、カードをドラッグ＆ドロップでカラム間移動できます。現在ログイン中のユーザーに割り当てられたカードは他と色分けされ、すぐに自分のカードが分かります。自分のコメントは編集・削除できますが、他人のコメントは編集・削除できません。
```

このプロンプトを入力すると、Claude Code が計画と仕様ドラフトプロセスを開始します。Claude Code はリポジトリセットアップ用の組み込みスクリプトも実行します。

このステップが完了すると、新しいブランチ（例: `001-create-taskify`）と `specs/001-create-taskify` ディレクトリの新しい仕様が作成されます。

生成された仕様には、テンプレートで定義されたユーザーストーリーや機能要件が含まれます。

この段階で、プロジェクトフォルダの内容は以下のようになります：

```text
├── memory
│\t ├── constitution.md
│\t └── constitution_update_checklist.md
├── scripts
│\t ├── check-task-prerequisites.sh
│\t ├── common.sh
│\t ├── create-new-feature.sh
│\t ├── get-feature-paths.sh
│\t ├── setup-plan.sh
│\t └── update-claude-md.sh
├── specs
│\t └── 001-create-taskify
│\t     └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

### **ステップ2:** 機能仕様の明確化

ベースライン仕様が作成されたら、最初の試みで適切にキャプチャされなかった要件を明確化できます。たとえば、同じ Claude Code セッション内で次のようなプロンプトを使えます：

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

また、Claude Code に **レビュー＆受け入れチェックリスト** を検証するよう依頼し、要件を満たすものをチェックし、満たさないものは空のままにします。次のプロンプトを使えます：

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

Claude Code との対話は仕様を明確化し質問する機会です — **最初の試みを最終としないでください**。

### **ステップ3:** 計画の生成

技術スタックやその他の技術要件を具体的に指定できます。プロジェクトテンプレートに組み込まれた `/plan` コマンドを使い、次のようなプロンプトを利用できます：

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

このステップの出力にはいくつかの実装詳細ドキュメントが含まれ、ディレクトリツリーは以下のようになります：

```text
.
├── CLAUDE.md
├── memory
│\t ├── constitution.md
│\t └── constitution_update_checklist.md
├── scripts
│\t ├── check-task-prerequisites.sh
│\t ├── common.sh
│\t ├── create-new-feature.sh
│\t ├── get-feature-paths.sh
│\t ├── setup-plan.sh
│\t └── update-claude-md.sh
├── specs
│\t └── 001-create-taskify
│\t     ├── contracts
│\t     │\t ├── api-spec.json
│\t     │\t └── signalr-spec.md
│\t     ├── data-model.md
│\t     ├── plan.md
│\t     ├── quickstart.md
│\t     ├── research.md
│\t     └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

`research.md` ドキュメントで、指示通りの技術スタックが使われているか確認してください。気になる点があれば Claude Code に洗練を依頼したり、ローカルのプラットフォーム/フレームワークのバージョンをチェックさせたりできます（例: .NET）。

また、選択した技術スタックが急速に変化している場合（例: .NET Aspire、JSフレームワーク）、Claude Code に追加調査を依頼できます。次のようなプロンプトを使えます：

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

この過程で、Claude Code が間違ったものを調査している場合は、次のようなプロンプトで正しい方向に導けます：

```text
I think we need to break this down into a series of steps. First, identify a list of tasks
that you would need to do during implementation that you're not sure of or would benefit
from further research. Write down a list of those tasks. And then for each one of these tasks,
I want you to spin up a separate research task so that the net results is we are researching
all of those very specific tasks in parallel. What I saw you doing was it looks like you were
researching .NET Aspire in general and I don't think that's gonna do much for us in this case.
That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

>[!NOTE]
>Claude Code は熱心すぎて、要求していないコンポーネントを追加することがあります。根拠や変更の理由を明確にするよう依頼してください。

### **ステップ4:** Claude Code に計画を検証させる

計画が整ったら、Claude Code に欠落部分がないか確認させます。次のようなプロンプトを使えます：

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

これにより実装計画が洗練され、Claude Code の計画サイクルで見落とされた盲点を回避できます。初期の洗練パスが終わったら、実装前にもう一度チェックリストを実行させてください。

また、[GitHub CLI](https://docs.github.com/en/github-cli/github-cli) がインストールされていれば、現在のブランチから `main` への詳細な説明付きプルリクエストを作成するよう Claude Code に依頼できます。

>[!NOTE]
>実装前に、過剰設計された部分がないかクロスチェックするよう Claude Code に依頼するのも有効です（Claude Code は熱心すぎることがあります）。過剰設計があれば解決を依頼し、[constitution](base/memory/constitution.md) を必ず遵守させてください。

### ステップ5: 実装

準備ができたら、Claude Code にソリューションを実装するよう指示します（例のパスを含む）：

```text
implement specs/002-create-taskify/plan.md
```

Claude Code が動き出し、実装を開始します。

>[!IMPORTANT]
>Claude Code はローカルCLIコマンド（例: `dotnet`）を実行します。マシンにインストールされていることを確認してください。

実装が完了したら、Claude Code にアプリケーションを実行させ、ビルドエラーがあれば解決させます。アプリが実行できてもCLIログから直接取得できないランタイムエラー（例: ブラウザログのエラー）がある場合は、そのエラーを Claude Code に貼り付けて解決を依頼してください。

</details>

---


## トラブルシューティング

### Linux での Git Credential Manager

Linux で Git 認証に問題がある場合は、Git Credential Manager をインストールできます：

```bash
#!/bin/bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## メンテナー

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## サポート

サポートが必要な場合は、[GitHub イシュー](https://github.com/github/spec-kit/issues/new) を開いてください。バグ報告、機能リクエスト、Spec-Driven Development の利用に関する質問を歓迎します。

## 謝辞

このプロジェクトは [John Lam](https://github.com/jflam) の作業と研究に大きく影響を受けています。

## ライセンス

このプロジェクトは MIT オープンソースライセンスの条件の下でライセンスされています。詳細は [LICENSE](./LICENSE) ファイルをご覧ください。
