#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 11:16
# @Author  : yongjie.su
# @File    : 10.2.3 基于CPU部署Qwen2-0.5B_pipeline.py
# @Software: PyCharm
from transformers import AutoTokenizer, Qwen2ForCausalLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("../Qwen2-0.5B", trust_remote_code=True)
model = Qwen2ForCausalLM.from_pretrained("../Qwen2-0.5B", trust_remote_code=True).cpu().float()


def answer_question(question):
    output = pipeline("text-generation", model=model, tokenizer=tokenizer)(question)
    return output[0]['generated_text']


question = "中国的首都是哪里？"
answer = answer_question(question)
print(answer)
