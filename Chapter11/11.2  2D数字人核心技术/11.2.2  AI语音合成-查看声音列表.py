#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 13:08
# @Author  : yongjie.su
# @File    : 11.2.2  AI语音合成-查看声音列表.py
# @Software: PyCharm
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 11:58
# @Author  : yongjie.su
# @File    : 11.2.2  AI语音合成.py
# @Software: PyCharm
# edge-tts --list-voices
import asyncio
import edge_tts


async def get_voices():
    voices = await edge_tts.list_voices()
    return voices


if __name__ == "__main__":
    voices = asyncio.run(get_voices())
    print(voices)
