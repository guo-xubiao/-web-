# 从测试报告中获取测试结果

import mysql.connector

def save_test_results_to_mysql(results_file, host, user, password, database):
    # 连接到 MySQL 数据库
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # 创建游标
    cursor = conn.cursor()

    # 创建测试结果表
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_results
                    (case_name VARCHAR(255), result VARCHAR(50))''')

    # 读取测试结果文件
    with open(results_file, 'r') as file:
        content = file.readlines()

    # 提取测试结果并插入到数据库
    for line in content:
        if line.strip():  # 忽略空行
            case_name, result = line.strip().split('：')
            cursor.execute("INSERT INTO test_results (case_name, result) VALUES (%s, %s)", (case_name, result))

    # 提交事务
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # 从测试报告中获取测试结果
    with open('results.txt', 'r') as file:
        content = file.read()

    # 假设测试结果的格式为：测试用例名称：测试结果
    results = content.split('\n')

    # 遍历结果列表，提取测试用例名称和测试结果
    for result in results:
        if result:
            case_name, result = result.split('：')
            print(f'测试用例：{case_name}，测试结果：{result}')

            # 或者根据测试结果执行相应的操作
            if result == '通过':
                # 执行通过操作
                print(f'执行通过操作，测试用例：{case_name}')

            elif result == '失败':
                # 执行失败操作
                print(f'执行失败操作，测试用例：{case_name}')

            else:
                # 执行其他操作
                print(f'执行其他操作，测试用例：{case_name}')

    # 将测试结果保存到数据库中
    save_test_results_to_mysql(
        results_file='results.txt',
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )


