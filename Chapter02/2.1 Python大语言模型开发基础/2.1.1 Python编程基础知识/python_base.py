#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 18:52
# @Author  : yongjie.su
# @File    : python_base.py
# @Software: PyCharm
# 单个变量复制
# name = "Alice"
# 多个变量复制
name, age = "Alice", 18

score = 90
if score >= 90:
    print("优秀！")
elif score >= 80:
    print("良好！")
elif score >= 60:
    print("一般！")
else:
    print("不及格！")

# for循环 打印0-99的整数
for value in range(100):
    print(value)

# while循环 打印0-99的整数
value = 0
while value < 100:
    print(value)
    value += 1


# 定义一个求两个整数的函数
def sum(x: int, y: int) -> int:
    return x + y


print(sum(1, 2))


# 定义一个二叉树节点类
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
