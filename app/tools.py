from langchain_core.tools import tool





@tool
def calculator(expression: str) -> str:
# def 函数名(参数名: 类型) -> 返回值类型:
# :  前面：参数变量名字（必写）
# :  后面：类型注解（可选）
# -> 后面：返回值类型注解（可选）
    """
    计算数学表达式。
    例如：2 + 3 * 4
    """

    # 工具开始执行
    print(f"\n[Tool] calculator 开始执行")
    print(f"[Tool] 函数接收到的表达式(参数): {expression}")

    try:
        result = eval(expression, {"__builtins__": {}}, {})

        # 工具执行成功
        print(f"[Tool] 计算结果: {result}")

        return str(result)

    except Exception as e:  # 把错误原因存到变量 `e`

        # 工具执行失败
        print(f"[Tool] 执行失败: {e}")

        return f"计算失败：{e}"