#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 20:30
# @Author  : yongjie.su
# @File    : 10.3.1  基于Gradio框架的网页部署.py
# @Software: PyCharm
import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModel

print(gr.__version__)

if torch.cuda.is_available():
    print("CUDA is available!")
else:
    print("CUDA is not available.")

chatglm_6b_path = "chatglm3-6b"

tokenizer = AutoTokenizer.from_pretrained(chatglm_6b_path, trust_remote_code=True)
with torch.no_grad():
    model = AutoModel.from_pretrained(
        chatglm_6b_path,
        trust_remote_code=True
    ).half().cuda()

model = model.eval()


def chat(question, history):
    prompt = f"""
            任务：回答下面问题。
            问题：{question}
            限制：只告诉我答案，无关内容都不需要。        
    """
    response, history = model.chat(tokenizer, prompt, history=[])
    return response


gr_chat = gr.ChatInterface(
    fn=chat,
    examples=["您好呀", "你是谁？"],
    title="基于ChatGLM3-6B的聊天机器人"
)

gr_chat.launch(share=True)
