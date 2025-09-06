#!/bin/bash
# 新しい機能計画に基づいてエージェントコンテキストファイルを段階的に更新
# サポート: CLAUDE.md, GEMINI.md, .github/copilot-instructions.md
# O(1) 操作 - 現在のコンテキストファイルと新しい plan.md のみを読み取る

set -e

REPO_ROOT=$(git rev-parse --show-toplevel)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
FEATURE_DIR="$REPO_ROOT/specs/$CURRENT_BRANCH"
NEW_PLAN="$FEATURE_DIR/plan.md"

# 更新するエージェントコンテキストファイルを決定
CLAUDE_FILE="$REPO_ROOT/CLAUDE.md"
GEMINI_FILE="$REPO_ROOT/GEMINI.md"
COPILOT_FILE="$REPO_ROOT/.github/copilot-instructions.md"

# 引数によるオーバーライドを許可
AGENT_TYPE="$1"

if [ ! -f "$NEW_PLAN" ]; then
    echo "ERROR: No plan.md found at $NEW_PLAN"
    exit 1
fi

echo "=== Updating agent context files for feature $CURRENT_BRANCH ==="

# 新しい計画から技術を抽出
NEW_LANG=$(grep "^**Language/Version**: " "$NEW_PLAN" 2>/dev/null | head -1 | sed 's/^**Language\/Version**: //' | grep -v "NEEDS CLARIFICATION" || echo "")
NEW_FRAMEWORK=$(grep "^**Primary Dependencies**: " "$NEW_PLAN" 2>/dev/null | head -1 | sed 's/^**Primary Dependencies**: //' | grep -v "NEEDS CLARIFICATION" || echo "")
NEW_TESTING=$(grep "^**Testing**: " "$NEW_PLAN" 2>/dev/null | head -1 | sed 's/^**Testing**: //' | grep -v "NEEDS CLARIFICATION" || echo "")
NEW_DB=$(grep "^**Storage**: " "$NEW_PLAN" 2>/dev/null | head -1 | sed 's/^**Storage**: //' | grep -v "N/A" | grep -v "NEEDS CLARIFICATION" || echo "")
NEW_PROJECT_TYPE=$(grep "^**Project Type**: " "$NEW_PLAN" 2>/dev/null | head -1 | sed 's/^**Project Type**: //' || echo "")

