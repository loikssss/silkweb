"""
Web — 网络拓扑定义。
支持链式、星型、网格、动态四种拓扑。
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Tuple


class Topology(Enum):
    CHAIN = "chain"        # A → B → C
    STAR = "star"          # 中心分发
    MESH = "mesh"          # 全连接
    DYNAMIC = "dynamic"    # 运行时自动组网


@dataclass
class Web:
    topology: Topology
    silks: List[str] = field(default_factory=list)
    edges: List[Tuple[str, str]] = field(default_factory=list)  # (from, to)

    def add(self, silk_name: str):
        self.silks.append(silk_name)

    def connect(self, from_silk: str, to_silk: str):
        self.edges.append((from_silk, to_silk))
