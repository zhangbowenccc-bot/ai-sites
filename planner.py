from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def create_plan(goal):

    prompt = f"""
你是AI创业规划师。

目标:
{goal}

制定完成目标的步骤。
"""

    return llm.invoke(prompt)