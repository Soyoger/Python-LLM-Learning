#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 20:30
# @Author  : yongjie.su
# @File    : 10.3.1  构建第一个Gradio应用.py
# @Software: PyCharm
import random
import gradio as gr

print(gr.__version__)


def chat(question, history):
    if question != '摇一摇':
        return "输入错误，请重新输入：摇一摇"
    result = random.choice([1, 2, 3, 4, 5, 6])
    output = f"结果是：{result}"
    return output


gr_chat = gr.ChatInterface(
    fn=chat,
    examples=["摇一摇"],
    title="ChatBot"
)

gr_chat.launch(share=True)
