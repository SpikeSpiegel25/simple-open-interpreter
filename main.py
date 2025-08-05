import os
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_ollama import ChatOllama
from tools import list_files, read_file

# 创建一个示例文件
with open("example.txt", "w") as f:
    f.write("This is a sample file for the LangChain Open Interpreter demo.\n")
    f.write("It contains two lines of text.\n")

def main():
    print("Initializing LangChain Agent...")

    # 选择一个 LLM
    llm = ChatOllama(
        base_url="http://localhost:11434",
        model="qwen2.5:7b"
    )

    # 将所有工具放进一个列表
    tools = [list_files, read_file]

    # 从 LangChain Hub 获取 ReAct Agent 的 Prompt 模板
    prompt = hub.pull("hwchase17/react")
    prompt = prompt.partial(
        format_instructions="你必须严格按照以下格式输出工具调用与最终答案：\n"
                            "Action: 工具名\nAction Input: 工具输入（无多余描述，仅参数字符串）\n"
                            "Final Answer: 你的结论\n"
                            "不允许输出任何其它内容或解析说明。"
    )

    # 创建 Agent
    agent = create_react_agent(llm, tools, prompt)

    # 创建 Agent Executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, andle_parsing_errors=True )

    print("\nAgent Initialized. Starting interaction.")
    print("-----------------------------------------\n")

    # 交互
    # 任务1：让 Agent 列出当前目录下的文件
    print(">>> Task 1: List files in the current directory")
    response1 = agent_executor.invoke({
        "input": "Can you please list all the files in the current directory?"
    })
    print("\n>>> Agent's Final Answer:")
    print(response1['output'])
    print("\n-----------------------------------------\n")

    # 任务2： 让 Agent 读取指定文件的内容
    print(">>> Task 2: Read the content of 'example.txt'")
    response2 = agent_executor.invoke({
        "input": "I see a file named example.txt. Can you read its content for me?"
    })
    print("\n>>> Agent's Final Answer:")
    print(response2['output'])
    print("\n-----------------------------------------\n")

if __name__ == "__main__":
    main()
