#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 18:52
# @Author  : yongjie.su
# @File    : 13.2.1  传统分类器的训练.py
# @Software: PyCharm
import jieba
import pandas as pd
from sklearn.model_selection import train_test_split

# 加载数据
waimai_10k_df = pd.read_csv('waimai_10k.csv')

# 1. 读取数据
df = pd.read_csv('waimai_10k.csv')

# 2. 随机切分数据集，比例为 70% 训练集，30% 测试集
train_df, test_df = train_test_split(df, test_size=0.4, random_state=100)

# 输出数据集的大小
print(f'Training set size: {len(train_df)}')
print(f'Test set size: {len(test_df)}')

x_train = train_df['review'].values.tolist()
y_train = train_df['label'].values.tolist()
x_test = test_df['review'].values.tolist()
y_test = test_df['label'].values.tolist()


# 定义文件读取函数
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


stop_words_path = "stopwords.txt"
stop_words = read_text_file(stop_words_path)
stop_words = [stop_word.replace("\n", '') for stop_word in stop_words]


def filter_stop_words(lines):
    new_lines = []
    for line in lines:
        try:
            segs = jieba.lcut(line)
            # 去数字
            segs = [v for v in segs if not str(v).isdigit()]
            # 去左右空格
            segs = list(filter(lambda x: x.strip(), segs))
            # 去掉停用词
            segs = list(filter(lambda x: x not in stop_words, segs))
            new_lines.append(" ".join(segs))
        except Exception:
            print(line)
            continue
    return new_lines


x_train = filter_stop_words(x_train)
x_test = filter_stop_words(x_test)

from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer(
    analyzer='word',
    max_features=4000,
)
vec.fit(x_train)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(vec.transform(x_train), y_train)

pre = classifier.predict(vec.transform(x_test))
print(classifier.score(vec.transform(x_test), y_test))
# from sklearn.metrics import precision_score, recall_score, f1_score

# 计算并输出精确率、召回率和F1得分
# precision = precision_score(y_test, pre, average='weighted')
# recall = recall_score(y_test, pre, average='weighted')
# f1 = f1_score(y_test, pre, average='weighted')
#
# print(f"Precision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")
# print(f"F1 Score: {f1:.4f}")
from sklearn.metrics import classification_report

report = classification_report(y_test, pre)
print(report)
