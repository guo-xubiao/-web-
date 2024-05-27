import allure
import pytest

from config import login_and_assert
from utils.database_utils.mysql_handle import MySQLHandle
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage
from utils.ui_utils.get_driver import get_driver

mysql_hadle = MySQLHandle(host='localhost', user='root', password='123456', port=3308, database='test_db')


@allure.feature('登录模块')
class TestLogin:
    @staticmethod
    def get_data_from_database():
        mysql_hadle.connect()
        login_data = mysql_hadle.select_data(table="login_data", fields="username,password,timeout", limit=2,
                                             condition='id=1')
        mysql_hadle.close()
        return login_data

    @allure.title('登录成功')
    @allure.story('用户登录')
    @pytest.mark.parametrize("username, password, timeout", get_data_from_database(),ids=['****'])
    def test_login1(self, allure_report, username, password, timeout):
        # 打开浏览器
        with allure.step('打开浏览器'):
            driver = get_driver('edge')
        with allure.step('打开网站并登录'):
            base_page = BasePage(driver)
            login_and_assert(driver, username, password, timeout)
            base_page.get_screenshot("D:\\Web_Test_boxuegu\\output\\image\\screenshot.png")
        with allure.step('断言'):
            result = base_page.assert_text("个人中心", "个人中心")

        if result:
            logger = Logger(log_file='D:\\Web_Test_boxuegu\\output\\log\\test.log', log_level='INFO')
            logger.info('运行了test_login1')
            logger.debug('test_login1 debug')

        base_page.quit()
