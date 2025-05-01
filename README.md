# douyin-auto-cliker
基于Helium的自动化私信，下面的 GIF 的最后一部分就是本项目

![image](./static/douyin_spider_v1_0.gif)

### 安装说明
使用前安装好库

```
pip install helium pandas numpy
```

### 数据准备
准备一个 Excel 表格, 表头有 "user_id", "nickname", "score", 项目自动按照 nickname 进行搜索

### 数据对接
将 main.py 内的 Excel 文件替换, 我懒得加 argparser 所以没有改

```python
# 将这一句的文件定位出来
dou_yin = Douyin(os.path.join('..', 'Capture', 'runs', 'bert-user-test.xlsx'))
```
