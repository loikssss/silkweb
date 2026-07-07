# 🕸️ SilkWeb — Agent 编织框架

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 把 Agent 像丝线一样编织成网，协作完成复杂任务。

---

## 什么是 SilkWeb？

SilkWeb 是一个 **Agent 构建 + 多 Agent 编排框架**。

和普通的多 Agent 框架不同，SilkWeb 的核心是**构建 Agent**——你说"我需要一个能分析财报的Agent"，它就帮你生成完整配置（prompt + 工具 + 记忆 + 边界），而不是让你自己去写。

**你不是在编排一堆写死的 Agent，而是在编织一个不断生长的 Agent 网络。**

## 核心概念

### 🧵 Silk（丝）— Agent 构建器

Silk 不是一个数据类，是一个 **Agent 生成器**。你给一段自然语言描述，它给你一个完整可运行的 Agent。

```python
loom.forge("财报分析师", "读取财报，提取关键指标，判断健康度", tools=["web_search", "pdf_reader"])
```

产物是结构化的 Agent 蓝图（可导出为 JSON）：
- 系统提示词（system prompt）
- 能力声明
- 工具集
- 记忆配置
- 行为边界

### 🕸️ Web（网）— 运行时拓扑

Agent 之间的协作网络。支持多种编织方式：
- **链式**：A → B → C 串行
- **星型**：中心分发
- **网格**：全连接自由通信
- **动态**：运行时自动组网

### ⚙️ Loom（编织器）— 编译 + 运行时

两个阶段：
1. **编译期**：`forge()` → 把需求编译成 Agent 配置
2. **运行期**：`run()` → 编排多 Agent 协作执行

## 快速体验

```python
from silkweb.loom import Loom

loom = Loom(topology="chain")

# 锻造 3 个 Agent——输入自然语言描述
loom.forge("财报分析师", "读取财报，提取关键财务指标", tools=["web_search"])
loom.forge("行业研究员", "评估行业地位和竞争格局", tools=["web_search"])
loom.forge("投资建议师", "综合前两个分析，给出买卖建议")

# 查看编织结果
print(loom.summary())

# 运行
result = loom.run("分析宁德时代2024年财报并给出投资建议")
print(result)
```

## 架构

```
┌─────────────────────────────────────────┐
│            Loom 编译期 (forge)           │
│                                         │
│  需求描述 ──→ 蓝图编译 ──→ Agent 配置    │
│  ("我需要一个...)   (prompt+工具+记忆)    │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│            Loom 运行期 (run)             │
│                                         │
│      🧵 Agent A ──→ 🧵 Agent B          │
│      (财报分析)     (行业研究)           │
│                       │                 │
│                       ▼                 │
│                     🧵 Agent C           │
│                    (投资建议)            │
└─────────────────────────────────────────┘
```

## 适用场景

| 场景 | 说明 | 拓扑 |
|:----|:-----|:----|
| **复杂任务分解** | 一个请求需要多个能力组合 | 星型 |
| **流水线处理** | 数据经过多步链式处理 | 链式 |
| **代码开发流水线** | 生成 → 审查 → 测试 | 链式 |
| **知识蒸馏** | 多专家各自贡献领域知识 | 星型 |
| **团队模拟** | 不同角色 Agent 协作 | 网格 |

## 路线图

| 阶段 | 内容 | 状态 |
|:----|:-----|:----:|
| v0.1 | 基础骨架 | ✅ |
| v0.2 | **`forge()` Agent 构建 + 链式编排** | ✅ **当前** |
| v0.3 | 意图解析 + 动态拓扑 | ⏳ |
| v0.4 | AI 真实调用（接入 LLM） | ❌ |
| v0.5 | 插件系统 + 远程节点 | ❌ |
| v1.0 | 生产可用 + 监控仪表盘 | ❌ |

## 相关项目

- **cangjie-book2skill**：把方法论书籍蒸馏成 Agent Skill
- **cangjie-cognitive-implant**：从素材中提取个人认知上下文

## License

MIT © 2026 loikssss
