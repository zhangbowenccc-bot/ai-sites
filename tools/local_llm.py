import subprocess

def generate_text(prompt):

    cmd=["ollama","run","qwen2:7b",prompt]

    result=subprocess.run(cmd,capture_output=True,text=True)

    return result.stdout