#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/19 14:40
# @Author  : yongjie.su
# @File    : 基于Streamlit框架的网页部署.py
# @Software: PyCharm
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModel

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


def chat(question, history=[]):
    prompt = f"""
            任务：回答下面问题。
            问题：{question}
            限制：只告诉我答案，无关内容都不需要。        
    """
    response, history = model.chat(tokenizer, prompt, history=[])
    return response


st.title('Chat Bot')

prompt = st.chat_input("Chat something")
if prompt:
    st.text(f"提问：{prompt}")
    with st.status("running", expanded=True, state='running') as status:
        result = chat(prompt)
        st.text(result)
        status.update(label="请继续提问或者结束会话！", state="complete", expanded=True)
