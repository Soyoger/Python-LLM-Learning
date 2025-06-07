#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 20:35
# @Author  : yongjie.su
# @File    : 基于Streamlit框架的网页部署.py
# @Software: PyCharm
import streamlit as st
import pandas as pd

# 设置测试标题
st.title('Demo')
st.text('显示一个DataFrame:')

# 创建一个DataFrame
data = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [5, 6, 7, 8]
})

# 在应用程序中显示DataFrame
st.write(data)
