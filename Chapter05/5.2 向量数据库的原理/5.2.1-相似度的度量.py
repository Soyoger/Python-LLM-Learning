#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/3/4 22:25
# @Author  : yongjie.su
# @File    : 5.2.1-相似度的度量.py
# @Software: PyCharm
from scipy.spatial import distance


def euclidean_distance(v1, v2):
    """
    欧拉距离
    :param v1:
    :param v2:
    :return:
    """
    return distance.euclidean(v1, v2)


def manhattan_distance(v1, v2):
    """
    曼哈顿距离
    :param v1:
    :param v2:
    :return:
    """
    return distance.cityblock(v1, v2)


def hamming_distance(v1, v2):
    """
    汉明距离
    :param v1:
    :param v2:
    :return:
    """
    return distance.hamming(v1, v2)


def chebyshev_distance(v1, v2):
    """
    切比雪夫距离
    :param v1:
    :param v2:
    :return:
    """
    return distance.chebyshev(v1, v2)


def cosine_similarity(v1, v2):
    """
    余弦相似度
    :param v1:
    :param v2:
    :return:
    """
    return distance.cosine(v1, v2)


if __name__ == '__main__':
    v1 = [1, 1, 0]
    v2 = [1, 0, 1]
    print(euclidean_distance(v1, v2))
    print(manhattan_distance(v1, v2))
    print(hamming_distance(v1, v2))
    print(chebyshev_distance(v1, v2))
    print(cosine_similarity(v1, v2))
