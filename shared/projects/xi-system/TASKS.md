# TASKS.md

# 任务：跑通 4 Agent 分派 + 实际 token 成本记录

> 第一次完整分派任务。
> 核心目的：验证分派流程可跑通，并记录实际 token 消耗用于复盘优化。

---

## 任务主题

**分析"溪系统"当前的文件结构与工作流，识别优化机会，给出分阶段 token 成本优化建议。**

---

## 分派流程

### 阶段 1：Main Agent 接收并分派

**Main 做**：
- 理解真实目标
- 分派给 Research

**分派完成后记录**：
- Main 本次输入 tokens（历史上下文）
- Main 本次输出 tokens（分派指令）

---

### 阶段 2：Research Agent 调研

**Research 做**：
- 检查 workspace 目录结构
- 对比 OpenClaw 官方推荐实践
- 输出调研 memo（含优先级建议）

**完成后记录**：
- Research 输入 tokens
- Research 输出 tokens

---

### 阶段 3：Archivist Agent 整理

**Archivist 做**：
- 分析本次分派的 token 成本分布
- 提出优化建议
- 更新 token 使用日志

**完成后记录**：
- Archivist 输入 tokens
- Archivist 输出 tokens

---

### 阶段 4：Main Agent 汇总

**Main 汇总**：
- 最终报告（含 token 成本分析）
- 下一步建议

**完成后记录**：
- Main 汇总输入 tokens
- Main 汇总输出 tokens

---

## 复盘模板（任务完成后填写）

```json
{
  "任务": "溪系统现状分析 + 分派验证",
  "日期": "YYYY-MM-DD",
  "参与者": ["Main", "Research", "Archivist"],
  "token 使用": {
    "Main-分派":   { "输入": N, "输出": N },
    "Research":    { "输入": N, "输出": N },
    "Archivist":   { "输入": N, "输出": N },
    "Main-汇总":   { "输入": N, "输出": N }
  },
  "token 总计": {
    "输入": N,
    "输出": N,
    "合计": N
  },
  "流程是否跑通": true/false,
  "最大消耗阶段": "阶段名",
  "优化空间": "...",
  "分派是否值得": true/false,
  "下次分派阈值建议": "N tokens"
}
```

---

## 成本优化参考（填入实测值）

| 分派深度 | 典型输入 | 典型输出 | 典型合计 |
|---------|---------|---------|---------|
| Main 直接回答 | - | - | 待填 |
| 1 个子 Agent | - | - | 待填 |
| 2 个子 Agent 并行 | - | - | 待填 |
| 3 个子 Agent | - | - | 待填 |

---

## 下一步（任务完成后）

1. Archivist 填写实际 token 用量到 DECISIONS.md
2. 制定分派性价比阈值
3. 建立 token 日志模板
