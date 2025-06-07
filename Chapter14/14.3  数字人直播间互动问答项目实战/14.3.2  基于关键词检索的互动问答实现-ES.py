#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 23:41
# @Author  : yongjie.su
# @File    : 14.3.2  基于关键词检索的互动问答实现-ES.py
# @Software: PyCharm
from loguru import logger
from elasticsearch import Elasticsearch

es_host = "localhost"
es_user = "user"
es_passwd = "passwd"

es_client = Elasticsearch(hosts=es_host, http_auth=(es_user, es_passwd))


def es_query(index_name, search_query, size):
    logger.debug(f"{index_name=} {search_query=} {size=}")
    res = es_client.search(index=index_name, body=search_query, size=size)
    if len(res['hits']['hits']) < 1:
        logger.error(f"NOTHING FOUND FOR {search_query}")
        raise ValueError(f"NOTHING FOUND FOR {search_query}")
    return res


def query_by_keyword(index_name, keyword, size=1):
    """
    通过回答的文本匹配问答URL
    :param index_name:
    :param keyword:
    :param size: 返回个数
    :return:
    """
    # 进行关键词搜索，搜索文本，关键词 字段
    search_query = {
        'query': {
            "multi_match": {
                "query": keyword, "fields": ["text", "keyword"],
                "operator": "or"
            }
        }
    }
    try:
        sub_hits = es_query(index_name, search_query, size=size)
    except Exception as err:
        logger.exception(err)
        return []
    return sub_hits
