#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/5 22:54
# @Author  : yongjie.su
# @File    : 6.3.5  使用提示词进行文本摘要.py
# @Software: PyCharm
from Chapter06.chatgpt_base import do_request

if __name__ == "__main__":
    text = "文旅市场热度持续攀升，点燃“假日经济”的消费新活力。在重庆，各大景区纷纷推出数百场以“粽”为主题的文旅活动，赛龙舟、包粽子、制香囊等让市民游客沉浸式体验传统文化魅力；在广东，佛山凭借非物质文化遗产项目“叠滘赛龙舟”，成为今年端午假期的热门“民俗小城”；在福建泉州等地，民俗踩街、王爷船巡海仪式等地方特色节庆活动也吸引了众多游客。"

    prompt = f"""
        身份：资深文本摘要提取专家 
        任务：从给定的文本中提取内容摘要。
        输出：使用JSON格式输出，结果使用键summary，值为摘要结果。
        文本内容：{text}
        限制：对文本内容进行摘要，要做到精炼不重复，字数不超过30字。
    """
    is_success, result = do_request(prompt)
    print(result)
    # {
    #     "summary": "文旅市场热度持续攀升，重庆景区推出粽主题活动；广东佛山叠滘赛龙舟成热门；福建泉州民俗节庆吸引游客。"
    # }
