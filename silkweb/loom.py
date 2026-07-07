"""
Loom — 编织器。多 Agent 构建 + 编排引擎。
"""

from typing import List, Dict, Any, Optional
from .silk import SilkBlueprint
from .web import Web, Topology


class Loom:
    """
    编织器：
    - 编译期：将需求描述构建成 Agent（Silk）
    - 运行期：编排多个 Agent 协作
    """

    def __init__(self, topology: str = "chain"):
        self.silks: Dict[str, SilkBlueprint] = {}
        self.web = Web(Topology(topology))
        self.results: Dict[str, Any] = {}

    # ── 编译期：Agent 构建 ──

    def forge(self, name: str, description: str, tools: Optional[List[str]] = None) -> SilkBlueprint:
        """锻造一个 Agent（Silk）。"""
        blueprint = SilkBlueprint.from_description(f"{name}，{description}")
        if tools:
            for t in tools:
                blueprint.add_tool(t)
        self.silks[name] = blueprint
        self.web.add(name)
        return blueprint

    def forge_from_file(self, path: str) -> SilkBlueprint:
        """从配置文件加载一个 Agent。"""
        blueprint = SilkBlueprint.from_file(path)
        self.silks[blueprint.name] = blueprint
        self.web.add(blueprint.name)
        return blueprint

    def export_all(self, output_dir: str):
        """导出所有 Agent 配置。"""
        for name, silk in self.silks.items():
            path = silk.to_file(os.path.join(output_dir, f"{name}.json"))
            print(f"  ✅ 已导出: {path}")

    # ── 运行期：编排执行 ──

    def connect(self, from_silk: str, to_silk: str):
        self.web.connect(from_silk, to_silk)

    def run(self, task: str) -> Dict[str, Any]:
        """运行编排流程。"""
        results = {}
        context = {"task": task}

        print(f"\n  🕸️ SilkWeb 开始执行: {task}\n")

        for i, name in enumerate(self.web.silks):
            silk = self.silks.get(name)
            if not silk:
                continue

            print(f"  [{'='*20}")
            print(f"   🧵 {name} ({silk.capability})")
            print(f"   📝 {silk.description}")

            # 模拟执行
            result = self._execute(silk, context)

            results[name] = result
            context[f"{name}_output"] = result
            print(f"   ✅ {name} 完成")
            print(f"   {'='*20}]\n")

        self.results = results
        return {
            "task": task,
            "results": results,
            "final": results.get(self.web.silks[-1]) if self.web.silks else None,
        }

    def _execute(self, silk: SilkBlueprint, context: Dict) -> str:
        """v0.1: 模拟执行，输出 Agent 的 system prompt 作为占位。"""
        return (
            f"[{silk.name}]\n"
            f"能力: {silk.capability}\n"
            f"描述: {silk.description}\n"
            f"工具: {', '.join(silk.tools) if silk.tools else '（无）'}\n"
            f"输入上下文: {context.get('task', '')[:100]}"
        )

    def summary(self) -> str:
        lines = [f"🕸️ SilkWeb | 拓扑: {self.web.topology.value}"]
        lines.append(f"   编织了 {len(self.silks)} 个 Agent:")
        for name, silk in self.silks.items():
            tools = f" [{', '.join(silk.tools)}]" if silk.tools else ""
            lines.append(f"   🧵 {name}: {silk.capability}{tools}")
        return "\n".join(lines)


import os  # noqa: E402 (needed for export_all)
