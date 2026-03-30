# SESSION-STATE.md

# 当前会话状态

> WAL Protocol：关键信息先写这里，再回复。

---

## 当前任务

| 任务 | 状态 | 开始时间 |
|------|------|---------|
| DeerFlow 部署（服务器） | ✅ 完成 | 2026-03-30 09:00 |
| DeerFlow Mac 本地（树） | ✅ 完成 | 2026-03-30 14:00 |

---

## 当前项目上下文

### DeerFlow 部署（云行 = 影）

**服务器 DeerFlow（影）**：
- 位置：`/root/apps/deer-flow/`
- **Web UI（正式）：https://deerflow.viewtrends.store/**
- 内部端口：2026（已绑定域名，跳过安全组）
- API 端口：8001（内部）、2024（LangGraph）
- 状态：✅ 运行中（4 容器）

**配置**：
- 模型：DeepSeek-V3（复用 ranking_app 的火山引擎 API）
- API Key：`$VOLCANO_API_KEY`（已配置）
- Config：`/root/apps/deer-flow/config.yaml`

**Docker 容器**：
- deer-flow-nginx（端口 2026）
- deer-flow-gateway（端口 8001）
- deer-flow-langgraph（端口 2024）
- deer-flow-frontend（端口 3000）

### Mac DeerFlow（树）

- 状态：✅ 已部署
- 位置：`~/Documents/Github/deer-flow/`
- Frontend：http://127.0.0.1:3030
- Gateway：http://127.0.0.1:8001
- 启动脚本：`~/Documents/Github/deer-flow/start-deer-flow-mac.sh`
- 配置：MiniMax-M2.7-Highspeed（与影相同）
- 备注：仅 Mac 本地访问，不可公网访问

### listing_factory
- **阶段**: Phase A（页面定型）
- **阻塞**: Codex 在写代码，暂不动
- **Dev server**: http://127.0.0.1:3021 ✅ 运行中

### rank.viewtrends.store
- **问题**: S4 (Product Vector) OOM killed
- **原因**: Docker 容器内存 1GB 不足
- **状态**: 暂停，等主人指令

---

## Agent 命名

| Agent | 名字 | 职责 |
|-------|------|------|
| Main | 溪 | 主入口、编排、交付 |
| Research | 风 | 调研、搜索、分析 |
| Builder | 草 | 写代码、改配置 |
| Archivist | 梦 | 记忆治理、知识沉淀 |
| DeerFlow-A（Mac） | 树 | 本地任务执行 |
| DeerFlow-B（Server） | 影 | 主力任务执行 |

---

## 今日关键决策

- DeerFlow 定位：溪的外部执行引擎（不是竞争者）
- 架构：溪作为主脑，DeerFlow 作为执行力强的个体
- 调度：Mac 在线 → 调用树；Mac 离线 → 调用影
- task-018 跳过是主人主动忽略，非 bug

---

## 待主人确认

- [ ] Mac DeerFlow（树）部署 — 需要 Mac 安装 Docker
- [ ] DeerFlow Skills 迁移评估
- [ ] 共享日志方案确认

---

## 偏好记录（来自 WAL）

- 主人要求：token 成本实时记录
- 主人要求：不主动碰 listing_factory 和 rank 两个项目
- 主人要求：溪+DeerFlow 作为组合，不是替代关系

---

*最后更新: 2026-03-30 22:59 GMT+8（深夜，溪待机）*