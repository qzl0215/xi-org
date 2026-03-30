# MEMORY.md

# 溪 — 长期记忆

> 本文件是 Main Agent 的精选长期记忆。
> 由 Archivist Agent 维护，Main Agent 在每次主私聊 session 加载。
> 写入规则见 MEMORY_POLICY.md。

---

## 主人长期目标

- 建立以品牌排行（rank.viewtrends.store）为核心的可运营业务
- 建设多 Agent 组织体系，提高长期执行效率
- 用 AI + 系统沉淀真实、可验证的经济价值

---

## 主人稳定偏好（高置信度）

- 真实可验证 > 听起来好听
- 长期复利 > 短期爽感
- 简洁 > 复杂（除非有明确理由）
- 直接说结论，再给理由
- 不经确认不执行高风险操作

---

## 重要项目脉络

| 项目 | 状态 | 说明 |
|------|------|------|
| rank.viewtrends.store | 进行中 | 品牌排行业务，主站 |
| 溪多 Agent 组织 | 建设中 | 正在搭建 Main/Research/Builder/Archivist 分工 |

---

## 已验证规则

- （待 Archivist 从历史中提炼补充）

---

## 历史纠偏（已纠正的错误理解）

- （待补充）

---

## 架构决策记录

### 2026-03-30：workspace 合并
- `~/.qclaw/workspace/` 是溪唯一 canonical workspace，已与 GitHub xi-org 同步
- `~/srv/xi/` 完全弃用，不再使用
- 合并后结构：根目录保留溪核心文件（SOUL.md、AGENTS.md 等），workspaces/main/ 是主 workspace，shared/ 是共享资产

### 2026-03-30：服务器基础设施部署
- 服务器：viewtrends-prod（43.160.239.62），腾讯云轻量应用服务器，SSH 配置在 ~/.ssh/config，OpenClaw 已预装
- Qdrant（向量数据库）：运行中，端口 6333（Dashboard: http://43.160.239.62:6333/dashboard）
- LiteLLM（模型代理）：运行中，pip 安装（版本 1.82.6），端口 8000，已接入 MiniMax-M2.7-highspeed
- MiniMax API base: https://api.minimaxi.com/v1
- 待办：阿里云安全组开放 8000、6333 端口
- 待办：open-webui 本地安装（镜像 6GB，拉取中）

---

## 待办记录

### 基础设施
- [x] 腾讯云安全组：开放 8000（LiteLLM）、6333（Qdrant）入方向 TCP
- [x] 验证外网访问 LiteLLM（8000 端口开完后）
- [x] open-webui 本地安装（镜像拉取中，完成后启动）

### 商家知识库子项目
- [ ] 500 篇商品内容导入 Qdrant
- [ ] 知识库应用层开发（基于 Qdrant API）

### 模型层
- [ ] LiteLLM 自动路由配置（简单任务路由到便宜模型，省 token）
- [ ] 如果需要 Azure 模型接入，补全 Azure API key

---

## 最后更新

- 2026-03-30
