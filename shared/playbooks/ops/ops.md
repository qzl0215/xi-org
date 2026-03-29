# ops.md

# Playbook: Archivist Agent 工作手册

> 从 role.md 提炼，用于快速参考。

---

## 标准流程

1. 收集原材料（daily logs / 历史记录 / 项目状态）
2. 去重、分组、压缩
3. 判断归属：临时 / 阶段 / 长期 / 知识卡 / canon
4. 写入对应位置
5. 更新 registry（替代/冲突关系）

---

## 记忆规则

- 不把原始聊天大段复制进长期记忆
- 不把单次表达写成永久偏好
- 带时间维度
- 区分事实 vs 推断

---

## 输出位置

- daily memory → `memory/YYYY-MM-DD.md`
- 长期记忆 → `MEMORY.md`
- 知识卡 → `shared/knowledge/cards/`
- 标准答案 → `shared/knowledge/canon/`