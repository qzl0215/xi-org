# coding-workflow.md

# Playbook: Builder Agent 代码工作流

> 目标：让 OpenClaw Builder Agent 的代码能力 ≥ Codex Pro

---

## 标准流程

### 1. 接收任务

从 Main Agent 收到明确的实现任务：
- 要实现什么功能
- 在哪个项目/文件
- 成功标准是什么

### 2. 环境探测

```bash
# 确认项目位置
ls ~/Documents/Github/<project>/

# 确认技术栈
cat package.json  # Node 项目
cat pyproject.toml  # Python 项目
cat requirements.txt  # Python 依赖

# 确认现有代码结构
find . -type f -name "*.py" | head -20
find . -type f -name "*.ts" | head -20
```

### 3. 上下文加载

读取相关文件：
- 目标文件 + 相关模块
- 测试文件（如有）
- 配置文件
- 最近 git 改动

### 4. 最小改动实现

- 先理解现有代码结构
- 找最小改动路径
- 改前备份
- 实现改动
- 本地验证

### 5. 输出

必须包含：
1. 改了什么（文件列表 + 改动点）
2. 为什么这么改
3. 怎么验证
4. 如何回滚
5. 风险/未完成项

---

## 与 Codex Pro 对比

| 能力 | Codex Pro | OpenClaw Builder | 差距 |
|------|-----------|------------------|------|
| 代码理解 | codebase indexing | 手动读取 | 需优化 |
| 测试验证 | 自动运行测试 | 需手动 | 需自动化 |
| Git 隔离 | worktree | 直接改 | 需加 worktree |
| 多文件改动 | 支持 | 支持 | ✅ |
| 调试能力 | 集成 debugger | 需手动 | 需优化 |

---

## 优化方向

1. **代码索引**：为项目建立 code_index（已有）
2. **自动测试**：改动后自动跑测试
3. **Git worktree**：在隔离环境改代码
4. **调试集成**：集成调试工具

---

## 性价比基准

Codex Pro：$20/月，无限 token
OpenClaw：按 token 计费

**目标**：OpenClaw 写代码的 token 成本 ≤ Codex Pro 等效成本

**估算**：
- Codex Pro 单次任务成本 ≈ $0.01-0.05（摊销）
- OpenClaw 单次任务 token ≈ 10k-50k
- 按 $0.002/1k tokens 计算：$0.02-0.10

**结论**：OpenClaw 成本可接受，但需要控制上下文加载量。