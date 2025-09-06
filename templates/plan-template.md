# 実装計画: [FEATURE]

**ブランチ**: `[###-feature-name]` | **日付**: [DATE] | **仕様**: [link]
**入力**: `/specs/[###-feature-name]/spec.md` からの機能仕様

## 実行フロー (/plan コマンドスコープ)
```
1. 入力パスから機能仕様をロード
   → 見つからない場合: ERROR " {path} に機能仕様なし"
2. 技術的コンテキストを埋める (NEEDS CLARIFICATION をスキャン)
   → コンテキストからプロジェクトタイプを検出 (web=frontend+backend, mobile=app+api)
   → プロジェクトタイプに基づいて構造決定を設定
3. 下記の憲法チェックセクションを評価
   → 違反が存在する場合: 複雑さ追跡に文書化
   → 正当化不可能の場合: ERROR "まずアプローチを簡素化"
   → 進捗追跡を更新: 初期憲法チェック
4. フェーズ 0 を実行 → research.md
   → NEEDS CLARIFICATION が残っている場合: ERROR "不明点を解決"
5. フェーズ 1 を実行 → contracts, data-model.md, quickstart.md, エージェント固有のテンプレートファイル (例: Claude Code の `CLAUDE.md`, GitHub Copilot の `.github/copilot-instructions.md`, Gemini CLI の `GEMINI.md`)
6. 憲法チェックセクションを再評価
   → 新しい違反がある場合: 設計をリファクタリング, フェーズ 1 に戻る
   → 進捗追跡を更新: 設計後憲法チェック
7. フェーズ 2 を計画 → タスク生成アプローチを記述 (tasks.md を作成しない)
8. 停止 - /tasks コマンドの準備完了
```

**重要**: /plan コマンドはステップ 7 で停止。フェーズ 2-4 は他のコマンドによって実行:
- フェーズ 2: /tasks コマンドが tasks.md を作成
- フェーズ 3-4: 実装実行 (手動またはツール経由)

## 要約
[Extract from feature spec: primary requirement + technical approach from research]

## 技術的コンテキスト
**言語/バージョン**: [例: Python 3.11, Swift 5.9, Rust 1.75 または NEEDS CLARIFICATION]
**主要依存関係**: [例: FastAPI, UIKit, LLVM または NEEDS CLARIFICATION]
**ストレージ**: [該当する場合, 例: PostgreSQL, CoreData, files または N/A]
**テスト**: [例: pytest, XCTest, cargo test または NEEDS CLARIFICATION]
**ターゲットプラットフォーム**: [例: Linux server, iOS 15+, WASM または NEEDS CLARIFICATION]
**プロジェクトタイプ**: [single/web/mobile - ソース構造を決定]
**パフォーマンス目標**: [ドメイン固有, 例: 1000 req/s, 10k lines/sec, 60 fps または NEEDS CLARIFICATION]
**制約**: [ドメイン固有, 例: <200ms p95, <100MB memory, offline-capable または NEEDS CLARIFICATION]
**規模/範囲**: [ドメイン固有, 例: 10k users, 1M LOC, 50 screens または NEEDS CLARIFICATION]

## 憲法チェック
*ゲート: フェーズ 0 研究前に合格する必要。フェーズ 1 設計後に再チェック。*

