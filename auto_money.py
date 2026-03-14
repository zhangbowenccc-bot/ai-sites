from executor import run_business
from tools.trend_finder import get_trends
import os

print("AI自动创业系统启动")

trends = get_trends()

print("发现趋势:", trends)

if not os.path.exists("sites"):
    os.mkdir("sites")

for i, trend in enumerate(trends):

    print(f"\n===== AI创业项目 {i+1}: {trend} =====")

    run_business(trend)

    os.rename("output_site.html", f"sites/auto_site_{i+1}.html")

print("\nAI创业系统完成")