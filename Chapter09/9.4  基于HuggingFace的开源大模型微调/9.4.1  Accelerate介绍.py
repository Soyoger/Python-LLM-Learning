#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/13 22:19
# @Author  : yongjie.su
# @File    : 9.4.1  Accelerate介绍.py
# @Software: PyCharm

# from accelerate import Accelerator
# accelerator = Accelerator()
# device = accelerator.device
# model, optimizer, training_dataloader, scheduler = accelerator.prepare(
#     model, optimizer, training_dataloader, scheduler
# )


# init_empty_weights 的使用
# from accelerate import init_empty_weights
# from transformers import BertModel
#
# # 使用 init_empty_weights 上下文管理器来初始化模型
# with init_empty_weights():
#     model = BertModel.from_pretrained("bert-large-uncased")
#
# # 在 init_empty_weights 之外，可以正常使用模型
# # 例如，将模型放置到某个设备上
# model.to("cuda")


# 使用load_checkpoint_and_dispatch
# from accelerate import load_checkpoint_and_dispatch
# from transformers import AutoConfig, AutoModelForCausalLM
#
# # 配置 checkpoint 文件路径
# checkpoint_path = "./checkpoint"
# # 加载模型配置
# model_config = AutoConfig.from_pretrained(checkpoint_path)
# # 创建模型但不加载权重
# model = AutoModelForCausalLM.from_config(model_config)
#
# # 使用 load_checkpoint_and_dispatch 来加载权重并分配到多个设备
# model = load_checkpoint_and_dispatch(
#     model,
#     checkpoint_path,
#     device_map="auto",  # 自动分配设备
#     no_split_module_classes=["GPT2Block"]  # 指定不分割的模块类
# )
# 现在模型的权重已经分配到多个设备，可以正常使用模型进行推理或训练
# outputs = model.generate(input_ids)

# 使用案例
from accelerate import Accelerator
import torch
from torch.utils.data import DataLoader, TensorDataset

# 初始化Accelerator
accelerator = Accelerator()

# 创建一个简单的模型
model = torch.nn.Linear(10, 1)

# 创建数据集和数据加载器
dataset = TensorDataset(torch.randn(100, 10), torch.randn(100, 1))
dataloader = DataLoader(dataset, batch_size=16)

# 准备优化器
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 使用accelerator准备模型、数据加载器和优化器
model, dataloader, optimizer = accelerator.prepare(model, dataloader, optimizer)

# 训练循环
for epoch in range(10):
    for batch in dataloader:
        inputs, targets = batch
        outputs = model(inputs)
        loss = torch.nn.functional.mse_loss(outputs, targets)
        optimizer.zero_grad()
        accelerator.backward(loss)
        optimizer.step()

    print(f"Epoch {epoch} completed.")
