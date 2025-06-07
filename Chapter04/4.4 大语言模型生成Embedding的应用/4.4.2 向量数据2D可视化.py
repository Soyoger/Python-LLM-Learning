#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/1/24 16:39
# @Author  : yongjie.su
# @File    : 4.4.2 向量数据2D可视化.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('Reviews_embeddings.csv')
matrix = np.array(df.ada_embedding.apply(eval).to_list())

model = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
vis_dims = model.fit_transform(matrix)

colors = ["red", "darkorange", "gold", "blue", "darkgreen"]
x = [x for x, _ in vis_dims]
y = [y for _, y in vis_dims]
color_indices = df.Score.values - 1
colormap = matplotlib.colors.ListedColormap(colors)
plt.scatter(x, y, c=color_indices, cmap=colormap, alpha=0.3)
# for score in [0, 1, 2, 3, 4]:
#     avg_x = np.array(x)[df.Score - 1 == score].mean()
#     avg_y = np.array(y)[df.Score - 1 == score].mean()
#     color = colors[score]
#     plt.scatter(avg_x, avg_y, marker='x', color=color, s=100)
plt.savefig("2D结果.png")
plt.show()