"""
Loom — 编织器。多 Agent 编排引擎的核心。
"""

from typing import List, Dict, Any
from .silk import Silk
from .web import Web, Topology


class Loom:
    """编织器：管理 Silk 的编排和执行。"""

    def __init__(self, topology: str = "chain", silks: List[Silk] = None):
        self.silks = {s.name: s for s in (silks or [])}
        self.web = Web(Topology(topology), list(self.silks.keys()))

    def add_silk(self, silk: Silk):
        self.silks[silk.name] = silk
        self.web.add(silk.name)

    def connect(self, from_silk: str, to_silk: str):
        self.web.connect(from_silk, to_silk)

    def run(self, task: str) -> Dict[str, Any]:
        """运行编排流程。v0.1: 简单链式执行。"""
        results = {}
        context = {"task": task}

        for name in self.web.silks:
            print(f"  🧵 {name} 正在执行...")
            result = self._execute(name, context)
            results[name] = result
            context[f"{name}_output"] = result

        return {
            "task": task,
            "results": results,
            "final": results.get(self.web.silks[-1]) if self.web.silks else None,
        }

    def _execute(self, name: str, context: Dict) -> str:
        silk = self.silks.get(name)
        if not silk:
            return f"[{name}] 未找到 Silk"
        # v0.1 占位：打印能力声明
        return f"[{name}] 能力: {silk.capability} | 上下文: {context.get('task', '')}"

    def summary(self) -> str:
        lines = [f"Loom 编织器 | 拓扑: {self.web.topology.value}"]
        for name, silk in self.silks.items():
            lines.append(f"  🧵 {name}: {silk.capability}")
        return "\n".join(lines)
