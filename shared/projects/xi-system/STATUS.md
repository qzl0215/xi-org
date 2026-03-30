# STATUS.md

# 溪系统 · 状态报告

> 更新时间：2026-03-30 19:24 GMT+8

---

## 系统状态

| 维度 | 状态 | 说明 |
|------|------|------|
| Workspace | ✅ 正常 | ~/.qclaw/workspace/，唯一 canonical，GitHub xi-org 同步 |
| 弃用路径 | ❌ | ~/srv/xi/ 已弃用，不再使用 |
| 4 Agent 分派 | ✅ 跑通 | Research → Builder → Archivist 链路验证 |
| Token 统计 | ✅ 建立 | ~/srv/xi/scripts/token-stats.py，每日 cron |
| 安全政策 | ✅ 补充 | SECURITY + INCIDENT + ONBOARDING |
| Listing Factory | ✅ Dev 运行 | http://127.0.0.1:3021 |
| 服务器基础设施 | ✅ 已部署 | 腾讯云 viewtrends-prod |
| Qdrant | ✅ 运行中 | 端口 6333，向量数据库已就绪 |
| LiteLLM | ✅ 运行中 | 端口 8000，MiniMax-M2.7-highspeed 已接入 |
| open-webui | ✅ 已安装 | 本地 Mac 端口 3000（独立 AI UI） |

---

## Token 累计（截至今日）

| 指标 | 数量 |
|------|------|
| 总输入 | 13,144,005 |
| 总输出 | 101,109 |
| 缓存读取 | 7,167,068 |
| 缓存写入 | 1,159,167 |
| **总计** | **21,571,349** |

---

## 技能安装建议

| 技能 | 优先级 | 理由 |
|------|--------|------|
| `github` | P0 | GitHub PR/issues 管理，日常工作流必需 |
| `webapp-testing` | P1 | 前端验证，溪需验证页面改动 |
| 其他 | 暂不安装 | 极简主义 |

**代码执行策略**：Codex/Claude Code 负责写代码，溪负责 orchestration + 治理。不重复造轮子。

---

## 本周进展

- [x] P0 安全政策（SECURITY + INCIDENT + ONBOARDING）
- [x] P1 token 统计自动化
- [x] 4 Agent 分派流程验证
- [x] listing_factory dev server 重启
- [ ] ONBOARDING 完成

---

## 下一步

### P0（立即）
1. 商家知识库 500 篇导入 Qdrant（向量数据库已就绪）
2. listing_factory M1 Demo 验收

### P1（本週）
3. 安装 `github` skill
4. LiteLLM 路由配置（多模型自动路由，省 token）

### P2（按需）
5. ONBOARDING 完成
6. open-webui × 溪的桥接方案研究