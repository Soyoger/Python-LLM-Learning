#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 17:58
# @Author  : yongjie.su
# @File    : test_langsmith.py
# @Software: PyCharm
import os

os.environ['LANGCHAIN_API_KEY'] = "lsv2_pt_xxx"
LANGCHAIN_TRACING_V2 = True
LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com"
LANGCHAIN_API_KEY = "lsv2_pt_xxx"
LANGCHAIN_PROJECT = "pr-monthly-helmet-69"

from langchain_openai import AzureChatOpenAI

azure_endpoint = "https://internal-qa-service-branch2.openai.azure.com/"
openai_api_key = "eeexxx"

azure_chat = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key)

# print(azure_chat.invoke("Hello, world!"))

# dataset_name = "LCEL-QA"

from langsmith import Client
from langsmith.schemas import Run, Example
from langsmith.evaluation import evaluate
import openai
from langsmith.wrappers import wrap_openai


# Define AI system
# openai_client = wrap_openai(azure_chat.Client())


def predict(inputs: dict) -> dict:
    messages = [{"role": "user", "content": inputs["input"]}]
    response = azure_chat.invoke(input=messages, model="gpt-3.5-turbo")
    return {"output": response}


# Define evaluators
def must_mention(run: Run, example: Example) -> dict:
    prediction = run.outputs.get("output") or ""
    required = example.outputs.get("must_mention") or []
    score = all(phrase in prediction for phrase in required)
    return {"key": "must_mention", "score": score}


dataset_name = "ds-potable-attachment-83"
experiment_results = evaluate(
    predict,  # Your AI system
    data=dataset_name,  # The data to predict and grade over
    evaluators=[must_mention],  # The evaluators to score the results
    experiment_prefix="rap-generator",  # A prefix for your experiment names to easily identify them
    metadata={
        "version": "1.0.0",
    },
)
print(experiment_results)
