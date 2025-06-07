#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 15:53
# @Author  : yongjie.su
# @File    : 6.3.2  使用提示词提取关键词.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    text = "数字人是运用AI数字技术创造出来的，与人类形象接近的数字化人物形象。"
    prompt = f"""
        身份：资深自然语言处理专家 
        任务：从给定的文本中提取关键词
        输出：使用JSON格式输出，结果使用键keywords，值为关键词列表。
        文本内容：{text}
        限制：如果关键词比较多，输出最重要的5个关键词即可。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "keywords": ["数字人", "AI数字技术", "数字化人物形象"]
    # }