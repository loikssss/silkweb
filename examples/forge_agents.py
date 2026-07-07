"""
SilkWeb v0.2 示例：用 Loom.forge() 构建 Agent，然后编排执行。
"""

from silkweb.loom import Loom


def main():
    # 初始化编织器
    loom = Loom(topology="chain")

    # 锻造 Agent——输入自然语言描述即可
    loom.forge(
        "财报分析师",
        "读取上市公司财报，提取关键财务指标，判断健康度",
        tools=["web_search", "pdf_reader"],
    )
    loom.forge(
        "行业研究员",
        "结合财报分析结果，评估行业地位和竞争格局",
        tools=["web_search"],
    )
    loom.forge(
        "投资建议师",
        "综合前两个分析，给出买入/持有/卖出的判断和建议",
        tools=[],
    )

    # 查看编织结果
    print(loom.summary())
    print()

    # 导出所有 Agent 配置
    loom.export_all("/tmp/silkweb-agents")
    print()

    # 运行
    result = loom.run("分析宁德时代2024年财报并给出投资建议")
    print(f"最终结果:\n{result['final']}")


if __name__ == "__main__":
    main()
