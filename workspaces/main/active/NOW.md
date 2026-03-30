# NOW.md — 当前最重要的一件事

> 每次会话开始前，先读此文件。

---

## 当前阶段：溪系统搭建 — 第 1 阶段

**最重要的下一步：**

### 🎯 验证 OpenClaw workspace 已切换到新路径

**为什么：**
系统搭建完了，但还没确认 OpenClaw 实际读取的是新 workspace（`~/srv/xi/workspaces/main/`）。
如果还在读旧路径（`~/.qclaw/workspace/`），整个新系统都不会生效。

**怎么做：**
在 OpenClaw 对话里问一句：
> "你在哪个 workspace 工作？"

如果回答包含 `/srv/xi/workspaces/main/` → 切换成功 ✅
如果回答包含 `.qclaw/workspace/` → 切换未生效，需要重启 Gateway

---

## 次级待办（排序列）

- [ ] 验证新 workspace 生效
- [ ] 创建第一个真实项目（rank.viewtrends.store 运营优化 / 溪系统运营）
- [ ] 把项目写入 `shared/projects/`
- [ ] 在 knowledge/ 里建立第一张 knowledge card
- [ ] 跑通第一次 Main → Research/Builder/Archivist 分派
- [ ] 整理第一份 daily memory

---

## 一句话原则

**先验证，再填内容，最后跑分派。别一次铺太多。**