# 単一のエージェントコンテキストファイルを更新する関数
update_agent_file() {
    local target_file="$1"
    local agent_name="$2"

    echo "Updating $agent_name context file: $target_file"

    # 新しいコンテキスト用のテンプファイルを作成
    local temp_file=$(mktemp)

    # ファイルが存在しない場合、テンプレートから作成
    if [ ! -f "$target_file" ]; then
        echo "Creating new $agent_name context file..."

        # これが SDD リポジトリ自体かどうかをチェック
        if [ -f "$REPO_ROOT/templates/agent-file-template.md" ]; then
            cp "$REPO_ROOT/templates/agent-file-template.md" "$temp_file"
        else
            echo "ERROR: Template not found at $REPO_ROOT/templates/agent-file-template.md"
            return 1
        fi

        # プレースホルダーを置き換え
        sed -i.bak "s/\[PROJECT NAME\]/$(basename $REPO_ROOT)/" "$temp_file"
        sed -i.bak "s/\[DATE\]/$(date +%Y-%m-%d)/" "$temp_file"
        sed -i.bak "s/\[EXTRACTED FROM ALL PLAN.MD FILES\]/- $NEW_LANG + $NEW_FRAMEWORK ($CURRENT_BRANCH)/" "$temp_file"

        # タイプに基づいてプロジェクト構造を追加
        if [[ "$NEW_PROJECT_TYPE" == *"web"* ]]; then
            sed -i.bak "s|\[ACTUAL STRUCTURE FROM PLANS\]|backend/\nfrontend/\ntests/|" "$temp_file"
        else
            sed -i.bak "s|\[ACTUAL STRUCTURE FROM PLANS\]|src/\ntests/|" "$temp_file"
        fi

        # 最小限のコマンドを追加
        if [[ "$NEW_LANG" == *"Python"* ]]; then
            COMMANDS="cd src && pytest && ruff check ."
        elif [[ "$NEW_LANG" == *"Rust"* ]]; then
            COMMANDS="cargo test && cargo clippy"
        elif [[ "$NEW_LANG" == *"JavaScript"* ]] || [[ "$NEW_LANG" == *"TypeScript"* ]]; then
            COMMANDS="npm test && npm run lint"
        else
            COMMANDS="# Add commands for $NEW_LANG"
        fi
        sed -i.bak "s|\[ONLY COMMANDS FOR ACTIVE TECHNOLOGIES\]|$COMMANDS|" "$temp_file"

        # コードスタイルを追加
        sed -i.bak "s|\[LANGUAGE-SPECIFIC, ONLY FOR LANGUAGES IN USE\]|$NEW_LANG: Follow standard conventions|" "$temp_file"

        # 最近の変更を追加
        sed -i.bak "s|\[LAST 3 FEATURES AND WHAT THEY ADDED\]|- $CURRENT_BRANCH: Added $NEW_LANG + $NEW_FRAMEWORK|" "$temp_file"

        rm "$temp_file.bak"
    else
        echo "既存の $agent_name コンテキストファイルを更新中..."

        # 手動追加を抽出
        local manual_start=$(grep -n "<!-- MANUAL ADDITIONS START -->" "$target_file" | cut -d: -f1)
        local manual_end=$(grep -n "<!-- MANUAL ADDITIONS END -->" "$target_file" | cut -d: -f1)

        if [ ! -z "$manual_start" ] && [ ! -z "$manual_end" ]; then
            sed -n "${manual_start},${manual_end}p" "$target_file" > /tmp/manual_additions.txt
        fi

        # 既存ファイルを解析して更新バージョンを作成
        python3 - << EOF
import re
import sys
from datetime import datetime

# 既存ファイルを読み取る
with open("$target_file", 'r') as f:
    content = f.read()

# 新しい技術が既に存在するかをチェック
tech_section = re.search(r'## Active Technologies\n(.*?)\n\n', content, re.DOTALL)
if tech_section:
    existing_tech = tech_section.group(1)

    # まだ存在しない場合、新しい技術を追加
    new_additions = []
    if "$NEW_LANG" and "$NEW_LANG" not in existing_tech:
        new_additions.append(f"- $NEW_LANG + $NEW_FRAMEWORK ($CURRENT_BRANCH)")
    if "$NEW_DB" and "$NEW_DB" not in existing_tech and "$NEW_DB" != "N/A":
        new_additions.append(f"- $NEW_DB ($CURRENT_BRANCH)")

    if new_additions:
        updated_tech = existing_tech + "\n" + "\n".join(new_additions)
        content = content.replace(tech_section.group(0), f"## Active Technologies\n{updated_tech}\n\n")

# 必要に応じてプロジェクト構造を更新
if "$NEW_PROJECT_TYPE" == "web" and "frontend/" not in content:
    struct_section = re.search(r'## Project Structure\n\`\`\`\n(.*?)\n\`\`\`', content, re.DOTALL)
    if struct_section:
        updated_struct = struct_section.group(1) + "\nfrontend/src/      # Web UI"
        content = re.sub(r'(## Project Structure\n\`\`\`\n).*?(\n\`\`\`)',
                        f'\\1{updated_struct}\\2', content, flags=re.DOTALL)

# 言語が新しい場合、新しいコマンドを追加
if "$NEW_LANG" and f"# {NEW_LANG}" not in content:
    commands_section = re.search(r'## Commands\n\`\`\`bash\n(.*?)\n\`\`\`', content, re.DOTALL)
    if not commands_section:
        commands_section = re.search(r'## Commands\n(.*?)\n\n', content, re.DOTALL)

    if commands_section:
        new_commands = commands_section.group(1)
        if "Python" in "$NEW_LANG":
            new_commands += "\ncd src && pytest && ruff check ."
        elif "Rust" in "$NEW_LANG":
            new_commands += "\ncargo test && cargo clippy"
        elif "JavaScript" in "$NEW_LANG" or "TypeScript" in "$NEW_LANG":
            new_commands += "\nnpm test && npm run lint"

        if "```bash" in content:
            content = re.sub(r'(## Commands\n\`\`\`bash\n).*?(\n\`\`\`)',
                            f'\\1{new_commands}\\2', content, flags=re.DOTALL)
        else:
            content = re.sub(r'(## Commands\n).*?(\n\n)',
                            f'\\1{new_commands}\\2', content, flags=re.DOTALL)

# 最近の変更を更新（最後の3つだけ保持）
changes_section = re.search(r'## Recent Changes\n(.*?)(\n\n|$)', content, re.DOTALL)
if changes_section:
    changes = changes_section.group(1).strip().split('\n')
    changes.insert(0, f"- $CURRENT_BRANCH: Added $NEW_LANG + $NEW_FRAMEWORK")
    # Keep only last 3
    changes = changes[:3]
    content = re.sub(r'(## Recent Changes\n).*?(\n\n|$)',
                    f'\\1{chr(10).join(changes)}\\2', content, flags=re.DOTALL)

# 日付を更新
content = re.sub(r'Last updated: \d{4}-\d{2}-\d{2}',
                f'Last updated: {datetime.now().strftime("%Y-%m-%d")}', content)

# テンプファイルに書き込む
with open("$temp_file", 'w') as f:
    f.write(content)
EOF

        # 手動追加を復元（存在する場合）
        if [ -f /tmp/manual_additions.txt ]; then
            # テンプファイルから古い手動セクションを削除
            sed -i.bak '/<!-- MANUAL ADDITIONS START -->/,/<!-- MANUAL ADDITIONS END -->/d' "$temp_file"
            # 手動追加を追加
            cat /tmp/manual_additions.txt >> "$temp_file"
            rm /tmp/manual_additions.txt "$temp_file.bak"
        fi
    fi

    # テンプファイルを最終位置に移動
    mv "$temp_file" "$target_file"
    echo "✅ $agent_name context file updated successfully"
}

