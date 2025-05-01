# douyin-auto-cliker
---
基于Helium的自动化私信，下面的 GIF 的最后一部分就是本项目

![image](./static/douyin_spider_v1_0.gif)

#### 本项目面向有一定 Python 编程能力的用户, 请先学习 os 系统库、argparse 参数处理库、pandas 数据存储库、numpy 数值计算库的相关内容

### 安装说明

使用前安装好库

```
pip install helium pandas numpy
```

### 数据准备

准备一个 Excel 表格, 表头有 "user_id", "nickname", "score", 项目自动按照 nickname 进行搜索

### 数据对接

将 main.py 内的 Excel 文件替换, 我懒得加 argparse 所以没有改

```python
# 将这一句的文件定位出来
dou_yin = Douyin(os.path.join('..', 'Capture', 'runs', 'bert-user-test.xlsx'))
```

注意, 项目如果想要应用需要较多修改, 同时请遵守抖音用户协议

```python
class Douyin:
    '''
    功能类, 可以实现一些自动化功能
    '''
    def __init__(self, xlsx_file_name=os.path.join('..', 'Capture', 'runs', 'bert-user-score.xlsx'), weights=0.3):
        '''
        初始化函数, 根据你们自己需要访问的内容更改
        '''
        self.is_login = False
        self.operate = Operation()
        self.pd_file = pd.read_excel(xlsx_file_name)
        
        self.pd_file = self.pd_file[self.pd_file['score'] > weights]
```

上面的初始化函数决定了你需要输入的数据, 只有评分达到设定的阈值后才会发送, 并且项目其实只用到了 "nickname" 和 "score" 所以剩余那个加不加都行

### 修改发送内容

```python
class Douyin:
    '''
    这里省略好多内容, 在这个类内修改
    '''

    def search_account(self, driver):
        '''
        抖音搜索账号, 自动化获取用户信息并发送指定内容
        '''
        for nickname in self.pd_file['nickname']:
            print("正在搜索用户: %s" % nickname)

#################################################################################

            # 修改这一个参数就可以了, 直接放这里或者自行封装
            message = "Hello"

#################################################################################
            self.operate.send_message(driver=driver, message=message, nickname=nickname)
            print("已完成发送")
            
        driver.quit()
        print("已完成所有操作")
```

### 拓展内容

想要实现文本分类并导出用户分析，可以查阅另一个项目

![BERT 文本分类项目](https://github.com/hhhhc-da/bilibili-spider)
