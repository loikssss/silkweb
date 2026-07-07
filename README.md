# 🕸️ SilkWeb — Agent 编织框架

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 把 Agent 像丝线一样编织成网，协作完成复杂任务。

---

## 什么是 SilkWeb？

SilkWeb 是一个 **多 Agent 编排框架**，让多个 AI Agent 像丝网上的节点一样互联协作。

每个 Agent 是一根独立的「丝」(Silk)——有自己的能力、记忆和工具集。SilkWeb 的「编织器」(Loom) 负责把它们编织起来：共享上下文、路由任务、协调执行。

**核心思想：单个 Agent 再强也有限，但织成网的 Agent 集群很强大。**

## 核心概念

### 🧵 Silk（丝）
单个 Agent 的描述单元。每根丝声明：
- **能力**：它擅长做什么
- **工具集**：它能调用什么外部工具
- **上下文**：它的记忆/上下文窗口大小
- **边界**：它的权限和限制

### 🕸️ Web（网）
Agent 之间的通信拓扑。支持多种编织方式：
- **星型**：一个中心 Agent 分发任务
- **链式**：A → B → C 串行处理
- **网格**：所有 Agent 自由通信
- **动态织网**：运行时根据任务自动组网

### ⚙️ Loom（编织器）
核心编排引擎。它的工作：
1. **意图解析**：理解用户想做什么
2. **任务拆解**：把复杂目标拆成子任务
3. **Silk 匹配**：为每个子任务找到最合适的 Agent
4. **调度执行**：管理跨 Agent 的上下文传递和结果合并
5. **结果编织**：把所有 Agent 的输出合成完整回答

## 快速开始

```bash
# 安装
pip install silkweb

# 初始化项目
silkweb init my-project
cd my-project

# 运行
silkweb run
```

## 示例

```python
from silkweb import Loom, Silk

# 定义两个 Silk
coder = Silk(name="coder", capability="code_generation")
reviewer = Silk(name="reviewer", capability="code_review")

# 编织成链
loom = Loom(topology="chain", silks=[coder, reviewer])

# 运行
result = loom.run("写一个斐波那契函数并审查")
print(result)
```

## 架构

```
┌──────────────────────────────────────────┐
│               Loom (编织器)               │
│                                          │
│  意图解析 → 任务拆解 → Silk匹配 → 调度执行 │
│                                          │
│         ┌──────┬──────┬──────┐           │
│         ▼      ▼      ▼      ▼           │
│       Silk1  Silk2  Silk3  Silk4          │
│       (代码) (搜索) (分析) (总结)         │
│         │      │      │      │           │
│         └──────┴──────┴──────┘           │
│               结果编织                     │
└──────────────────────────────────────────┘
```

## 适用场景

| 场景 | 说明 | 拓扑建议 |
|:----|:-----|:---------|
| **复杂任务分解** | 一个请求需要多个能力组合 | 星型 |
| **流水线处理** | 数据经过多步链式处理 | 链式 |
| **团队模拟** | 不同角色 Agent 协作 | 网格 |
| **知识蒸馏** | 多专家各自贡献领域知识 | 星型 |
| **代码开发** | 生成 → 审查 → 测试 → 部署 | 链式 |

## 路线图

| 阶段 | 内容 | 状态 |
|:----|:-----|:----:|
| v0.1 | Silk 定义 + Loom 基础编排 + 链式拓扑 | ✅ 已发布 |
| v0.2 | 动态拓扑 + 上下文共享 + 意图解析 | ⏳ 开发中 |
| v0.3 | 插件系统 + 远程 Silk 节点 | ❌ |
| v1.0 | 生产可用 + 监控仪表盘 | ❌ |

## 相关项目

- **cangjie-book2skill**：把方法论书籍蒸馏成 Agent Skill
- **cangjie-cognitive-implant**：从素材中提取个人认知上下文

## License

MIT © 2026 loikssss
