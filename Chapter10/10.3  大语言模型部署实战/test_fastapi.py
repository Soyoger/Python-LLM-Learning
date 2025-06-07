#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 16:31
# @Author  : yongjie.su
# @File    : test_fastapi.py
# @Software: PyCharm
import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/chat"
    data = {
        "question": "中国的首都在哪里？",
        "top_p": 0.9,
        "temperature": 0.95
    }
    response = requests.post(url, json=data).json()
    print(response)
