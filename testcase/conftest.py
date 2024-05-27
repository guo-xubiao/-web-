import allure
import pytest

from utils.database_utils.mysql_handle import MySQLHandle


# 跨平台的支持allure，用于生成allure测试报告
@pytest.fixture(scope="session", autouse=True)
def allure_report():
    with allure.step("allure_report"):
        allure.dynamic.description("这是一个allure测试报告")
    yield  # 结束函数
