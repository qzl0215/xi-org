#!/bin/bash
# 溪组织资产同步脚本 — 服务器端
# 从 GitHub xi-org 拉取最新组织资产
# cron: */10 * * * *

cd /srv/xi || exit
git fetch origin
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main 2>/dev/null || echo "")
if [ "$LOCAL" != "$REMOTE" ] && [ -n "$REMOTE" ]; then
    git pull origin main --no-edit
fi
