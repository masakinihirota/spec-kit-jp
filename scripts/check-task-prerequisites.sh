#!/bin/bash
# 実装計画が存在するか確認し、オプションで設計ドキュメントを見つけるスクリプト
# 使用方法: ./check-task-prerequisites.sh [--json]

set -e

JSON_MODE=false
for arg in "$@"; do
    case "$arg" in
        --json) JSON_MODE=true ;;
        --help|-h) echo "使用方法: $0 [--json]"; exit 0 ;;
    esac
done

# 共通関数を読み込む
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# すべてのパスを取得
eval $(get_feature_paths)

# 機能ブランチにいるか確認
check_feature_branch "$CURRENT_BRANCH" || exit 1

# 機能ディレクトリが存在するか確認
if [[ ! -d "$FEATURE_DIR" ]]; then
    echo "エラー: 機能ディレクトリが見つかりません: $FEATURE_DIR"
    echo "最初に /specify を実行して、機能構造を作成してください。"
    exit 1
fi

# 実装計画が存在するか確認（必須）
if [[ ! -f "$IMPL_PLAN" ]]; then
    echo "エラー: $FEATURE_DIR に plan.md が見つかりません"
    echo "最初に /plan を実行して計画を作成してください。"
    exit 1
fi

if $JSON_MODE; then
    # 実際に存在する利用可能なドキュメントのJSON配列を作成
    docs=()
    [[ -f "$RESEARCH" ]] && docs+=("research.md")
    [[ -f "$DATA_MODEL" ]] && docs+=("data-model.md")
    ([[ -d "$CONTRACTS_DIR" ]] && [[ -n "$(ls -A "$CONTRACTS_DIR" 2>/dev/null)" ]]) && docs+=("contracts/")
    [[ -f "$QUICKSTART" ]] && docs+=("quickstart.md")
    # 配列をJSON形式に結合
    json_docs=$(printf '"%s",' "${docs[@]}")
    json_docs="[${json_docs%,}]"
    printf '{"FEATURE_DIR":"%s","AVAILABLE_DOCS":%s}\n' "$FEATURE_DIR" "$json_docs"
else
    # 利用可能な設計ドキュメントをリスト表示（オプション）
    echo "FEATURE_DIR:$FEATURE_DIR"
    echo "AVAILABLE_DOCS:"

    # 共通のチェック関数を使用
    check_file "$RESEARCH" "research.md"
    check_file "$DATA_MODEL" "data-model.md"
    check_dir "$CONTRACTS_DIR" "contracts/"
    check_file "$QUICKSTART" "quickstart.md"
fi

# 常に成功 - タスク生成は利用可能なドキュメントで動作する
