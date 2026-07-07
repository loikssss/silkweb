"""
Silk — Agent 构建器。
输入自然语言描述，输出完整的 Agent 配置。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import json
import os


AGENT_TEMPLATE = """# {name}

你是 {name}，擅长 {capability}。

## 角色描述
{description}

## 工具集
{tools_summary}

## 行为边界
- {boundaries}

## 记忆结构
{memory_structure}
"""


@dataclass
class SilkBlueprint:
    """Agent 构建蓝图——由需求描述编译而来。"""
    name: str
    capability: str
    description: str
    tools: List[str] = field(default_factory=list)
    system_prompt: str = ""
    boundaries: List[str] = field(default_factory=list)
    memory_config: Dict[str, Any] = field(default_factory=lambda: {
        "type": "short_term",
        "capacity": 4096,
    })
    output_dir: str = ""

    def to_file(self, path: str = ""):
        """将蓝图写入文件，生成可加载的 Agent 配置。"""
        path = path or os.path.join(self.output_dir, f"{self.name}.json")
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(self.__dict__, f, indent=2, ensure_ascii=False)
        return path

    @classmethod
    def from_file(cls, path: str) -> "SilkBlueprint":
        with open(path) as f:
            data = json.load(f)
        return cls(**data)

    @classmethod
    def from_description(cls, description: str) -> "SilkBlueprint":
        """从自然语言描述编译 Agent 蓝图。v0.1: 简单解析。"""
        parts = description.split("，")
        name = parts[0].strip() if parts else "agent"
        rest = "，".join(parts[1:]) if len(parts) > 1 else description

        return cls(
            name=name,
            capability="通用能力",
            description=rest,
            tools=[],
            boundaries=["不执行危险操作", "不确定时询问用户"],
            system_prompt=AGENT_TEMPLATE.format(
                name=name,
                capability="通用能力",
                description=rest,
                tools_summary="（待配置）",
                boundaries="\n- ".join(["不执行危险操作", "不确定时询问用户"]),
                memory_structure="短期记忆 (4096 tokens)",
            ),
        )

    def add_tool(self, tool: str):
        self.tools.append(tool)
        return self
