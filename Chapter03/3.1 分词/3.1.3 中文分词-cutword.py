#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 17:17
# @Author  : yongjie.su
# @File    : 3.1.3 中文分词-cutword.py
# @Software: PyCharm

"""
如果报错：
    错误问题：opencc 初始化失败！项目将没有繁简转化功能 No module named 'opencc'
    解决办法：pip install opencc  -i https://pypi.tuna.tsinghua.edu.cn/simple
    (opencc项目是一个开源的中文简繁体转化的工具)

"""

from cutword import Cutter

if __name__ == '__main__':
    sentence = "2023年度十大新词语是：生成式人工智能、全球文明倡议、村超、新质生产力、全国生态日、消费提振年、特种兵式旅游、显眼包、百模大战、墨子巡天。"
    custom_dict_path = "custom_dict.txt"
    """
    用户自定义词典格式：词\t词频\t词性
    """
    cutter = Cutter(want_long_word=True, custom_dict_path=custom_dict_path)
    segments = cutter.cutword(sentence)
    print(segments)
