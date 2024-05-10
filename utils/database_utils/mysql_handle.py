import pymysql


class MySQLHandle:
    def __init__(self, host, user, password, database, port, charset='utf8'):
        """
        初始化MySQLHandle类

        Parameters:
        - host: 数据库主机地址
        - user: 数据库用户名
        - password: 数据库密码
        - database: 数据库名称
        - port: 数据库端口
        - charset: 字符编码，默认为utf8
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.conn = None
        self.cursor = None

    def connect(self):
        """
        连接到数据库
        """
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                    port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        """
        关闭数据库连接
        """
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def execute_sql(self, sql, params=None):
        """
        执行SQL语句

        Parameters:
        - sql: 要执行的SQL语句
        - params: SQL语句中的参数

        Raises:
        - Exception: 执行SQL语句出现异常时抛出
        """
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
        """
        获取所有查询结果
        """
        return self.cursor.fetchall()

    def fetch_one(self):
        """
        获取单条查询结果
        """
        return self.cursor.fetchone()

    def fetch_many(self, size):
        """
        获取指定数量的查询结果

        Parameters:
        - size: 指定数量

        Returns:
        - 查询结果的列表
        """
        return self.cursor.fetchmany(size)

    def insert_data(self, table, data):
        """
        向表中插入数据

        Parameters:
        - table: 表名
        - data: 要插入的数据，字典类型，键为字段名，值为字段值
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))

        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"

        self.execute_sql(sql, tuple(data.values()))

    def update_data(self, table, data, condition):
        """
        更新表中的数据

        Parameters:
        - table: 表名
        - data: 要更新的数据，字典类型，键为字段名，值为字段值
        - condition: 更新条件
        """
        set_sql = ', '.join([f"{key} = %s" for key in data])

        sql = f"UPDATE {table} SET {set_sql} WHERE {condition}"

        self.execute_sql(sql, tuple(data.values()) + (condition,))

    def delete_data(self, table, condition):
        """
        删除表中的数据

        Parameters:
        - table: 表名
        - condition: 删除条件
        """
        sql = f"DELETE FROM {table} WHERE {condition}"

        self.execute_sql(sql, (condition,))

    def select_data(self, table, fields=None, condition=None, order=None, limit=None):
        """
        查询数据

        Parameters:
        - table: 表名
        - fields: 要查询的字段，默认为全部字段
        - condition: 查询条件
        - order: 排序方式
        - limit: 查询结果数量限制

        Returns:
        - 查询结果的列表
        """
        sql = f"SELECT {fields or '*'} FROM {table}"

        if condition:
            sql += f" WHERE {condition}"

        if order:
            sql += f" ORDER BY {order}"

        if limit:
            sql += f" LIMIT {limit}"

        self.execute_sql(sql)

        return self.fetch_all()
