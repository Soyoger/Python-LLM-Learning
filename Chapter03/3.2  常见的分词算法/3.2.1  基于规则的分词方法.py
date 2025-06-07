#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/30 23:09
# @Author  : yongjie.su
# @File    : 3.2.1  基于规则的分词方法.py
# @Software: PyCharm
class SegmentByDictionary:
    def __init__(self):
        self.dictionary = set()
        self.max_length = self.max_word_length()

    def max_word_length(self):
        """
        获取词典中最长的词的长度
        :return:
        """
        if len(self.dictionary) < 1:
            return 0
        return max(len(word) for word in self.dictionary)

    def add_word(self, word):
        self.dictionary.add(word)
        self.max_length = self.max_length if self.max_length > len(word) else len(word)

    def union_words(self, words: set):
        temp_max_length = max(len(word) for word in words)
        self.dictionary.update(words)
        self.max_length = self.max_length if self.max_length > temp_max_length else temp_max_length

    def cut_by_ffm(self, text):
        """
        正向最大匹配法
        :param text:
        :return:
        """
        # 结果集
        result = []
        # 定义起始位置
        index = 0
        length = len(text)
        while index < length:
            # 尝试匹配最长的词
            for size in range(self.max_length, 0, -1):
                word = text[index:index + size]
                # print(word)
                if word not in self.dictionary:
                    continue
                result.append(word)
                index += size
        return result


if __name__ == '__main__':
    sbd = SegmentByDictionary()
    sbd.add_word('基于')
    sbd.add_word('中文')
    sbd.union_words({'的', '自然语言处理', '分词', '技术'})
    # 打印词典
    print(sbd.dictionary)
    result = sbd.cut_by_ffm("基于中文的自然语言处理分词技术")
    # 打印分词结果
    print(result)
