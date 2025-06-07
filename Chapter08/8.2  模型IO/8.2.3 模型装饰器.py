#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 18:20
# @Author  : yongjie.su
# @File    : 8.2.3 模型装饰器.py
# @Software: PyCharm
# 大语言模型
import json
from typing import Optional, List, Any, Iterator, Union, Dict, Type

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import LanguageModelInput
from langchain_core.outputs import GenerationChunk
from langchain_core.runnables import Runnable
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel

azure_endpoint = "https://internal-xxx.openai.azure.com/"
# azure 官网获取
openai_api_key = "eeexxx"

azure_chat = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key)

# prompt = f"""
#     功能：告诉我一个中文笑话。
#     限制：字数20字以内。
# """
# response = azure_chat.invoke(prompt)
# print(response.content)

# 大语言模型的缓存
import time
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache

# 第一次执行
# start = time.time()
# prompt = f"""
#     功能：告诉我一个中文笑话。
#     限制：字数20字以内。
# """
# set_llm_cache(InMemoryCache())
# response = azure_chat.invoke(prompt)
# print(response.content)
# end = time.time()
# print(f"未使用缓存，请求耗时：{end - start}")

# 第二次执行
# start = time.time()
# prompt = f"""
#     功能：告诉我一个中文笑话。
#     限制：字数20字以内。
# """
# response = azure_chat.invoke(prompt)
# print(response.content)
# end = time.time()
# print(f"已使用缓存，请求耗时：{end - start}")

# 大语言模型函数调用
from langchain.tools import tool

# @tool
# def search_api(query: str) -> str:
#     """
#     Searches the API for the query.
#     """
#     return f"这是{query}测试结果"

# 定义工具
# @tool("search", return_direct=True)
# def search_api(query: str) -> str:
#     """
#     接入工具。如从API结构处查询。
#     """
#     return f"查询{query}得到: 苹果"
#
#
# tools = [search_api]
# llm_with_tools = azure_chat.bind_tools(tools)
# prompt = f"请使用中文随机说一个水果的名字。"
# tool_calls_outputs = llm_with_tools.invoke(prompt).tool_calls
# print(tool_calls_outputs)
# result = search_api.invoke(tool_calls_outputs[0]['args'])
# print(result)

# 自定义大语言模型
from transformers import pipeline


def sentiment_analysis(prompt):
    """
    进行情感分析
    :param prompt:
    :return:
    """
    pipe = pipeline(task="text-classification", trust_remote_code=True)
    result = pipe(prompt)
    return json.dumps(result, ensure_ascii=False)


from langchain_core.language_models.llms import LLM


class MyOpenLLM(LLM):

    def with_structured_output(
            self,
            schema: Union[Dict, Type[BaseModel]],
            **kwargs: Any
    ) -> Runnable[LanguageModelInput, Union[Dict, BaseModel]]:
        ...

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any
    ) -> str:
        """在给定输入上运行LLM。

        重写此方法以实现LLM逻辑。

        参数:
            prompt: 用于生成的提示。
            stop: 生成时使用的停用词。 模型输出在任何停止子串的第一次出现时被截断。
                如果不支持停用词，请考虑引发NotImplementedError。
            run_manager: 运行的回调管理器。
            **kwargs: 任意额外的关键字参数。 通常传递给模型提供者API调用。

        返回:
            模型输出作为字符串。 实际完成不应包括提示。
        """
        if stop is not None:
            raise ValueError("不允许使用停用词参数。")
        context = sentiment_analysis(prompt)
        return context

    def _stream(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any
    ) -> Iterator[GenerationChunk]:
        """在给定提示上流式传输LLM。

        应该由支持流传输的子类重写此方法。

        如果没有实现，对流进行调用的默认行为将是退回到模型的非流版本并返回
        作为单个块的输出。

        参数:
            prompt: 生成的提示。
            stop: 生成时使用的停用词。 模型输出在任何这些子字符串的第一次出现时被截断。
            run_manager: 运行的回调管理器。
            **kwargs: 任意额外的关键字参数。 通常传递给模型提供者API调用。

        返回:
            一个GenerationChunks的迭代器。
        """
        context = sentiment_analysis(prompt)
        for char in context:
            chunk = GenerationChunk(text=char)
            if run_manager:
                run_manager.on_llm_new_token(chunk.text, chunk=chunk)
            yield chunk

    @property
    def _llm_type(self) -> str:
        """获取此聊天模型所使用的语言模型的类型。 仅用于记录目的。"""
        return "my_open_llm"


prompt = "The food is very delicious."
llm = MyOpenLLM()
print(llm.invoke(prompt))

# 流式大语言模型
# prompt = f"""
#     功能：写出李白的《将进酒》。
#     限制：使用中文。
# """
# chunks = azure_chat.stream(prompt)
# for chunk in chunks:
#     print(chunk.content, end="", flush=True)
