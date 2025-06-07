#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 18:56
# @Author  : yongjie.su
# @File    : requests_demo.py
# @Software: PyCharm
# 导入requests库
import requests

# 处理 Get请求
response = requests.get('https://www.baidu.com/', timeout=3)
print(response.status_code)
print(response.text)

# 处理 Post请求
data = {'prompt': '请告诉我中国的首都在哪儿？'}
response = requests.post('http://localhost:8088/chat', json=data, timeout=3)
print(response.status_code)
print(response.text)
