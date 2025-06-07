#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/11 21:26
# @Author  : yongjie.su
# @File    : 12.3.2  品牌知识库和Prompt模版结合生成口播台词.py
# @Software: PyCharm

mock_top_3_contents = [
    "护手霜是一种能愈合及抚平肌肤裂痕，干燥，能够有效预防及治疗秋冬季手部粗糙干裂的护肤产品，秋冬季节经常使用可以使手部皮肤更加细嫩滋润。",
    "护手霜的主要功能是以保持皮肤。它的特点是不仅能保持皮肤水分的平衡，而且还能补充重要的油性成分、亲水性保湿成分和水分，并能作为活性成分和药剂的载体，使之为皮肤所吸收，达到调理和营养皮肤的目的。",
    "涂护手霜是有诀窍的，最好是先将护手霜挤在双掌中搓热，然后在手心、手背、手指和指甲上都涂抹上护手霜。接着用一根手指按摩涂抹，温热的感觉不但很舒服，也让吸收度更好。"
]


def get_content_by_rag(brand: str, *args, **kwargs):
    """
    返回品牌相关的知识库内容
    :param brand: 品牌名称
    :param args:
    :param kwargs:
    :return:
    """
    print(f"当前品牌是：{brand=}")
    return "\n".join(mock_top_3_contents)


from langchain_core.prompts import PromptTemplate

# 知识库返回的结果
product_content_from_rag = get_content_by_rag(brand="护手霜")
print(product_content_from_rag)

segment_template = """
    # 角色
    电商平台数字人直播商品台词撰写专家，注重品牌的精细化运营。

    # 技能
        - 精通中文，有良好的中文表达能力
        - 精通大品牌分段式数字人直播台词撰写
        - 掌握Markdown语法，能够准确识别和处理相关信息

    # 商品信息
        - 直播间信息：{room_info}
        - 商品名称：{product_name}
        - 商品规格：{product_specification}
        - 商品功效：{product_effectiveness}
        - 商品质量：{product_quality}
        - 商品优惠：{product_discount}
        - 商品物流：{product_shipping}
        - 知识库补充信息：```{product_content_from_rag}```
        
    # 电商平台规范
        - 规范内容：{standard_content}

    # 输出要求
        - 根据分段要求，按段输出内容，每段字数要求在100-200字以内，符合中文简体语言规范
        - 根据提供的直播间信息、商品信息和知识库补充信息，撰写数字人直播分段式台词
        - 内容要真实，段与段，句子与句子之前连贯，具有逻辑性，不能夸大其词
        - 遵守电商平台的规则和法律规范
        - 以销售为目的，突出商品特点
        - 所有台词不能包括敏感词库里面的任何一个字词
        - 只输出与该商品相关的信息，其他信息自动忽略

    # 分段要求
        1. 引导话术：要求用吸引力强的开场白来抓住观众的注意力，简洁明了地介绍直播的主题和重点，激发观众的兴趣和好奇心。
        2. 用户痛点：要求识别并放大观众的痛点，清晰展示问题的严重性，并介绍产品如何有效地解决这些问题，为观众提供实质性的解决方案。
        3. 产品卖点：详细介绍产品的规格、成分和材质，突出其功能和独特优势。说明产品的核心卖点，强调产品的独特之处，以便让观众对产品产生信任和兴趣。
        4. 使用方法：详细说明产品的使用方法，展示实际使用场景，帮助观众理解如何使用产品以及在日常生活中如何受益。
        5. 优惠机制：清晰传达当前的优惠活动，包括会员折扣、满减活动、节假日促销或店铺周年庆等，吸引观众参与并促进购买。
        6. 商品促单：强调产品的核心卖点，展示客户好评和口碑，并提醒观众当前的优惠折扣或限时促销，激发购买欲望和紧迫感。

    # 敏感词库
        敏感词：世界级、最高级、第一、唯一、首个、最好、最便宜、美白、祛痘
"""
# 实例化模版
prompt = PromptTemplate.from_template(template=segment_template)

room_info = "xxx直播间"
product_name = "护手霜"
product_specification = "300ml"
product_effectiveness = "能愈合及抚平肌肤裂痕、干燥"
product_quality = "商品是正品，有质量保障"
product_discount = "会员打9折，限时买二送一"
product_shipping = "顺风快递，包邮"
product_content_from_rag = product_content_from_rag

standard_content = "参考《京东、淘宝电商平台规范》"

prompt = prompt.format(
    room_info=room_info,
    product_name=product_name,
    product_specification=product_specification,
    product_effectiveness=product_effectiveness,
    product_quality=product_quality,
    product_discount=product_discount,
    product_shipping=product_shipping,
    product_content_from_rag=product_content_from_rag,
    standard_content=standard_content
)
print(f"实例化模版结果: {prompt}")
