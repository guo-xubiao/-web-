from time import sleep

import pytest
from selenium.webdriver.common.by import By

from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.get_driver import get_driver
from utils.ui_utils.base_page import BasePage
from config import login_and_assert


class Test_Page_Redirect():
    @pytest.mark.parametrize("username, password, timeout", [
        ("19197051934", "@gxb04215", 30),
        # ("another_username", "another_password", 20),
        # ("yet_another_username", "yet_another_password", 10)
    ])
    def test_page_redirect(self, allure_report, username, password, timeout):
        # 打开浏览器
        driver = get_driver('edge')
        login_and_assert(driver, username, password, timeout)
        base_page = BasePage(driver)
        # 点击软件测试进行页面切换
        base_page.click_element(
            (By.XPATH, '//*[@id="__layout"]/div/div[2]/section/div/div[1]/div/div[1]/div/div[1]/div/div[2]/span[3]/a'))
        base_page.get_current_window_handle()
        base_page.get_window_handles()
        base_page.switch_to_new_window()
        sleep(5)
        base_page.get_screenshot("D:\\Web_Test_boxuegu\\output\\image\\screenshot2.png")
        result = base_page.assert_text("软件测试", "软件测试")

        if result:
            logger = Logger(log_file='D:\\Web_Test_boxuegu\\output\\log\\test.log', log_level='INFO')
            logger.info('运行了test_page_redirect')
            logger.debug('test_page_redirect debug')
