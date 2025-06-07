#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 22:53
# @Author  : yongjie.su
# @File    : 6.3.3  使用提示词进行文本分类.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    texts = [
        '四大技术路径角逐固态电池 实现产业化仍任重道远',
        'AI Agent：超级员工将至',
        '雷军给准大学生的建议，你们认可吗？',
        '教育是教创造知识不是接受知识',
        '端午假期数据显示传统景区后劲十足'
    ]
    categories = ['汽车', '科技', '教育', '旅游']
    contents = [f'{idx + 1}、{text} \n' for idx, text in enumerate(texts)]

    prompt = f"""
        身份：资深文本分类专家 
        任务：按照提供的分类类别把新闻标题进行分类。
        输出：使用JSON格式输出，结果使用键category，值为分类类别。
        分类类别：{'、'.join(categories)}
        文本内容：{''.join(contents)}
        限制：每个新闻标题只属于一个最相关的分类，如果无法匹配到合适的分类，默认用其他。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "1": {
    #         "category": "科技"
    #     },
    #     "2": {
    #         "category": "科技"
    #     },
    #     "3": {
    #         "category": "教育"
    #     },
    #     "4": {
    #         "category": "教育"
    #     },
    #     "5": {
    #         "category": "旅游"
    #     }
    # }
