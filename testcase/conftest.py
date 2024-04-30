import allure
import pytest


# 跨平台的支持allure，用于生成allure测试报告
@pytest.fixture(scope="session", autouse=True)
def allure_report():
    with allure.step("allure_report"):
        allure.attach("allure测试报告", "allure测试报告")
    yield  # 结束函数
