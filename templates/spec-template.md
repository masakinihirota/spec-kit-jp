# 機能仕様: [FEATURE NAME]

**機能ブランチ**: `[###-feature-name]`
**作成日**: [DATE]
**ステータス**: 下書き
**入力**: ユーザー説明: "$ARGUMENTS"

## 実行フロー (メイン)
```
1. 入力からユーザー説明を解析
   → 空の場合: ERROR "機能説明が提供されていません"
2. 説明から主要概念を抽出
   → 識別: アクター, アクション, データ, 制約
3. 各不明瞭な側面について:
   → [NEEDS CLARIFICATION: 具体的な質問] でマーク
4. ユーザーシナリオ & テストセクションを埋める
   → 明確なユーザーフローがない場合: ERROR "ユーザーシナリオを決定できません"
5. 機能要件を生成
   → 各要件はテスト可能でなければならない
   → 曖昧な要件をマーク
6. 主要エンティティを識別 (データが関与する場合)
7. レビューチェックリストを実行
   → [NEEDS CLARIFICATION] がある場合: WARN "仕様に不確実性があります"
   → 実装詳細が見つかった場合: ERROR "技術詳細を削除"
8. 戻る: SUCCESS (計画の準備が整った仕様)
```

---

## ⚡ クイックガイドライン
- ✅ ユーザーが何を必要とし、なぜかを焦点に
- ❌ どのように実装するかを避ける (技術スタック, API, コード構造なし)
- 👥 開発者ではなくビジネスステークホルダー向けに書く

### セクション要件
- **必須セクション**: すべての機能で完了する必要がある
- **オプションセクション**: 機能に関連する場合のみ含める
- セクションが適用されない場合、完全に削除する ("N/A" のままにしない)

### AI 生成用
ユーザープロンプトからこの仕様を作成する場合:
1. **すべての曖昧さをマーク**: 作成する必要がある仮定に対して [NEEDS CLARIFICATION: 具体的な質問] を使用
2. **推測しない**: プロンプトが何かを指定していない場合 (例: 認証方法なしの "ログインシステム")、マークする
3. **テスターのように考える**: すべての曖昧な要件は "テスト可能で曖昧でない" チェックリスト項目に失敗するべき
4. **一般的な未指定領域**:
   - ユーザータイプと権限
   - データ保持/削除ポリシー
   - パフォーマンスターゲットとスケール
   - エラーハンドリング動作
   - 統合要件
   - セキュリティ/コンプライアンスニーズ

---

## ユーザーシナリオ & テスト *(必須)*

### 主要ユーザーストーリー
[Describe the main user journey in plain language]

### 受け入れシナリオ
1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

### エッジケース
- [boundary condition] の場合、何が起こるか?
- システムは [error scenario] をどのように処理するか?

## 要件 *(必須)*

### 機能要件
- **FR-001**: システムは [specific capability, e.g., "allow users to create accounts"] しなければならない
- **FR-002**: システムは [specific capability, e.g., "validate email addresses"] しなければならない
- **FR-003**: ユーザーは [key interaction, e.g., "reset their password"] ことができる必要がある
- **FR-004**: システムは [data requirement, e.g., "persist user preferences"] しなければならない
- **FR-005**: システムは [behavior, e.g., "log all security events"] しなければならない

*曖昧な要件をマークする例:*
- **FR-006**: システムは [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?] 経由でユーザーを認証しなければならない
- **FR-007**: システムは [NEEDS CLARIFICATION: retention period not specified] の間ユーザーデータを保持しなければならない

### 主要エンティティ *(機能がデータに関与する場合含める)*
- **[Entity 1]**: [What it represents, key attributes without implementation]
- **[Entity 2]**: [What it represents, relationships to other entities]

---

## レビュー & 受け入れチェックリスト
*ゲート: main() 実行中に自動チェックが実行*

### コンテンツ品質
- [ ] 実装詳細なし (言語, フレームワーク, API)
- [ ] ユーザー価値とビジネスニーズに焦点
- [ ] 非技術的ステークホルダー向けに書く
- [ ] すべての必須セクションが完了

### 要件完全性
- [ ] [NEEDS CLARIFICATION] マーカーが残っていない
- [ ] 要件はテスト可能で曖昧でない
- [ ] 成功基準は測定可能
- [ ] 範囲は明確に境界付けられている
- [ ] 依存関係と仮定が識別されている

---

## 実行ステータス
*処理中に main() によって更新*

- [ ] ユーザー説明が解析された
- [ ] 主要概念が抽出された
- [ ] 曖昧さがマークされた
- [ ] ユーザーシナリオが定義された
- [ ] 要件が生成された
- [ ] エンティティが識別された
- [ ] レビューチェックリストが合格

---
