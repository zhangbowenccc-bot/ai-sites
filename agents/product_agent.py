from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")


def design_product(topic):

    prompt = f"""
你是AI产品经理。

领域:
{topic}

请设计一个AI产品。

输出:
1 产品名称
2 产品功能
3 用户群体
4 收费模式
"""

    return llm.invoke(prompt)