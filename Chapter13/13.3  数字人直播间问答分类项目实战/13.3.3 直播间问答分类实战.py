#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/17 22:52
# @Author  : yongjie.su
# @File    : 13.3.3 直播间问答分类实战.py
# @Software: PyCharm
import re


def is_product_explanation(text):
    """
    通过正则匹配“n号”来判定是否为求讲解
    :param text:
    :return:
    """
    pattern = r"[1-9]\d{0,2}号"
    result = re.search(pattern, text)
    return result is not None


print(is_product_explanation("求讲解6号宝贝"))
print(is_product_explanation("男士购买洗面奶推荐哪个？"))
