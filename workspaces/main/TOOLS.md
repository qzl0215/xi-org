# TOOLS.md

> 本文件定义 Main Agent 的环境约定、路径约定、工具使用规则与高风险边界。 
> 它不是使命文件；使命与主权看 `SOUL.md`。 
> 它不是项目状态文件；项目状态看 `shared/projects/*`。 
> 它不是记忆文件；长期记忆看 `MEMORY.md` 与 `memory/*`。

---

# 1. 基本原则

1. **先确认真实路径，再操作。**
   不要凭记忆假设路径、端口、配置文件位置。
   在未确认 canonical path 前，不直接改配置、不直接重启。

2. **优先读，后改。**
   先收集证据：路径、配置、进程、端口、日志、最近变更。
   再做最小必要修改。

3. **优先最小差异改动。**
   不做大面积无必要重构。
   不为了"顺手整理"扩大改动范围。

4. **优先可逆操作。**
   改前留快照。
   高风险文件先备份再编辑。

5. **绝不把 workspace 当 secrets 仓库。**
   凭证、token、auth、私钥、cookie 不应写入共享知识、记忆、项目文件。

---

# 2. 目标目录拓扑（标准化目标）

若系统已完成标准化，默认以这些路径为准：

- `ORG_ROOT=/srv/xi`
- `SHARED_ROOT=/srv/xi/shared`
- `WORKSPACES_ROOT=/srv/xi/workspaces`
- `MAIN_WS=/srv/xi/workspaces/main`
- `RESEARCH_WS=/srv/xi/workspaces/research`
- `BUILDER_WS=/srv/xi/workspaces/builder`
- `ARCHIVIST_WS=/srv/xi/workspaces/archivist`
- `OPENCLAW_RUNTIME=~/.openclaw`
- `OPENCLAW_CONFIG=~/.openclaw/openclaw.json`

若系统尚未完成标准化，先做 discovery，不要硬套标准路径。

---

# 3. 已知历史线索（仅作线索，不作真相）

历史上曾出现过以下线索：

- 可能存在旧配置路径：`/root/openclaw-data/openclaw.json`
- 可能存在 Gateway 相关端口：`18789` / `18790`
- 可能存在多个 OpenClaw 副本或多个项目目录并存

这些都**不是默认真相**。 
它们只说明：**必须先探测当前系统，再下手。**

---

# 4. Discovery 优先命令

在任何高价值或高风险操作前，优先用以下命令建立事实：

## 4.1 路径探测
```bash
pwd
whoami
hostname
find /root /srv -maxdepth 4 -name 'openclaw.json' 2>/dev/null
find /root /srv -maxdepth 4 -type d -name '.openclaw' 2>/dev/null
find /root /srv -maxdepth 4 -type d -name 'workspaces' 2>/dev/null
```

## 4.2 进程与端口探测
```bash
ps aux | grep -i openclaw | grep -v grep
ss -lntp | grep -E '18789|18790|openclaw'
lsof -i -P -n | grep -i openclaw
```

## 4.3 目录结构探测
```bash
ls -la
find . -maxdepth 2 -type f | sort | head -200
tree -L 3 2>/dev/null || find . -maxdepth 3 | sort | head -300
```

## 4.4 Git 状态探测
```bash
git status --short
git branch --show-current
git log --oneline --decorate -n 20
git diff --stat
```

原则：先看事实，再改系统。

---

# 5. 推荐工具与命令习惯

## 5.1 搜索

优先使用：

- `rg`：搜索文件内容
- `fd`：搜索文件名（若已安装）
- `find`：通用查找
- `grep`：仅在简单场景下使用

优先级：
`rg` > `grep -R`

## 5.2 查看大文件

不要直接 `cat` 巨大文件。
优先使用：

```bash
head -100 FILE
tail -100 FILE
sed -n '1,120p' FILE
rg "pattern" FILE
```

## 5.3 JSON / YAML / 结构化处理

优先使用：

- `jq` 处理 JSON
- `yq` 处理 YAML（若已安装）
- 若工具缺失，使用 `python3` 做一次性解析

## 5.4 差异与快照

改前先留快照：

```bash
cp FILE FILE.bak.$(date +%Y%m%d-%H%M%S)
```

比较优先使用：

```bash
diff -u OLD NEW
git diff
git diff --stat
```

## 5.5 磁盘 / 进程 / 网络

常用只读诊断：

```bash
df -h
du -sh *
ps aux
ss -lntp
lsof -i -P -n
```

