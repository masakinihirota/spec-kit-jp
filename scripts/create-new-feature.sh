#!/bin/bash
# 新しい機能にブランチ、ディレクトリ構造、テンプレートを作成
# 使用法: ./create-new-feature.sh "機能説明"
#        ./create-new-feature.sh --json "機能説明"

set -e

JSON_MODE=false

# フラグ以外の引数を収集
ARGS=()
for arg in "$@"; do
    case "$arg" in
        --json)
            JSON_MODE=true
            ;;
        --help|-h)
            echo "Usage: $0 [--json] <feature_description>"; exit 0 ;;
        *)
            ARGS+=("$arg") ;;
    esac
done

FEATURE_DESCRIPTION="${ARGS[*]}"
if [ -z "$FEATURE_DESCRIPTION" ]; then
        echo "Usage: $0 [--json] <feature_description>" >&2
        exit 1
fi

# リポジトリルートを取得
REPO_ROOT=$(git rev-parse --show-toplevel)
SPECS_DIR="$REPO_ROOT/specs"

# specs ディレクトリが存在しない場合作成
mkdir -p "$SPECS_DIR"

# 最も番号の高い機能ディレクトリを見つける
HIGHEST=0
if [ -d "$SPECS_DIR" ]; then
    for dir in "$SPECS_DIR"/*; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            number=$(echo "$dirname" | grep -o '^[0-9]\+' || echo "0")
            number=$((10#$number))
            if [ "$number" -gt "$HIGHEST" ]; then
                HIGHEST=$number
            fi
        fi
    done
fi

# ゼロパディングで次の機能番号を生成
NEXT=$((HIGHEST + 1))
FEATURE_NUM=$(printf "%03d" "$NEXT")

# 説明からブランチ名を作成
BRANCH_NAME=$(echo "$FEATURE_DESCRIPTION" | \
    tr '[:upper:]' '[:lower:]' | \
    sed 's/[^a-z0-9]/-/g' | \
    sed 's/-\+/-/g' | \
    sed 's/^-//' | \
    sed 's/-$//')

# 2-3 つの意味のある単語を抽出
WORDS=$(echo "$BRANCH_NAME" | tr '-' '\n' | grep -v '^$' | head -3 | tr '\n' '-' | sed 's/-$//')

# 最終ブランチ名
BRANCH_NAME="${FEATURE_NUM}-${WORDS}"

# 新しいブランチを作成して切り替え
git checkout -b "$BRANCH_NAME"

# 機能ディレクトリを作成
FEATURE_DIR="$SPECS_DIR/$BRANCH_NAME"
mkdir -p "$FEATURE_DIR"

# テンプレートが存在する場合、コピー
TEMPLATE="$REPO_ROOT/templates/spec-template.md"
SPEC_FILE="$FEATURE_DIR/spec.md"

if [ -f "$TEMPLATE" ]; then
    cp "$TEMPLATE" "$SPEC_FILE"
else
    echo "Warning: Template not found at $TEMPLATE" >&2
    touch "$SPEC_FILE"
fi

if $JSON_MODE; then
    printf '{"BRANCH_NAME":"%s","SPEC_FILE":"%s","FEATURE_NUM":"%s"}\n' \
        "$BRANCH_NAME" "$SPEC_FILE" "$FEATURE_NUM"
else
    # Output results for the LLM to use (legacy key: value format)
    echo "BRANCH_NAME: $BRANCH_NAME"
    echo "SPEC_FILE: $SPEC_FILE"
    echo "FEATURE_NUM: $FEATURE_NUM"
fi
