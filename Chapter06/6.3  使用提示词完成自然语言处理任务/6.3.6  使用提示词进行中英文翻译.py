#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 22:54
# @Author  : yongjie.su
# @File    : 6.3.6  使用提示词进行中英文翻译.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    text = "数字人是运用AI数字技术创造出来的，与人类形象接近的数字化人物形象。"

    prompt = f"""
        身份：资深中英文翻译专家
        任务：把给定的中文文本翻译成标准的美式英文。
        输出：使用JSON格式输出，结果使用键result，值为翻译结果。
        文本内容：{text}
        限制：只做中英文翻译，用词和表达必须准确无误。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "result": "Digital humans are created using AI digital technology, resembling human-like digital characters."
    # }
