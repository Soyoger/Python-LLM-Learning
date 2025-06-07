#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 23:31
# @Author  : yongjie.su
# @File    : 3.1.4 制作词云图.py
# @Software: PyCharm
import jieba
from PIL import Image
import numpy as np
from collections import Counter
from wordcloud import WordCloud


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines


if __name__ == "__main__":
    # 加载停用词
    stop_words_path = "stopwords.txt"
    stop_words = read_text_file(stop_words_path)
    stop_words = [stop_word.replace("\n", '') for stop_word in stop_words]
    # 加载文档
    text_file_path = '2023生成式大模型安全与隐私白皮书.txt'
    lines = read_text_file(text_file_path)
    # 分词 并去停用词
    segments = []
    for line in lines:
        if line == '\n':
            continue
        if len(str(line).strip()) <= 1:
            continue
        line = line.replace('\n', '')
        segs = jieba.lcut(line, cut_all=False)
        # 去停用词
        segs = list(set(segs) - set(stop_words))
        segments.extend(segs)
    # 统计，获取分词结果中词列表的 top n
    segments = [segment for segment in segments if segment.strip() != '']
    result = dict(Counter(segments))
    # 绘图
    # 加载背景图片
    img = Image.open('background.png')
    # 将图片变为数组，便于用作词云图形状
    img_array = np.array(img)
    wordcloud = WordCloud(
        # mask=img_array,  # 设置背景图，上面已经加载
        # 设置字体和大小,这里使用黑体
        font_path="SimHei.ttf",
        # 词云图中词语字号最大值
        max_font_size=70,
        # 词云图中词语字号最小值
        min_font_size=7,
        # 设置词语数量
        max_words=100,
        # 当 max_words 超过总词数，是否使用重复的词语代替
        repeat=True,
        # 设置背景颜色为白色
        background_color="white",
        # 设置宽和高
        width=500,
        height=400
    ).generate_from_frequencies(result)
    # 将词云图保存到
    wordcloud.to_file('wordcloud.png')
