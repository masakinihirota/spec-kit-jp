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
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

また、Claude Code に **レビュー & 受け入れチェックリスト** を検証するよう依頼し、要件を満たすものをチェックし、満たさないものは空のままにします。次のプロンプトを使用できます：

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

Claude Code との対話を仕様を明確化し質問する機会として使用することが重要です — **最初の試みを最終的なものとして扱わないでください**。

### **ステップ 3:** 計画を生成

技術スタックとその他の技術要件を具体的に指定できます。プロジェクトテンプレートに組み込まれた `/plan` コマンドを使用し、次のようなプロンプトを使用できます：

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
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

このプロセス中に、Claude Code が間違ったものを調査していることに気づくかもしれません — 次のようなプロンプトで正しい方向に導けます：

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
>Claude Code は熱心すぎて、要求していないコンポーネントを追加するかもしれません。根拠と変更のソースを明確にするよう依頼してください。

### **ステップ 4:** Claude Code に計画を検証させる

計画が整ったら、Claude Code に欠落部分がないことを確認するよう実行させます。次のようなプロンプトを使用できます：

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

これにより実装計画が洗練され、Claude Code が計画サイクルで逃した潜在的な盲点が回避されます。初期の洗練パスが完了したら、実装に移る前にチェックリストをもう一度実行します。

また、[GitHub CLI](https://docs.github.com/en/github-cli/github-cli) がインストールされている場合、Claude Code に現在のブランチから `main` への詳細な説明付きプルリクエストを作成するよう依頼できます。

>[!NOTE]
>エージェントに実装させる前に、詳細をクロスチェックして過剰設計された部分がないか確認する価値もあります（Claude Code は熱心すぎることを覚えておいてください）。過剰設計されたコンポーネントや決定が存在する場合、Claude Code にそれらを解決するよう依頼してください。Claude Code が計画を立てる際に [constitution](base/memory/constitution.md) を基礎となる部分として遵守することを確認してください。

### ステップ 5: 実装

準備ができたら、Claude Code にソリューションを実装するよう指示します（例のパスを含む）：

```text
implement specs/002-create-taskify/plan.md
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

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get started

### 1. Install Specify

Initialize your project depending on the coding agent you're using:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

### 2. Create the spec

Use the `/specify` command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/specify Build an application that can help me organize my photos in separate photo albums. Albums are grouped by date and can be re-organized by dragging and dropping on the main page. Albums never other nested albums. Within each album, photos are previewed in a tile-like interface.
```

### 3. Create a technical implementation plan

Use the `/plan` command to provide your tech stack and architecture choices.

```bash
/plan The application uses Vite with minimal number of libraries. Use vanilla HTML, CSS, and JavaScript as much as possible. Images are not uploaded anywhere and metadata is stored in a local SQLite database.
```

### 4. Break down and implement

Use `/tasks` to create an actionable task list, then ask your agent to implement the feature.

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📚 Core philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "_what_" before the "_how_"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development phases

| Phase | Focus | Key Activities |
|-------|-------|----------------|
| **0-to-1 Development** ("Greenfield") | Generate from scratch | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready applications</li></ul> |
| **Creative Exploration** | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple technology stacks & architectures</li><li>Experiment with UX patterns</li></ul> |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add features iteratively</li><li>Modernize legacy systems</li><li>Adapt processes</li></ul> |

## 🎯 Experimental goals

Our research and experimentation focus on:

### Technology independence

- Create applications using diverse technology stacks
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks

### Enterprise constraints

- Demonstrate mission-critical application development
- Incorporate organizational constraints (cloud providers, tech stacks, engineering practices)
- Support enterprise design systems and compliance requirements

### User-centric development

- Build applications for different user cohorts and preferences
- Support various development approaches (from vibe-coding to AI-native development)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative feature development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS** (or WSL2 on Windows)
- AI coding agent: [Claude Code](https://www.anthropic.com/claude-code), [GitHub Copilot](https://code.visualstudio.com/), or [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 📖 Learn more

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#detailed-process)** - Step-by-step implementation guide

---

## Detailed process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init --here
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot
# Or in current directory:
specify init --here --ai claude
```

The CLI will check if you have Claude Code or Gemini CLI installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Bootstrap the project

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/specify`, `/plan`, and `/tasks` commands available.

The first step should be creating a new project scaffolding. Use `/specify` command and then provide the concrete requirements for the project you want to develop.

>[!IMPORTANT]
>Be as explicit as possible about _what_ you are trying to build and _why_. **Do not focus on the tech stack at this point**.

An example prompt:

```text
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

After this prompt is entered, you should see Claude Code kick off the planning and spec drafting process. Claude Code will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-create-taskify`), as well as a new specification in the `specs/001-create-taskify` directory.

The produced specification should contain a set of user stories and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

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

### **STEP 2:** Functional specification clarification

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt. For example, you could use a prompt like this within the same Claude Code session:

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15
tasks for each one randomly distributed into different states of completion. Make sure that there's at least
one task in each stage of completion.
```

You should also ask Claude Code to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with Claude Code as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 3:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/plan` command that is built into the project template with a prompt like this:

```text
We are going to generate this using .NET Aspire, using Postgres as the database. The frontend should use
Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API,
tasks API, and a notifications API.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

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

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask Claude Code to refine it if any of the components stand out, or even have it check the locally-installed version of the platform/framework you want to use (e.g., .NET).

Additionally, you might want to ask Claude Code to research details about the chosen tech stack if it's something that is rapidly changing (e.g., .NET Aspire, JS frameworks), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could
benefit from additional research as .NET Aspire is a rapidly changing library. For those areas that you identify that
require further research, I want you to update the research document with additional details about the specific
versions that we are going to be using in this Taskify application and spawn parallel research tasks to clarify
any details using research from the web.
```

During this process, you might find that Claude Code gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

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
>Claude Code might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 4:** Have Claude Code validate the plan

With the plan in place, you should have Claude Code run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files.
Read through it with an eye on determining whether or not there is a sequence of tasks that you need
to be doing that are obvious from reading this. Because I don't know if there's enough here. For example,
when I look at the core implementation, it would be useful to reference the appropriate places in the implementation
details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that Claude Code missed in its planning cycle. Once the initial refinement pass is complete, ask Claude Code to go through the checklist once more before you can get to the implementation.

You can also ask Claude Code (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

>[!NOTE]
>Before you have the agent implement it, it's also worth prompting Claude Code to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask Claude Code to resolve them. Ensure that Claude Code follows the [constitution](base/memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### STEP 5: Implementation

Once ready, instruct Claude Code to implement your solution (example path included):

```text
implement specs/002-create-taskify/plan.md
```

Claude Code will spring into action and will start creating the implementation.

>[!IMPORTANT]
>Claude Code will execute local CLI commands (such as `dotnet`) - make sure you have them installed on your machine.

Once the implementation step is done, ask Claude Code to try to run the application and resolve any emerging build errors. If the application runs, but there are _runtime errors_ that are not directly available to Claude Code through CLI logs (e.g., errors rendered in browser logs), copy and paste the error in Claude Code and have it attempt to resolve it.

</details>

---

## Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

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

## Maintainers

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam).

## License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.