**シンプルさ**:
- プロジェクト: [#] (最大 3 - 例: api, cli, tests)
- フレームワークを直接使用? (ラッパークラスなし)
- 単一データモデル? (シリアライズが異なる場合を除き DTO なし)
- パターンを避ける? (証明された必要性なしで Repository/UoW なし)

**アーキテクチャ**:
- すべての機能をライブラリとして? (直接アプリコードなし)
- ライブラリリスト: [各々の名前 + 目的]
- ライブラリごとの CLI: [ --help/--version/--format 付きコマンド]
- ライブラリドキュメント: llms.txt 形式を計画?

**テスト (交渉不可)**:
- RED-GREEN-Refactor サイクルを強制? (テストは最初に失敗する必要)
- Git コミットは実装前にテストを表示?
- 順序: Contract→Integration→E2E→Unit を厳格に遵守?
- 実際の依存関係を使用? (実際の DB, モックなし)
- 統合テスト対象: 新しいライブラリ, 契約変更, 共有スキーマ?
- 禁止: テスト前に実装, RED フェーズをスキップ

**観測性**:
- 構造化ログを含める?
- フロントエンドログ → バックエンド? (統合ストリーム)
- エラーコンテキストは十分?

**バージョン管理**:
- バージョン番号を割り当て? (MAJOR.MINOR.BUILD)
- すべての変更で BUILD を増分?
- 破壊的変更を処理? (並列テスト, 移行計画)

## プロジェクト構造

### 文書 (この機能)
```
specs/[###-feature]/
├── plan.md              # このファイル (/plan コマンド出力)
├── research.md          # フェーズ 0 出力 (/plan コマンド)
├── data-model.md        # フェーズ 1 出力 (/plan コマンド)
├── quickstart.md        # フェーズ 1 出力 (/plan コマンド)
├── contracts/           # フェーズ 1 出力 (/plan コマンド)
└── tasks.md             # フェーズ 2 出力 (/tasks コマンド - /plan によって作成されない)
```

### ソースコード (リポジトリルート)
```
# オプション 1: 単一プロジェクト (デフォルト)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# オプション 2: Web アプリケーション ("frontend" + "backend" が検出された場合)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# オプション 3: モバイル + API ("iOS/Android" が検出された場合)
api/
└── [上記の backend と同じ]

ios/ または android/
└── [プラットフォーム固有の構造]
```

**構造決定**: [DEFAULT to Option 1 unless Technical Context indicates web/mobile app]

## フェーズ 0: アウトライン & 研究
1. **上記の技術的コンテキストから不明点を抽出**:
   - 各 NEEDS CLARIFICATION → 研究タスク
   - 各依存関係 → ベストプラクティスタスク
   - 各統合 → パターンタスク

2. **研究エージェントを生成して派遣**:
   ```
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **発見を統合** `research.md` で以下の形式を使用:
   - 決定: [選択されたもの]
   - 根拠: [なぜ選択されたか]
   - 検討された代替案: [他に評価されたもの]

**出力**: すべての NEEDS CLARIFICATION が解決された research.md

## フェーズ 1: 設計 & 契約
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts from functional requirements**:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests from contracts**:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios from user stories**:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `/scripts/update-agent-context.sh [claude|gemini|copilot]` for your AI assistant
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## フェーズ 2: タスク計画アプローチ
*このセクションは /tasks コマンドが何をするかを記述 - /plan 中に実行しない*

**タスク生成戦略**:
- `/templates/tasks-template.md` をベースとしてロード
- フェーズ 1 設計ドキュメント (contracts, data model, quickstart) からタスクを生成
- 各契約 → 契約テストタスク [P]
- 各エンティティ → モデル作成タスク [P]
- 各ユーザーストーリー → 統合テストタスク
- テストを合格させるための実装タスク

**順序付け戦略**:
- TDD 順序: 実装前にテスト
- 依存関係順序: UI よりサービスよりモデル
- 並列実行のために [P] をマーク (独立ファイル)

**推定出力**: tasks.md の 25-30 の番号付き順序付きタスク

**重要**: このフェーズは /tasks コマンドによって実行, /plan によってではない

## フェーズ 3+: 将来の実装
*これらのフェーズは /plan コマンドのスコープを超える*

**Phase 3**: Task execution (/tasks command creates tasks.md)
**Phase 4**: Implementation (execute tasks.md following constitutional principles)
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## 複雑さ追跡
*憲法チェックに正当化が必要な違反がある場合のみ記入*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## 進捗追跡
*このチェックリストは実行フロー中に更新*

**Phase Status**:
- [ ] Phase 0: Research complete (/plan command)
- [ ] Phase 1: Design complete (/plan command)
- [ ] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [ ] Initial Constitution Check: PASS
- [ ] Post-Design Constitution Check: PASS
- [ ] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
