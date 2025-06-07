#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 23:11
# @Author  : yongjie.su
# @File    : 4.2.2 Word2Vec模型.py
# @Software: PyCharm
import jieba
from gensim.models import Word2Vec


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
    sentences = [
        "这部电影非常精彩，剧情好看，演员非常出色。"
    ]
    # 分词
    # jieba.add_word("人工智能")
    segments = [jieba.lcut(sentence) for sentence in sentences]
    print(segments)
    # 去停用词
    tokenizeds = [[word for word in segment if word not in stop_words] for segment in segments]
    print(tokenizeds)

    model = Word2Vec(
        tokenizeds,
        sg=1,
        vector_size=20,
        window=5,
        min_count=1,
        hs=1
    )
    # 保存模型
    model.save('word2vec.model')
    # 加载模型
    model = Word2Vec.load('word2vec.model')

    # 查看特定词的词向量
    embedding = model.wv['精彩']
    print(embedding)
    # 查看类似于某个词的词
    most_similar = model.wv.most_similar("精彩", topn=3)
    print(most_similar)
    # 相似度判断
    similarity = model.wv.similarity('精彩', '精彩')
    print(f"相似度是：{similarity}")
