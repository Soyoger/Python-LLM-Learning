#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 22:37
# @Author  : yongjie.su
# @File    : 10.3.2  基于FastAPI框架的接口部署.py
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union
from fastapi.responses import JSONResponse
from transformers import AutoTokenizer, AutoModel

app = FastAPI()

chatglm_6b_path = "chatglm3-6b"
tokenizer = AutoTokenizer.from_pretrained(chatglm_6b_path, trust_remote_code=True)
model = AutoModel.from_pretrained(
    chatglm_6b_path,
    trust_remote_code=True
).half().cuda()
model = model.eval()


class Input(BaseModel):
    question: str = Field(..., description="提问")
    history: Union[list, None] = Field(None, description="记忆信息")
    top_p: float = Field(..., description="核采样")
    temperature: float = Field(..., description="温度")


@app.post("/chat")
def chat(data: Input):
    question = data.question
    history = data.history
    top_p = data.top_p
    temperature = data.temperature
    if not history:
        history = []
    response, history = model.chat(
        tokenizer,
        question,
        history=history,
        top_p=top_p,
        temperature=temperature
    )
    content = {"response": response, "history": history}
    return JSONResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
