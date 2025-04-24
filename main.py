import os
from douyin.douyin import Douyin

dou_yin = Douyin(os.path.join('..', 'Capture', 'runs', 'bert-user-test.xlsx'))

def select_platform():
    print("抖音开始登录")
    driver = dou_yin.login()
    
    print("抖音开始搜索用户")
    auto_send_message(driver)


def auto_send_message(driver):
    while True:
        if not dou_yin.is_login:
            print("请先登录...")
            dou_yin.login()
            continue
        break
    
    # 发送数据 API
    dou_yin.search_account(driver=driver)

if __name__ == "__main__":
    select_platform()