#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/14 22:58
# @Author  : yongjie.su
# @File    : 4.2.1  One-Hot编码.py
# @Software: PyCharm
import pandas as pd

# 准备数据集
data = ['大数据', '云技术', '机器学习', '深度学习', '大语言模型']
df = pd.DataFrame({'人工智能技术': data})


# 方法一
def get_dummies(dataframe: pd.DataFrame):
    dummies = pd.get_dummies(dataframe['人工智能技术'], prefix='人工智能技术', dtype=int)
    # print(dummies)
    return dummies


def get_one_hot_by_apply(dataframe: pd.DataFrame):
    one_hot_df = pd.DataFrame()
    col_name = '人工智能技术'
    for value in dataframe[col_name].unique():
        new_col = f'{col_name}_{value}'
        one_hot_df[new_col] = dataframe['人工智能技术'].apply(lambda x: 1 if x == value else 0)
    # print(one_hot_df)
    return one_hot_df


def get_one_hot_by_pytorch(items: list):
    import torch
    from torch.nn import functional
    # 为每个类别创建一个唯一的索引（整数）
    item_to_index = {item: index for index, item in enumerate(items)}
    # 将标签字符串转换为对应的整数索引
    labels_indices = torch.tensor([item_to_index[item] for item in items])
    # 使用PyTorch的functional.one_hot生成one-hot编码
    one_hot = functional.one_hot(labels_indices, num_classes=len(data))
    # 默认LongTensor类型
    # ndarray类型：one_hot.numpy()
    # list类型：one_hot.numpy().tolist()
    return one_hot


if __name__ == '__main__':
    # 使用get_dummies函数构建
    print(get_dummies(df))
    # 通过apply构建
    print(get_one_hot_by_apply(df))
    # 通过pytorch构建
    print(get_one_hot_by_pytorch(data))
