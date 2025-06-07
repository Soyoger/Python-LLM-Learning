#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 11:58
# @Author  : yongjie.su
# @File    : 11.2.2  AI语音合成.py
# @Software: PyCharm
# edge-tts --voice zh-CN-XiaoxiaoNeural --text "大家好，这是测试。" --write-media hello_test.mp3
import asyncio
import edge_tts


async def tts(words, voice, output, **kwargs) -> None:
    """
    生成tts
    :return:
    """
    rate = kwargs.get('rate', "+0%")
    volume = kwargs.get('volume', "+0%")
    communicate = edge_tts.Communicate(words, voice, rate=rate, volume=volume)
    await communicate.save(output)


if __name__ == "__main__":
    words = "大家好，这是测试。"
    voice = "zh-CN-XiaoxiaoNeural"
    output = "hello_test.mp3"
    kwargs = {}
    asyncio.run(tts(words, voice, output, **kwargs))
