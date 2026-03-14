from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")


def create_marketing(topic):

    prompt = f"""
你是AI营销专家。

产品领域:
{topic}

请设计营销方案。

输出:
1 目标用户
2 推广渠道
3 宣传策略
4 盈利方式
"""

    return llm.invoke(prompt)