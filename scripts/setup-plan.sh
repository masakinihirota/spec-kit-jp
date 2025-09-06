#!/bin/bash
# 現在のブランチの実装計画構造を設定
# 実装計画生成に必要なパスを返す
# 使用法: ./setup-plan.sh [--json]

set -e

JSON_MODE=false
for arg in "$@"; do
    case "$arg" in
        --json) JSON_MODE=true ;;
        --help|-h) echo "Usage: $0 [--json]"; exit 0 ;;
    esac
done

# 共通関数をソース
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# すべてのパスを取得
eval $(get_feature_paths)

# 機能ブランチ上かどうかをチェック
check_feature_branch "$CURRENT_BRANCH" || exit 1

# specs ディレクトリが存在しない場合作成
mkdir -p "$FEATURE_DIR"

# 計画テンプレートが存在する場合、コピー
TEMPLATE="$REPO_ROOT/templates/plan-template.md"
if [ -f "$TEMPLATE" ]; then
    cp "$TEMPLATE" "$IMPL_PLAN"
fi

if $JSON_MODE; then
    printf '{"FEATURE_SPEC":"%s","IMPL_PLAN":"%s","SPECS_DIR":"%s","BRANCH":"%s"}\n' \
        "$FEATURE_SPEC" "$IMPL_PLAN" "$FEATURE_DIR" "$CURRENT_BRANCH"
else
    # LLM 使用のためのすべてのパスを出力
    echo "FEATURE_SPEC: $FEATURE_SPEC"
    echo "IMPL_PLAN: $IMPL_PLAN"
    echo "SPECS_DIR: $FEATURE_DIR"
    echo "BRANCH: $CURRENT_BRANCH"
fi
