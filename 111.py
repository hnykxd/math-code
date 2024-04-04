import os
import schedule
import time

print("                                       Windows主进程，请勿关闭")
print("Windows主进程，请勿关闭")
print("Windows主进程，请勿关闭")
print("Windows主进程，请勿关闭")
print("Windows主进程，请勿关闭")
print("Windows主进程，请勿关闭")
def run_file():
    file_path = r"D:\Desktop\接下来进入到最后的宣誓阶段：.ppsx"
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        print("文件路径不存在或者无法找到。请检查路径是否正确。")

# 将run_file()函数安排在早上六点46分30秒运行
schedule.every().day.at("06:46:30").do(run_file)

# 在程序中执行调度
while True:
    schedule.run_pending()
    time.sleep(1)
    
