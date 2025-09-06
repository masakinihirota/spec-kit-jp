## Spec Kit への貢献

こんにちは！Spec Kit に貢献したいと考えてくださり、ありがとうございます。このプロジェクトへの貢献は、[プロジェクトのオープンソースライセンス](LICENSE) の下で公開されます。

このプロジェクトは [Contributor Code of Conduct](CODE_OF_CONDUCT.md) とともにリリースされていることに注意してください。このプロジェクトに参加することで、その条件に従うことに同意したことになります。

## コードの実行とテストのための前提条件

これらは、プルリクエスト（PR）提出プロセスの一部として変更をローカルでテストできるようにするために必要な1回限りのインストールです。

1. [Python 3.11+](https://www.python.org/downloads/) をインストール
1. パッケージ管理用に [uv](https://docs.astral.sh/uv/) をインストール
1. [Git](https://git-scm.com/downloads) をインストール
1. AI コーディングエージェントを用意：[Claude Code](https://www.anthropic.com/claude-code)、[GitHub Copilot](https://code.visualstudio.com/)、または [Gemini CLI](https://github.com/google-gemini/gemini-cli)

## プルリクエストの提出

1. リポジトリをフォークしてクローン
1. 依存関係を設定してインストール：`uv sync`
1. CLI がマシンで動作することを確認：`uv run specify --help`
1. 新しいブランチを作成：`git checkout -b my-branch-name`
1. 変更を加え、テストを追加し、すべてがまだ動作することを確認
1. 関連する場合、サンプルプロジェクトで CLI 機能をテスト
1. フォークにプッシュしてプルリクエストを提出
1. プルリクエストがレビューされてマージされるのを待つ。

プルリクエストが受け入れられる可能性を高めるためにできること：

- プロジェクトのコーディング規約に従う。
- 新機能のテストを書く。
- 変更がユーザー向け機能に影響する場合、ドキュメント（`README.md,` `spec-driven.md`）を更新。
- 変更を可能な限り焦点を絞ったものにする。相互依存しない複数の変更をしたい場合は、別々のプルリクエストとして提出することを検討。
- [良いコミットメッセージ](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) を書く。
- Spec-Driven Development ワークフローで変更をテストして互換性を確保。

## 開発ワークフロー

spec-kit で作業する場合：

1. 選択したコーディングエージェントで `specify` CLI コマンド（`/specify`、`/plan`、`/tasks`）を使用して変更をテスト
2. `templates/` ディレクトリでテンプレートが正しく動作することを確認
3. `scripts/` ディレクトリでスクリプト機能をテスト
4. 主要なプロセス変更がある場合、メモリファイル（`memory/constitution.md`）が更新されていることを確認

## リソース

- [Spec-Driven Development 方法論](./spec-driven.md)
- [オープンソースへの貢献方法](https://opensource.guide/how-to-contribute/)
- [プルリクエストの使用](https://help.github.com/articles/about-pull-requests/)
- [GitHub ヘルプ](https://help.github.com)
