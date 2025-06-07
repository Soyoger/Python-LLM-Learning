#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/25 23:46
# @Author  : yongjie.su
# @File    : 3.1.3 中文分词.py
# @Software: PyCharm
import jieba

sentence = "2023年度十大新词语是：生成式人工智能、全球文明倡议、村超、新质生产力、全国生态日、消费提振年、特种兵式旅游、显眼包、百模大战、墨子巡天。"

# 精确模式
# accurate_mode_segments = jieba.cut(sentence, cut_all=False, HMM=True)
# print(list(accurate_mode_segments))
# accurate_mode_segments = jieba.cut(sentence, cut_all=False, HMM=False)
# print(list(accurate_mode_segments))

# 全模式
# cut_all_mode_segments = jieba.cut(sentence, cut_all=True)
# print(list(cut_all_mode_segments))

# 搜索引擎模式
# search_mode_segments = jieba.cut_for_search(sentence)
# print(list(search_mode_segments))

# paddle模式
# jieba.enable_paddle()
# accurate_mode_segments = jieba.cut(sentence, cut_all=False, use_paddle=True)
# print(list(accurate_mode_segments))


# jieba.add_word('生成式人工智能')
# jieba.add_word('新质生产力')

jieba.load_userdict('user_dict.txt')

if __name__ == '__main__':
    # parallel模式
    jieba.enable_parallel(2)
    sentence = "2023年度十大新词语是：生成式人工智能、全球文明倡议、村超、新质生产力、全国生态日、消费提振年、" + "\n" + "特种兵式旅游、显眼包、百模大战、墨子巡天。"
    accurate_mode_segments = jieba.cut(sentence, cut_all=False)
    print(list(accurate_mode_segments))
