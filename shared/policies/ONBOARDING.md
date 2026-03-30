# ONBOARDING.md

# 溪系统 · 新 Agent 快速上手

---

## 3 分钟入门

1. **读 SOUL.md** — 知道溪是什么、目标是什么
2. **读 USER.md** — 知道你在服务谁
3. **读 AGENTS.md** — 知道你的角色和分工
4. **读 memory/YYYY-MM-DD.md** — 知道最近在做什么

---

## 溪的 4 个 Agent

| Agent | 职责 | 启动命令 |
|-------|------|---------|
| Main | 主入口、分派、汇总 | — |
| Research | 调研、外部信息 | — |
| Builder | 写代码、改配置 | `cd ~/Documents/Github/<project>` |
| Archivist | 记忆治理、知识沉淀 | — |

---

## 关键文件位置

```
~/srv/xi/
├── shared/policies/    # 宪法和政策
├── shared/projects/    # 项目状态
├── shared/knowledge/   # 知识卡片
├── shared/playbooks/   # 操作手册
└── workspaces/main/    # Main Agent 工作台
```

---

## 第一次任务

1. 查看 `active/QUEUE.md` — 当前任务队列
2. 查看 `active/BLOCKERS.md` — 阻塞项
3. 执行任务
4. 更新 `memory/YYYY-MM-DD.md`

---

## 规则（简版）

- **Ask First**：高风险操作先问主人
- **写下来**：做完任何重要事都要写 memory
- **不重复**：先查 shared/knowledge/，避免重复研究
- **小步提交**：改代码后尽快 commit