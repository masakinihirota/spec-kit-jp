#!/bin/bash
# すべてのスクリプトの共通関数と変数

# リポジトリルートを取得
get_repo_root() {
    git rev-parse --show-toplevel
}

# 現在のブランチを取得
get_current_branch() {
    git rev-parse --abbrev-ref HEAD
}

# 現在のブランチが機能ブランチかどうかをチェック
# Returns 0 if valid, 1 if not
check_feature_branch() {
    local branch="$1"
    if [[ ! "$branch" =~ ^[0-9]{3}- ]]; then
        echo "ERROR: Not on a feature branch. Current branch: $branch"
        echo "Feature branches should be named like: 001-feature-name"
        return 1
    fi
    return 0
}

# 機能ディレクトリパスを取得
get_feature_dir() {
    local repo_root="$1"
    local branch="$2"
    echo "$repo_root/specs/$branch"
}

# 機能のすべての標準パスを取得
# Usage: eval $(get_feature_paths)
# Sets: REPO_ROOT, CURRENT_BRANCH, FEATURE_DIR, FEATURE_SPEC, IMPL_PLAN, TASKS
get_feature_paths() {
    local repo_root=$(get_repo_root)
    local current_branch=$(get_current_branch)
    local feature_dir=$(get_feature_dir "$repo_root" "$current_branch")

    echo "REPO_ROOT='$repo_root'"
    echo "CURRENT_BRANCH='$current_branch'"
    echo "FEATURE_DIR='$feature_dir'"
    echo "FEATURE_SPEC='$feature_dir/spec.md'"
    echo "IMPL_PLAN='$feature_dir/plan.md'"
    echo "TASKS='$feature_dir/tasks.md'"
    echo "RESEARCH='$feature_dir/research.md'"
    echo "DATA_MODEL='$feature_dir/data-model.md'"
    echo "QUICKSTART='$feature_dir/quickstart.md'"
    echo "CONTRACTS_DIR='$feature_dir/contracts'"
}

# ファイルが存在するかどうかをチェックして報告
check_file() {
    local file="$1"
    local description="$2"
    if [[ -f "$file" ]]; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}

# ディレクトリが存在し、ファイルがあるかどうかをチェック
check_dir() {
    local dir="$1"
    local description="$2"
    if [[ -d "$dir" ]] && [[ -n "$(ls -A "$dir" 2>/dev/null)" ]]; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}