---

# 6. 文件与目录职责约定

## 6.1 Root 注入文件（必须短硬）

以下 root 文件会高频影响 agent 上下文，必须保持精炼：

- `SOUL.md`
- `AGENTS.md`
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- `MEMORY.md`

不要把大体量细则、长篇知识、冗长 SOP 堆进这些文件。

## 6.2 Daily memory

- `memory/YYYY-MM-DD.md` 是 append-only 的每日记录
- 记录当天做了什么、确认了什么、踩了什么坑、出现了什么新开放回路
- 不要求优雅，只要求真实、可追溯

## 6.3 长期记忆

- `MEMORY.md` 只保留精选、稳定、长期、高复用内容
- 不复制原始聊天
- 不保存大量短期噪音

## 6.4 项目状态

所有项目状态以 `shared/projects/<project-id>/` 为主：

- `PROJECT.md`
- `STATUS.md`
- `TASKS.md`
- `DECISIONS.md`
- `RISKS.md`

不要把项目状态散落在聊天记录或 scratch 里。

## 6.5 知识治理

知识资产以 `shared/knowledge/` 为主：

- `inbox/`
- `sources/`
- `parsed/`
- `cards/`
- `canon/`
- `registry/`

不要把知识库混进 `MEMORY.md`。

---

# 7. 高风险红线（Ask First）

以下操作必须先征得明确同意：

**删除、覆盖、移动重要目录或文件**
- `rm -rf`
- 覆盖 `shared/policies/*`
- 覆盖 `shared/projects/*`
- 覆盖 `~/.openclaw/*`
- 批量移动 workspace

**高风险 Git 操作**
- `git reset --hard`
- `git clean -fdx`
- `git push --force`
- 改 remote
- 重写历史

**生产级副作用操作**
- 重启 gateway / service
- 生产部署
- 外发消息 / 邮件 / webhook
- 改线上环境变量
- 改 auth / token / secrets

**系统级高风险操作**
- `chmod -R`
- `chown -R`
- `apt install/remove`
- `docker system prune`
- 大范围 `rsync --delete`
- 编辑 systemd / supervisor / pm2 等服务配置（除非任务明确）

**不确定但可能不可逆的操作**
- 任何自己没有把握的命令
- 任何影响范围不清的递归改动
- 任何可能泄露隐私或凭证的行为

---

# 8. 默认可自由进行的低风险动作

以下动作默认可直接进行：

- 读取文件
- 搜索内容
- 整理摘要
- 写草稿
- 写 scratch 文件
- 更新 daily memory
- 更新项目状态文件
- 生成计划、模板、结构化文档
- 做小范围、可逆、易回滚的工作区改动
- 做只读型系统探测
- 做无副作用的验证与对比

---

# 9. OpenClaw 特别规则

1. 每个 agent 的 workspace 与 agentDir 应视为独立边界。
   不要混用，不要默认共用状态。

2. 不要直接把运行时状态当知识库。
   `~/.openclaw/` 主要是运行时配置、auth、sessions、skills。
   组织资产主要放在 `/srv/xi/shared/` 和对应 workspace。

3. Root 文件短，细则外置。
   细规则放到：
   - `shared/policies/*`
   - `shared/playbooks/*`
   - `skills/*/SKILL.md`

4. Workspace 不是硬沙箱。
   即使当前 cwd 在 workspace，也不能假设不会触碰宿主机其它位置。
   涉及高风险路径操作时要格外谨慎。

---

# 10. 修改协议

默认按以下顺序执行修改：

1. **Inspect**
   - 找路径
   - 看配置
   - 看状态
   - 看最近改动

2. **Snapshot**
   - 关键文件先备份
   - 记下当前状态

3. **Change**
   - 做最小改动
   - 只改当前目标真正需要的部分

4. **Validate**
   - 检查 diff
   - 检查语法 / 结构
   - 检查是否影响超出预期

5. **Record**
   - 把关键动作和结果写入 daily memory 或项目状态
   - 若形成长期规则，后续再升格到 policy / playbook / MEMORY

---

# 11. 输出证据规则

在报告"已经确认/已经修复/已经定位"之前，应尽量具备至少一种证据：

- 路径证据
- 配置证据
- 进程证据
- 端口证据
- diff 证据
- 日志证据
- 文件内容证据

不要仅凭推测下结论。

---

# 12. 一句话原则

先确认真实环境，再做最小可逆改动；把危险操作关进 Ask First，把长期资产与运行时状态严格分开。