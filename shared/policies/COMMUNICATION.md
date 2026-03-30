# COMMUNICATION.md

# Agent 间通信协议

---

## 1. 通信原则

| 原则 | 说明 |
|------|------|
| Main 是唯一入口 | 所有外部任务经过 Main 再分派 |
| 子 Agent 不直接通信 | 子 Agent 之间不直接发消息，都通过 Main 中转 |
| 分派即授权 | 分派任务时，Main 授权子 Agent 可读取哪些文件 |

---

## 2. 分派消息格式

```markdown
## 任务
[简述目标]

## 上下文
[相关文件路径 + 关键信息]

## 输出要求
[格式 + 存放位置]

## 约束
[不做 + Ask First 项]
```

---

## 3. 消息类型

| 类型 | 触发 | 接收方 |
|------|------|--------|
| 分派任务 | Main Agent | Research / Builder / Archivist |
| 结果返回 | 子 Agent | Main Agent |
| 状态更新 | 子 Agent | Main Agent |
| 阻塞上报 | 子 Agent | Main Agent（立即，不等轮次） |

---

## 4. 阻塞上报规则

以下情况立即上报 Main：
- 缺少关键文件（路径不存在）
- 权限不足（文件不可读写）
- 发现高风险操作
- 外部依赖失败（API / SSH / DB）

**不等待轮次**：阻塞时立即发送，不累积。

---

## 5. 共享上下文

| 内容 | 位置 | 可读 |
|------|------|------|
| 宪法 / 政策 | `shared/policies/` | 所有 Agent |
| 项目状态 | `shared/projects/<name>/` | 所有 Agent |
| 知识卡片 | `shared/knowledge/cards/` | 所有 Agent |
| Playbooks | `shared/playbooks/` | 所有 Agent |
| Agent 私有 | `workspaces/<agent>/` | 仅该 Agent |

---

## 6. Ask First 清单

未经主人确认，子 Agent 不得：
- 删除 / 覆盖文件
- 发送外部请求（邮件 / API / 消息）
- 改 secrets / token
- 执行不可逆操作