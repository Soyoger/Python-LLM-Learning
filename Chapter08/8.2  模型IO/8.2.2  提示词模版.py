#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/30 18:20
# @Author  : yongjie.su
# @File    : 8.2.2  提示词模版.py
# @Software: PyCharm

"""
PromptTemplate
"""
# from langchain_core.prompts import PromptTemplate
#
# template = """
#     请帮我进行计算：{a} + {b} 的值是多少？
# """
# # 实例化模版方法一，推荐该方法
# prompt = PromptTemplate.from_template(template=template)
# prompt = prompt.format(a=1, b=2)
# print(f"实例化模版方法一: {prompt}")
#
# # 实例化模版方法二
# prompt = PromptTemplate(template=template, input_variables=["a", "b"])
# prompt = prompt.format(a=10, b=20)
# print(f"实例化模版方法二: {prompt}")


"""
FewShotPromptTemplate
"""
# from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
#
# examples = [
#     {"question": "发什么快递？", "answer": "我们是顺丰快递，包邮哦！"},
#     {"question": "尺寸多大呀？", "answer": "我们是尺码都是均码哦！"},
# ]
#
# template = """\t 问题：{question} 答案：{answer}"""
# example_prompt = PromptTemplate(
#     template=template,
#     input_variables=["question", "answer"]
# )
#
# prefix = """
#     角色：直播间虚拟主播
#     功能：回答直播间用户的提问
#     示例：
# """
#
# suffix = """
#     限制：请严格按照直播场景回答问题，忽略不相关问题。
#     接下来，你来回答用户的问题：
# """
# few_shot_prompt = FewShotPromptTemplate(
#     examples=examples,
#     example_prompt=example_prompt,
#     example_separator="\n",
#     prefix=prefix,
#     suffix=suffix,
#     input_variables=["username", "question"]
# )
# few_shot_prompt = few_shot_prompt.format(username="username", question="发什么快递？")
# print(few_shot_prompt)


"""
ChatPromptTemplate
"""
from langchain_core.prompts import (
    ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
)

template = """您是一个非常资深的程序开发工程师，你可以回答任何关于编程的问题。"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = """请帮我解答一下这个问题：{question}"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])
print(f"新的ChatPromptTemplate提示词模版：{chat_prompt}")
chat_prompt = chat_prompt.format_prompt(question="Python为什么需要GIL锁？")
print(f"新的ChatPromptTemplate提示词：{chat_prompt}")
