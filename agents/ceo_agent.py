from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def ceo_decide(niche):

    prompt = f"""
你是AI创业公司的CEO。

领域:
{niche}

请制定商业方向。

输出：
1 商业机会
2 执行任务
"""

    return llm.invoke(prompt)