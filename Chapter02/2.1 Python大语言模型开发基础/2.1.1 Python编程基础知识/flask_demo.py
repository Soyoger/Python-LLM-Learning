#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 18:48
# @Author  : yongjie.su
# @File    : flask_demo.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


# 创建健康检查的服务
@app.route('/health', methods=["GET"])
def health():
    return 'OK'


# 创建对话服务
@app.route('/chat', methods=["POST"])
def chat():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8088, debug=False)
