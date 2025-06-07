#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/17 10:01
# @Author  : yongjie.su
# @File    : 13.2.3  定制化微调预训练模型.py
# @Software: PyCharm
import json
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("直播间提问数据集.csv")

train_df, test_df = train_test_split(df, test_size=0.3, random_state=100)


def prepare_fine_tunes_data(datasets: list, output_file="result.jsonl"):
    system_content = "你是一位直播间提问判断有效无效的资深专家。"
    system_content = {"role": "system", "content": system_content}
    with open(output_file, 'w', encoding='utf-8') as fd:
        for dataset in datasets:
            messages = [system_content]

            question = dataset.get('问题')
            user_content = {"role": "user", "content": question}
            messages.append(user_content)

            is_valid = dataset.get('是否有效')
            is_valid_reason = dataset.get('评判依据')
            assistant_content = {
                "role": "assistant",
                "content": f"是否有效：{is_valid}，评判依据：{is_valid_reason}"
            }
            messages.append(assistant_content)
            row = {
                "messages": messages
            }
            row_dumps = json.dumps(row, ensure_ascii=False)
            fd.write(row_dumps + "\n")


train_file = "train.jsonl"
test_file = "test.jsonl"

prepare_fine_tunes_data(train_df.to_dict(orient='records'), train_file)
prepare_fine_tunes_data(test_df.to_dict(orient='records'), test_file)
