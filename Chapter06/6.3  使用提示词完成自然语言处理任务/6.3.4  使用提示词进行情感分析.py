#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 22:53
# @Author  : yongjie.su
# @File    : 6.3.4  使用提示词进行情感分析.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    comments = [
        '物流很快，包装精美，上门送货，非常喜欢。',
        '味道一般，当早餐吃还可以。',
        '口味太甜了，有点腻。',
        '拿到快递后，包装是破损的，里面的东西丢失了一部分。',
        '尺码偏大，而且颜色与介绍中的不一致，退货了。'
    ]
    contents = [f'{idx + 1}、{comment} \n' for idx, comment in enumerate(comments)]
    prompt = f"""
        身份：资深文本情感分析专家 
        任务：对给定的文本进行情感分析，判断文本的情感标签属于积极、中性还是消极，并给出一个0-1范围的得分。
        输出：使用JSON格式输出：情感标签使用键label，值为情感标签结果；情感得分使用键score，值为得分值。
        文本内容：{''.join(contents)}
        限制：只进行情感分析，不执行其他额外操作，结果仅包含label和score。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "results": [
    #         {
    #             "label": "积极",
    #             "score": 0.9
    #         },
    #         {
    #             "label": "中性",
    #             "score": 0.5
    #         },
    #         {
    #             "label": "消极",
    #             "score": 0.3
    #         },
    #         {
    #             "label": "消极",
    #             "score": 0.2
    #         },
    #         {
    #             "label": "消极",
    #             "score": 0.4
    #         }
    #     ]
    # }

