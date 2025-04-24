import time
import numpy as np
from helium import *


class Operation:            
    #
    # 给用户发私信
    #
    def send_message(self, driver, message, nickname):
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

    #
    # 视频点赞
    #
    @staticmethod
    def video_click_like():
        time.sleep(3)
        like_label_items = find_all(S("//div[@data-e2e-state='video-player-no-digged']"))
        if len(like_label_items) > 0:
            press("z")
            print("点赞成功")
        else:
            print("该视频已经点赞啦")

    #
    # 用户关注
    #
    @staticmethod
    def user_click_follow():
        time.sleep(3)
        follow_exist = Text("关注").exists()
        if not follow_exist:
            follow_exist = Text("回关").exists()
            if not follow_exist:
                print("该用户已关注啦")
            else:
                click("回关")
                print("回关成功")
        else:
            click("关注")
            print("关注成功")

    # #
    # # 匹配消息
    # #
    # @staticmethod
    # def _match_comment(video_desc, match_comment_item_map):
    #     for key, value in match_comment_item_map.items():
    #         if key in video_desc:
    #             return value
    #     return ""

    # #
    # # 匹配视频
    # #
    # @staticmethod
    # def _match_video(video_desc, match_video_items):
    #     for match_video_item in match_video_items:
    #         if match_video_item in video_desc:
    #             return True
    #     return False

    # #
    # # 获取内容评论总条数
    # #
    # @staticmethod
    # def _get_comment_total_count(video_comment_count_text):
    #     return video_comment_count_text[video_comment_count_text.find("(") + 1:video_comment_count_text.find(")")]


