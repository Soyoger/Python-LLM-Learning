#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 19:11
# @Author  : yongjie.su
# @File    : 9.4.2  PEFT介绍.py
# @Software: PyCharm

# from peft import PromptEncoderConfig, TaskType
#
# p_tuning_config = PromptEncoderConfig(
#     encoder_reparameterization_type="MLP",
#     encoder_hidden_size=128,
#     num_attention_heads=16,
#     num_layers=24,
#     num_transformer_submodules=1,
#     num_virtual_tokens=20,
#     token_dim=1024,
#     task_type=TaskType.SEQ_CLS
# )
#
# from transformers import AutoModelForCausalLM
#
# model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m")
#
# from peft import get_peft_model
#
# p_tuning_model = get_peft_model(model, p_tuning_config)
# p_tuning_model.print_trainable_parameters()
#
# p_tuning_model.save_pretrained("./opt-350m-p_tuning_20240714")

# 推理
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM

config = PeftConfig.from_pretrained("./opt-350m-p_tuning_20240714")
model = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)
p_tuning_model = PeftModel.from_pretrained(model, "./opt-350m-p_tuning_20240714")
