import time
from helium import *
from operation.operation_douyin import Operation
import pandas as pd
import os

class Douyin:
    '''
    抖音功能类, 可以实现一些自动化功能
    '''
    def __init__(self, xlsx_file_name=os.path.join('..', 'Capture', 'runs', 'bert-user-score.xlsx'), weights=0.3):
        '''
        抖音初始化函数, 根据你们自己需要访问的内容更改
        '''
        self.is_login = False
        self.operate = Operation()
        self.pd_file = pd.read_excel(xlsx_file_name)
        
        self.pd_file = self.pd_file[self.pd_file['score'] > weights]

    def login(self):
        '''
        登录函数, 我们要拿到我们的窗体句柄, 否则会有很多浪费
        '''
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
        '''
        抖音搜索账号, 自动化获取用户信息并发送指定内容
        '''
        for nickname in self.pd_file['nickname']:
            print("正在搜索用户: %s" % nickname)
            message = "Hello"
            self.operate.send_message(driver=driver, message=message, nickname=nickname)
            print("已完成发送")
            
        driver.quit()
        print("已完成所有操作")
