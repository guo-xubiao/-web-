# 封装的pymysql的一些操作方法

import pymysql


class MySQLHandle:
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def execute_sql(self, sql, params=None):
        if not self.conn or not self.cursor:
            self.connect()

        try:
            if params:
                self.cursor.execute(sql, params)

            else:
                self.cursor.execute(sql)

            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            raise e

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_many(self, size):
        return self.cursor.fetchmany(size)

    def insert_data(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))

        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"

        self.execute_sql(sql, tuple(data.values()))

    def update_data(self, table, data, condition):
        set_sql = ', '.join([f"{key} = %s" for key in data])

        sql = f"UPDATE {table} SET {set_sql} WHERE {condition}"

        self.execute_sql(sql, tuple(data.values()) + (condition,))

    def delete_data(self, table, condition):
        sql = f"DELETE FROM {table} WHERE {condition}"

        self.execute_sql(sql, (condition,))

    def select_data(self, table, fields=None, condition=None, order=None, limit=None):
        sql = f"SELECT {fields or '*'} FROM {table}"

        if condition:
            sql += f" WHERE {condition}"

        if order:
            sql += f" ORDER BY {order}"

        if limit:
            sql += f" LIMIT {limit}"

        self.execute_sql(sql)

        return self.fetch_all()
