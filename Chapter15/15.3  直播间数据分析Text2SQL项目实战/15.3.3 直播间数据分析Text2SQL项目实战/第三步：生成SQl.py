#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 23:39
# @Author  : yongjie.su
# @File    : 第三步：生成SQl.py
# @Software: PyCharm
import os
import json
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from mysql_utils import DBUtils

azure_endpoint = "https://internal-qa-service-branch2.openai.azure.com/"
openai_api_key = "eeexxx"

llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    azure_deployment="gpt-35-turbo",
    openai_api_version="2024-02-15-preview",
    openai_api_key=openai_api_key
)


def generate_sql(question: str, table_info_str: str):
    """
    生成SQL语句
    :param question: 用户提问
    :param table_infos:
    :return:
    """
    prompt_template = """
        # 角色
        现在你是一个资深数据分析师，精通各类数据分析场景。

        # 技能
            - 精通中文，具备出色的中文阅读与理解能力
            - 熟练掌握MySQL数据库，能够根据“任务”中的用户需求，结合“表信息”，快速编写出准确且高效的SQL语句

        # 任务
            - 用户需求：{question}

        # 表信息
            - {table_info_str}

        # 输出
            - 要求仅输出SQL语句，不需要输出分析过程。SQL以#开头,以#结尾，样例如下： #SELECT * FROM TABLE LIMIT 10#
            - 只输出与该任务相关的信息，其他信息自动忽略
        """

    prompt_format = PromptTemplate.from_template(prompt_template)
    prompt = prompt_format.format(
        question=question,
        table_info_str=table_info_str
    )
    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    config = {
        "username": "admin",
        "password": "admin",
        "host": "localhost",
        "port": "3306",
        "database": "test",
        "charset": "utf8mb4"
    }
    db = DBUtils(**config)
    table_infos = db.get_database_tables_schema(database=config['database'])
    question = "请问一共有多少个用户？"
    if isinstance(table_infos, dict):
        table_info_str = json.dumps(table_infos, ensure_ascii=False)
    else:
        table_info_str = table_infos
    sql = generate_sql(question, table_info_str)
    print(sql)
    final_sql = sql.replace("#", "")
    print(final_sql)
    results = db.execute_all(final_sql)
    print(results)
