#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 22:34
# @Author  : yongjie.su
# @File    : 3.2.2  基于统计的分词方法.py
# @Software: PyCharm
def n_grams(num, text, language='english'):
    if num < 1:
        raise ValueError("不合法的n值！")
    if text is None or text == '':
        return []
    if language != 'english':
        raise ValueError('暂不支持该语言！')
    inputs = text.split(' ')
    result = [inputs[i: i + num] for i in range(len(inputs) - num + 1)]
    return result


if __name__ == "__main__":
    # 自定义的方法
    sentence = "Tokenization is a crucial step in natural language processing."
    print(n_grams(2, sentence, language='english'))

    # nltk工具包
    import nltk

    tokens = nltk.word_tokenize(sentence)
    bi_grams = nltk.bigrams(tokens)
    print(list(bi_grams))
    tri_grams = nltk.trigrams(tokens)
    print(list(tri_grams))
