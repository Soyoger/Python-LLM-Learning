#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/9 22:38
# @Author  : yongjie.su
# @File    : 4.1-1 Jieba构建词袋模型.py
# @Software: PyCharm
import jieba


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines


def get_stop_words(file_path):
    lines = read_text_file(file_path)
    stop_words = [line.replace("\n", '') for line in lines]
    return stop_words


if __name__ == '__main__':
    stop_words_path = "stopwords.txt"
    stop_words = get_stop_words(stop_words_path)
    content = [
        "机器学习推动人工智能的飞速发展。",
        "深度学习使人工智能变得更加强大。",
        "大语言模型让人工智能更加的智能。"
    ]
    # 分词
    jieba.add_word('大语言模型')
    segments = [jieba.lcut(con) for con in content]
    print(segments)
    # 去停用词
    tokenizeds = [[word for word in segment if word not in stop_words] for segment in segments]
    print(tokenizeds)
    # 分词结果放到一个袋子（List）里面，也就是取并集，再去重，获取对应的特征词。
    bag_of_words = list(set([word for words in tokenizeds for word in words]))
    print(bag_of_words)
    # 构建词袋模型
    bag_of_word2vec = [[1 if token in tokenized else 0 for token in bag_of_words] for tokenized in
                       tokenizeds]
    print(bag_of_word2vec)
