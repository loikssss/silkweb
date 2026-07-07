"""
SilkWeb 基础示例：链式编排三个 Agent。
"""

from silkweb.silk import Silk
from silkweb.loom import Loom


def main():
    # 定义三根丝
    researcher = Silk(
        name="researcher",
        capability="research_and_analysis",
        description="擅长搜索和分析信息",
    )
    writer = Silk(
        name="writer",
        capability="content_writing",
        description="擅长把分析结果写成清晰文本",
    )
    reviewer = Silk(
        name="reviewer",
        capability="quality_review",
        description="擅长审查和优化输出质量",
    )

    # 编织成链
    loom = Loom(topology="chain", silks=[researcher, writer, reviewer])

    print(loom.summary())
    print()

    # 运行
    result = loom.run("分析 Python 异步编程的优缺点")
    print(f"\n最终输出: {result['final']}")


if __name__ == "__main__":
    main()
