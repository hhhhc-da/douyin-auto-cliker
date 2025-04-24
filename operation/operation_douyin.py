import time
import numpy as np
from helium import *


class Operation:            
    '''
    这里是所有的 Op 函数, 我们可以实现所有操作
    '''
    def send_message(self, driver, message, nickname):
        '''
        搜索特定用户并给用户发私信, 我们进入"精选"之后可以把最上面的推荐搜索卡掉
        '''
        try:
            # 我们首先点击"精选"按钮
            click("精选")
            time.sleep(2)
            
            # 执行搜索操作
            write(nickname, into="搜索你感兴趣的内容")
            press(ENTER)
            time.sleep(5)
            
            # 展示所有结果
            click("用户")
            time.sleep(2)
            
            # 获取我们的网页句柄
            main_window = driver.current_window_handle
            
            # 进入用户界面
            click("{}".format(nickname))
            time.sleep(5)  # 等待用户页面加载
            
            # 进入私信
            while True:
                if not Text("私信").exists():
                    time.sleep(1)
                else:
                    while True:
                        if Text("发送消息").exists():
                            time.sleep(1)
                            break
                        else:
                            message_btn = find_all(Button("私信"))[0]
                            click(message_btn)
                            time.sleep(1)
                    break
            time.sleep(3)
            
            # 输入消息内容
            write(message, into="发送消息")
            time.sleep(1)
            
            # 发送消息
            press(ENTER)
            time.sleep(2)
            print("消息发送成功")
            
            # 返回旧页面并且将其他页面全部关闭
            all_window_handles = driver.window_handles
            for handle in all_window_handles:
                if handle != main_window:
                    driver.switch_to.window(handle)
                    driver.close()
                    time.sleep(0.5)
            driver.switch_to.window(main_window)
            time.sleep(2)
            
            # 然后进入新的抖音界面
            go_to("https://www.douyin.com/")
            time.sleep(5)
            
        except Exception as e:
            print(f"操作失败: {str(e)}")

