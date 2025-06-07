#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/9/3 21:59
# @Author  : yongjie.su
# @File    : mysql_utils.py
# @Software: PyCharm
from loguru import logger
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from urllib.parse import quote_plus as urlquote


class DBUtils:
    def __init__(self, **kwargs):
        self._username = kwargs.get('username', 'admin')
        self._password = kwargs.get('password', 'admin')
        self._host = kwargs.get('host', 'localhost')
        self._port = kwargs.get('port', '3306')
        self._database = kwargs.get('database', 'test')
        self._charset = kwargs.get('charset', 'utf8mb4')
        self._database_connection = (
            f"mysql+pymysql://{self._username}:{urlquote(self._password)}@"
            f"{self._host}:{self._port}/{self._database}?charset={self._charset}&autocommit=true"
        )
        self.engine = self.engine = create_engine(
            self._database_connection,
            pool_pre_ping=True,
            pool_size=10,
            pool_timeout=20,
            pool_recycle=3600
        )
        self.session = Session(self.engine)

    def connect_db(self):
        """
        创建数据库连接
        :return:
        """
        try:
            connection = self.engine.connect()
            connection.close()
            return True
        except Exception as err:
            logger.exception(f"链接数据库异常：{err=}")
            return False

    def show_databases(self):
        """
        查询所有数据库
        :return:
        """
        show_databases_sql = f"SELECT schema_name FROM information_schema.schemata"
        database_names = self.execute_all(show_databases_sql)
        database_names = [database[0] for database in database_names]
        return database_names

    def show_tables(self, database=None):
        """
        查询指定数据库的所有表
        :param database: 数据库名称
        :return:
        """
        if not database:
            return []
        show_tables_sql = f"SELECT table_name FROM information_schema.tables " \
                          f"WHERE table_schema = '{database}'"
        table_names = self.execute_all(show_tables_sql)
        table_names = [table[0] for table in table_names]
        return table_names

    def get_table_schema(self, table_name=None):
        """
        查询指定表的schema信息
        :param table_name: 表名称
        :return:
        """
        if not table_name:
            return None
        show_sql = f"SHOW CREATE TABLE {table_name}"
        create_table_statement = self.execute_first(show_sql)
        if len(create_table_statement) < 2 or create_table_statement is None:
            logger.exception(f"表不存在：{table_name=}")
            return None
        return create_table_statement[1]

    def get_database_tables_schema(self, database=None):
        """
        查询指定数据库的所有表的schema
        :param database: 数据库名称
        :return:
        """
        if not database:
            return None
        table_names = self.show_tables(database)
        table_schema_mapping = {}
        for table_name in table_names:
            create_table_statement = self.get_table_schema(table_name)
            table_schema_mapping[table_name] = create_table_statement
        return table_schema_mapping

    def execute_first(self, sql: str):
        """
        执行SQL，返回第一个结果
        :param sql:
        :return:
        """
        return self.session.execute(text(sql)).first()

    def execute_all(self, sql: str):
        """
        执行SQL，返回所有结果
        :param sql:
        :return:
        """
        return self.session.execute(text(sql)).all()


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
    res = db.connect_db()
    print(res)
    database_names = db.show_databases()
    print(database_names)
    table_names = db.show_tables(database=config['database'])
    print(table_names)
    print(db.get_table_schema("t_user"))
    print(db.get_database_tables_schema(database=config['database']))
