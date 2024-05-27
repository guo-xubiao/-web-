from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By
from utils.database_utils.mysql_handle import MySQLHandle
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.get_driver import get_driver
from utils.ui_utils.base_page import BasePage
from config import login_and_assert

mysql_hadle = MySQLHandle(host='localhost', user='root', password='123456', port=3308, database='test_db')


@allure.feature("页面跳转模块")
class TestPageRedirect:
    @staticmethod
    def get_data_from_database():
        mysql_hadle.connect()
        login_data = mysql_hadle.select_data(table="login_data", fields="username,password,timeout", limit=2,
                                             condition='id=2')
        mysql_hadle.close()
        return login_data
    @allure.story("测试页面跳转")
    @allure.title('登录成功')
    @pytest.mark.parametrize("username, password, timeout", get_data_from_database(),ids=['****'])
    def test_page_redirect(self, allure_report, username, password, timeout):

        # 打开浏览器
        with allure.step('打开浏览器'):
            driver = get_driver('edge')
        with allure.step('打开网站并登录'):
            base_page = BasePage(driver)
            login_and_assert(driver, username, password, timeout)

        with allure.step('页面切换'):
            # 点击‘软件测试’进行页面切换
            base_page.click_element(
                (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div/div[1]/div/div[1]/div/div[1]/div/div[2]/span[3]/a'))
            base_page.get_current_window_handle()
            base_page.get_window_handles()
            base_page.switch_to_new_window()
            sleep(5)
            base_page.get_screenshot("D:\\Web_Test_boxuegu\\output\\image\\screenshot2.png")
        with allure.step('断言'):
            result = base_page.assert_text("软件测试", "软件测试")

        if result:
            logger = Logger(log_file='D:\\Web_Test_boxuegu\\output\\log\\test.log', log_level='INFO')
            logger.info('运行了test_page_redirect')
            logger.debug('test_page_redirect debug')

        base_page.quit()
