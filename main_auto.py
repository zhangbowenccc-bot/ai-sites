import time
from executor import run_business

while True:

    print("\nAI业务系统启动...\n")

    run_business("AI副业")

    print("\n等待1小时继续...\n")

    time.sleep(3600)