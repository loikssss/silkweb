"""
Silk — 单 Agent 描述单元。
声明一个 Agent 的能力、工具集、上下文边界。
"""

from dataclasses import dataclass, field
from typing import List, Optional, Callable


@dataclass
class Silk:
    name: str
    capability: str
    tools: List[str] = field(default_factory=list)
    context_limit: int = 4096
    boundaries: List[str] = field(default_factory=list)
    description: str = ""
    system_prompt: Optional[str] = None

    def __post_init__(self):
        if not self.description:
            self.description = f"{self.name} ({self.capability})"
