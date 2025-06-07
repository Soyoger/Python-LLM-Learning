#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 11:12
# @Author  : yongjie.su
# @File    : 10.2.3  基于CPU部署Qwen2-0.5B.py
# @Software: PyCharm
from transformers import AutoTokenizer, Qwen2ForCausalLM

tokenizer = AutoTokenizer.from_pretrained("../Qwen2-0.5B", trust_remote_code=True)
model = Qwen2ForCausalLM.from_pretrained("../Qwen2-0.5B", trust_remote_code=True).cpu().float()

device = "cpu"

prompt = "请帮我写一首李白的诗。"


def encode_prompt(prompt: str):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    return tokenizer([text], return_tensors="pt").to(device)


def decode_ids(generated_ids: list):
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in
        zip(model_inputs.input_ids, generated_ids)
    ]
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


model_inputs = encode_prompt(prompt)
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512,
)
result = decode_ids(generated_ids)
print(result)
