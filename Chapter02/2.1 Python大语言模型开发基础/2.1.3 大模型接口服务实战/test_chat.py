#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/19 13:29
# @Author  : yongjie.su
# @File    : test_chat.py
# @Software: PyCharm
import time
import requests
import hashlib
from loguru import logger

# 自定义密钥，在请求服务的时候，密钥需要提前安全分发给服务调用的对象
SECRET_KEY = "chat-gpt"


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


def do_post(url, secret_key, prompt, role='user', temperature=0.1, model='gpt-3.5-turbo'):
    timestamp = int(time.time())
    sign = get_sign(secret_key, timestamp)
    data = {
        "timestamp": timestamp,
        "auth_token": sign,
        "prompt": prompt,
        "role": role,
        "temperature": temperature,
        "model": model
    }
    try:
        response = requests.post(url, json=data, timeout=10).json()
        code = response.get('code')
        logger.info(response)
        if code == 0:
            return response.get('data')
        else:
            logger.error(f"服务返回失败，{code=}")
    except Exception as e:
        logger.error(f"服务调用异常：{e=}")
    return '我无法回答'


if __name__ == "__main__":
    # host:port 需要替换成你的云主机IP:端口
    url = "http://127.0.0.1:8088/chat"
    prompt = "假如你是一个中文自然语言处理的专家，请帮我把下面这段话进行分词，然后返回一个分级结果集，需要分词的这段话是：人工智能是最近几年非常热门的计算机技术。"
    result = do_post(url, SECRET_KEY, prompt)
    logger.info(result)
