# DECISIONS.md

# 溪系统 · 决策记录

---

## 记忆漂移问题 — 复盘

**问题**：Token 成本记录不连续，每次子任务没有独立统计。

**根因**：
- 没有在每次子任务完成后立即写 memory
- 依赖"事后查脚本"而不是"实时记录"
- AGENTS.md 里没有明确规定"每次操作后必须记录 cost"

**修复方案**：
1. 每次分派任务后，立即在 DECISIONS.md 追加 cost 记录
2. Token 统计写入 `~/srv/xi/shared/reports/token-usage.json`（已自动化）
3. 在 AGENTS.md 加入 cost tracking 要求

---

## Token 成本记录（实时）

| 日期 | 任务 | Agent | 输入 | 输出 | 合计 | Runtime |
|------|------|-------|------|------|------|---------|
| 2026-03-30 | 4A 分派验证 | Research | 31.1k | 3.7k | 34.8k | 1m21s |
| 2026-03-30 | 4A 分派验证 | Archivist | 22.7k | 1.6k | 24.3k | 44s |
| 2026-03-30 | listing_factory 分析 | Builder | 208.3k | 1.4k | 209.7k | 2m12s |
| 2026-03-30 | listing_factory dev 重启 | Main | ~5k | ~2k | ~7k | ~5min |
| 2026-03-30 | Mac 诊断 | Main | ~1k | ~0.5k | ~1.5k | ~2min |
| 2026-03-30 | 政策文件写入 | Main | ~5k | ~2k | ~7k | ~3min |
| 2026-03-30 | rank.viewtrends 诊断 | Main | ~3k | ~1k | ~4k | ~10min |
| 2026-03-30 | 增量更新分析 | Main | ~3k | ~1k | ~4k | ~3min |

---

## task-018 问题记录

**现象**：Serper 步骤被 skip（`user_requested_skip_pending_task_018`）

**当时情况**：pipeline 跑到 task-018 时卡住，人工选择 skip 跳过

**根因**：待查（需要看当时的 collab foreman log 或 run_summary）

**后续动作**：
- [ ] 找到 task-018 的定义（在 collab foreman 系统里）
- [ ] 确认是人工决策点还是 bug
- [ ] 修复卡住原因

---

## 系统决策

| 日期 | 决策 | 理由 |
|------|------|------|
| 2026-03-30 | workspace 切换到 ~/srv/xi/ | Mac 作为写入端，服务器只读同步 |
| 2026-03-30 | 代码执行由 Codex 负责 | OpenClaw 做 orchestration，不重复造轮子 |
| 2026-03-30 | 不安装不必要的 skill | 极简主义 |

---

*最后更新：2026-03-30 05:53 GMT+8*