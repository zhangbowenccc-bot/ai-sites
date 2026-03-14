import os

print("AI Auto Deploy V29 启动")

site_folder = "websites"

repo = "ai-sites"

# 初始化 git
os.system("git init")

# 添加文件
os.system("git add .")

# 提交
os.system('git commit -m "AI generated sites"')

# 添加远程仓库
os.system(f"git remote add origin https://github.com/zhangbowenccc-bot/ai-sites.git")

# 推送
os.system("git branch -M main")
os.system("git push -u origin main")

print("网站已上传 GitHub")