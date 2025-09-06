#!/bin/bash
# 既存の機能ファイルを見つけるための現在の機能ブランチのパスを取得
# 既存の機能ファイルを必要とするコマンドで使用

set -e

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# すべてのパスを取得
eval $(get_feature_paths)

# 機能ブランチ上かどうかをチェック
check_feature_branch "$CURRENT_BRANCH" || exit 1

# パスを出力（何も作成しない）
echo "REPO_ROOT: $REPO_ROOT"
echo "BRANCH: $CURRENT_BRANCH"
echo "FEATURE_DIR: $FEATURE_DIR"
echo "FEATURE_SPEC: $FEATURE_SPEC"
echo "IMPL_PLAN: $IMPL_PLAN"
echo "TASKS: $TASKS"
