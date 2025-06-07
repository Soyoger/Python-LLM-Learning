#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/3 22:19
# @Author  : yongjie.su
# @File    : 6.3.1  使用提示词进行分词.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    text = "2024年是大模型应用的元年，全球将会出现非常多有趣的AI应用。"
    prompt = f"""
        身份：资深自然语言处理专家 
        任务：进行文本内容分词
        输出：使用JSON格式输出，结果使用键words，值为分词结果，分词结果使用空格隔开。
        文本内容：{text}
        限制：只进行分词，拒绝回答其他无关问题。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "words": "2024年 是 大 模型 应用 的 元年，全球 将会 出现 非常 多 有趣 的 AI 应用。"
    # }
