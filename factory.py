from executor import run_business

ideas = [
    "AI写作助手",
    "AI学习助手",
    "AI短视频生成",
    "AI电商选品工具",
    "AI简历优化工具"
]

for i, idea in enumerate(ideas):

    print(f"\n===== 生成创业项目 {i+1}: {idea} =====\n")

    run_business(idea)

    import os
    os.rename("output_site.html", f"sites/site_{i+1}.html")