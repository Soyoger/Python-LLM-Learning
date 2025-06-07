#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 13:02
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/4 15:25
# @Software: PyCharm
import time
import hashlib
from openai import OpenAI
from loguru import logger
from flask import Flask, request

# 定义 OpenAI api_key
OPENAI_API_KEY = "sk-pGRxxx"
# 自定义密钥，在请求服务的时候，密钥需要提前安全分发给服务调用的对象
SECRET_KEY = "chat-gpt"

app = Flask(__name__)
# 设置显示中文，而非unicode码
app.json.ensure_ascii = False


@app.route("/health", methods=["GET"])
def health():
    """
    健康检查服务
    :return:
    """
    timestamp = int(time.time())
    return dict(code=0, timestamp=timestamp, data=None, message="成功")


def get_md5(plaintext: str):
    """
    计算md5
    :param plaintext:
    :return:
    """
    return hashlib.md5(plaintext.encode('utf-8')).hexdigest()


def get_sign(secret_key, timestamp):
    """
    接口认证的简单加密算法
    :param secret_key: 用户共享的密钥
    :param timestamp: 时间戳
    :return:
    """
    plaintext = "openai".join([secret_key, str(timestamp)])
    sign = get_md5(plaintext)
    logger.info(f"{timestamp=} {plaintext=} {sign=}")
    return sign


def verify_token(secret_key, timestamp, auth_token):
    """
    进行auth_token的认证
    :param secret_key: 用户共享的密钥
    :param timestamp: 时间戳
    :param auth_token: 认证
    :return: 返回认证结果，bool类型
    """
    sign = get_sign(secret_key, timestamp)
    return sign == auth_token


def send_message(messages, temperature=0.1, model='gpt-3.5-turbo'):
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )
    if "GPT4" in model:
        response = client.chat.completions.create(
            model=model,
            response_format={"type": "json_object"},
            temperature=temperature,
            max_tokens=2048,
            messages=messages
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


@app.route('/chat', methods=['POST'])
def get_chat():
    try:
        data = request.get_json()
        timestamp = data.get('timestamp')
        auth_token = data.get('auth_token')
        is_verify = verify_token(SECRET_KEY, timestamp, auth_token)
        if not is_verify:
            return dict(code=-2, timestamp=int(time.time()), data=None, message=f"认证失败")
        prompt = data.get('prompt')
        temperature = data.get('temperature', 0.1)
        model = data.get('model', 'gpt-3.5-turbo')
        role = data.get('role', 'user')
        messages = [{"role": role, "content": prompt}]
        response = send_message(messages, temperature, model)
        return dict(code=0, timestamp=int(time.time()), data=response, message="成功")
    except Exception as e:
        logger.error(f"请求ChatGPT失败：{e=}")
        return dict(code=-1, timestamp=int(time.time()), data='我无法回答', message=f"失败，{e=}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8088, debug=False)
