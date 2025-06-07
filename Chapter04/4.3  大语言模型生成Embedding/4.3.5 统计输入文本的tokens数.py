#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 17:38
# @Author  : yongjie.su
# @File    : 4.3.5 统计输入文本的tokens数.py
# @Software: PyCharm
import tiktoken


def encoding_for_model(text: str, model_name="gpt-3.5-turbo"):
    """
    使用tiktoken.encoding_for_model()方法，自动加载给定模型名称对应的正确编码。
    :param text:
    :param model_name:
    :return:
    """
    encoding = tiktoken.encoding_for_model(model_name)
    return encoding.encode(text)


def decoding_for_model(ids: list, model_name="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model_name)
    return encoding.decode(ids)


def num_tokens_from_string(text: str, encoding_name="cl100k_base") -> int:
    """
    返回输入文本的tokens个数
    第二代嵌入模型，如text-embedding-ad-002，请使用cl100k_base编码。
    :param text: 输入的文本内容
    :param encoding_name: 默认编码器：cl100k_base
    :return:
    """
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


if __name__ == '__main__':
    # 文本字符串转换为标记整数列表
    text = "Hello OpenAI"
    ids = encoding_for_model(text)
    print(ids)
    # 标记整数列表转换成文本
    text = decoding_for_model(ids)
    print(text)
    # 统计tokens数
    num_tokens = num_tokens_from_string(text)
    print(num_tokens)
