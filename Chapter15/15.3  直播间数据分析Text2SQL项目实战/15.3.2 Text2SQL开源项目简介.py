#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 20:42
# @Author  : yongjie.su
# @File    : 15.3.2 Text2SQL开源项目简介.py
# @Software: PyCharm
from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore


class VannaDemo(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


config = {
    'api_key': 'sk-xxx',
    'model': 'gpt-3.5'
}

vn = VannaDemo(**config)

vn.train(ddl="""
        CREATE TABLE `t_user` (
            `id` int NOT NULL AUTO_INCREMENT COMMENT '主键ID',
            `login_name` varchar(30) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '登录名',
            `password` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '密码',
            `user_type` tinyint DEFAULT '0' COMMENT '0内部用户；1外部客户',
            `nickname` varchar(30) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '客户昵称',
            `head_img` varchar(128) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '头像',
            `mobile` varchar(11) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '手机号',
            `status` tinyint DEFAULT '0' COMMENT '状态：0正常；1删除；2禁用',
            `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
            `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
            PRIMARY KEY (`id`),
            UNIQUE KEY `idx_login_name` (`login_name`) USING BTREE,
            KEY `idx_mobile` (`mobile`) USING BTREE
        ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户表'
""")

vn.train(documentation="表 t_user 用来存储系统的用户信息")

vn.train(sql="SELECT id, login_name FROM t_user WHERE login_name = 'admin'")

vn.ask("统计一下内部用户和外部用户分别有多少人？")
