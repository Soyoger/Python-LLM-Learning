#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/3 22:23
# @Author  : yongjie.su
# @File    : chatgpt_base.py
# @Software: PyCharm
from openai import OpenAI

# 代理地址
OPENAI_API_BASE = "https://api.openai-proxy.org/v1"
OPENAI_API_KEY = "sk-2KExxx"
if OPENAI_API_BASE is None or OPENAI_API_BASE == "":
    OPENAI_API_BASE = f"https://api.openai.com/v1"


def send_message(messages, temperature=0.1, model='gpt-3.5-turbo'):
    client = OpenAI(
        base_url=OPENAI_API_BASE,
        api_key=OPENAI_API_KEY
    )
    if "GPT4" in model:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=temperature,
            max_tokens=2048,

        )
    else:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stop=None,
            temperature=temperature,
        )
    for choice in response.choices:
        if "text" in choice:
            return choice.text
    return response.choices[0].message.content


def do_request(prompt, role='user', temperature=0.1, model='gpt-3.5-turbo'):
    messages = [{"role": role, "content": prompt}]
    is_success = False
    try:
        content = send_message(messages, temperature=temperature, model=model)
        is_success = True
        return is_success, content
    except Exception as err:
        content = f"Error: {err=}"
    return is_success, content