# 引数または既存ファイルの検出に基づいてファイルを更新
case "$AGENT_TYPE" in
    "claude")
        update_agent_file "$CLAUDE_FILE" "Claude Code"
        ;;
    "gemini")
        update_agent_file "$GEMINI_FILE" "Gemini CLI"
        ;;
    "copilot")
        update_agent_file "$COPILOT_FILE" "GitHub Copilot"
        ;;
    "")
        # Update all existing files
        [ -f "$CLAUDE_FILE" ] && update_agent_file "$CLAUDE_FILE" "Claude Code"
        [ -f "$GEMINI_FILE" ] && update_agent_file "$GEMINI_FILE" "Gemini CLI"
        [ -f "$COPILOT_FILE" ] && update_agent_file "$COPILOT_FILE" "GitHub Copilot"

                    # ファイルが存在しない場合、現在のディレクトリに基づいて作成するかユーザーに尋ねる
        if [ ! -f "$CLAUDE_FILE" ] && [ ! -f "$GEMINI_FILE" ] && [ ! -f "$COPILOT_FILE" ]; then
            echo "No agent context files found. Creating Claude Code context file by default."
            update_agent_file "$CLAUDE_FILE" "Claude Code"
        fi
        ;;
    *)
        echo "ERROR: Unknown agent type '$AGENT_TYPE'. Use: claude, gemini, copilot, or leave empty for all."
        exit 1
        ;;
esac
echo ""
echo "Summary of changes:"
if [ ! -z "$NEW_LANG" ]; then
    echo "- Added language: $NEW_LANG"
fi
if [ ! -z "$NEW_FRAMEWORK" ]; then
    echo "- Added framework: $NEW_FRAMEWORK"
fi
if [ ! -z "$NEW_DB" ] && [ "$NEW_DB" != "N/A" ]; then
    echo "- Added database: $NEW_DB"
fi

echo ""
echo "Usage: $0 [claude|gemini|copilot]"
echo "  - No argument: Update all existing agent context files"
echo "  - claude: Update only CLAUDE.md"
echo "  - gemini: Update only GEMINI.md"
echo "  - copilot: Update only .github/copilot-instructions.md"
