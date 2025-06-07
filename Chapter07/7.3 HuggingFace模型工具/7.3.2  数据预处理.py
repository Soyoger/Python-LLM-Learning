#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 11:06
# @Author  : yongjie.su
# @File    : 7.3.2  数据预处理.py
# @Software: PyCharm
# 自然语言处理
# from transformers import AutoTokenizer
#
# tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
# encoded_input = tokenizer("2024年是人工智能应用爆发的一年，这一年全球AI爱好者开发出很多有趣的AI应用！")
# print(encoded_input)

# 图片处理
# from PIL import Image
# from transformers import AutoImageProcessor
#
# image_path = "cat.jpg"
# image = Image.open(image_path)
# processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
# inputs = processor(images=image, return_tensors="pt")
# print(inputs)


# 音频处理
# import wave
# import numpy as np
# from transformers import AutoFeatureExtractor
#
#
# def get_wav_data(audio_path):
#     with wave.open(audio_path, 'rb') as wav_file:
#         n_frames = wav_file.getnframes()
#         # 读取音频数据
#         frames = wav_file.readframes(n_frames)
#         # 将音频数据转换为 numpy 数组
#         wave_form = np.frombuffer(frames, dtype=np.int16)
#         print(wave_form)
#         return wave_form
#
#
# audio_path = "./audio.wav"
# audio_input = get_wav_data(audio_path)
#
# feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base")
#
# # sampling_rate 指每秒测量语音信号中的数据点数，16kHz。
# results = feature_extractor(audio_input, sampling_rate=16000)
# print(f"数据大小：{results['input_values'][0].shape}")
# print(results)


# 多模态
from datasets import load_dataset, Audio

lj_speech = load_dataset("lj_speech", split="train", trust_remote_code=True)
lj_speech = lj_speech.map(remove_columns=["file", "id", "normalized_text"])

print(lj_speech[0]["audio"])

print(lj_speech[0]["text"])

lj_speech = lj_speech.cast_column("audio", Audio(sampling_rate=16_000))

from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")


def prepare_dataset(example):
    audio = example["audio"]

    example.update(processor(audio=audio["array"], text=example["text"], sampling_rate=16000))

    return example


result = prepare_dataset(lj_speech[0])
print(result)
