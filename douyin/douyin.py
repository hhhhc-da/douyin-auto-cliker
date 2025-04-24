import time
from helium import *
from operation.operation_douyin import Operation
import pandas as pd
import os

"""
 1. 用户作品针对性点赞收藏评论
 2. 视频点赞收藏评论
"""


class Douyin:

    def __init__(self, xlsx_file_name=os.path.join('..', 'Capture', 'runs', 'bert-user-score.xlsx'), weights=0.3):
        self.is_login = False
        self.operate = Operation()
        self.pd_file = pd.read_excel(xlsx_file_name)
        
        self.pd_file = self.pd_file[self.pd_file['score'] > weights]

    def login(self):
        # 要拿到我们的句柄才行
        driver = start_chrome('www.douyin.com')
        wait_until(Text('登录后免费畅享高清视频').exists)
        while True:
            exist = Text("登录后免费畅享高清视频").exists()
            if not exist:
                self.is_login = True
                print("登录成功")
                break
            else:
                time.sleep(3)
        time.sleep(6)
        press(DOWN)
        return driver

    def search_account(self, driver):
        for nickname in self.pd_file['nickname']:
            print("正在搜索用户: %s" % nickname)
            message = "Hello"
            self.operate.send_message(driver=driver, message=message, nickname=nickname)
            print("已完成发送")
            
        driver.quit()
        print("已完成所有操作")
