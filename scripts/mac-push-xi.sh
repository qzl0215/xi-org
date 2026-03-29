#!/bin/bash
# 溪组织资产自动 push 脚本 — Mac 端
# 从 ~/srv/xi/ push 到 GitHub xi-org
# cron: */10 * * * * （无 token 消耗，纯 git 操作）
# ============================================================

LOG_FILE="$HOME/.qclaw/logs/sync-xi.log"
mkdir -p "$(dirname "$LOG_FILE")"

cd "$HOME/srv/xi" || exit

# 检查是否有变更
if ! git diff --quiet || ! git diff --staged --quiet; then
    git add -A
    git commit -m "auto: $(date '+%Y-%m-%d %H:%M:%S')" 2>/dev/null
    git push origin main 2>/dev/null
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] pushed" >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] no change" >> "$LOG_FILE"
fi
