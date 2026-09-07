from fastapi import FastAPI
from pydantic import BaseModel

from .agent import agent
# 等价于    from app.agent import agent


app = FastAPI(title="创建的第一个智能体demo！")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "Agent正在运行!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    print("\n" + "=" * 60)
    print("[Agent] 收到用户问题")
    print(f"[Agent] 用户: {request.message}")

    # 调用 Agent
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message
                }
            ]
        }
    )

    print("[Agent] 执行过程:")

    # 查看 Agent 产生的所有消息
    for message in result["messages"]:

        # 如果模型决定调用工具
        tool_calls = getattr(message, "tool_calls", [])

        if tool_calls:
            for call in tool_calls:
                print("\n[Agent → Tool]")
                print(f"工具名称: {call['name']}")
                print(f"工具参数: {call['args']}")

        # 如果这是工具返回的结果
        if getattr(message, "type", None) == "tool":
            print("\n[Tool → Agent]")
            print(f"工具名称: {getattr(message, 'name', 'unknown')}")
            print(f"工具结果: {message.content}")

    # 最后一条消息就是最终答案
    answer = result["messages"][-1].content

    print("\n[Agent] 最终答案:")
    print(answer)
    print("=" * 60 + "\n")

    return {
        "answer": answer
    }

