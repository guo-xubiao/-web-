import pytest

from config import login_and_assert
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.base_page import BasePage
from utils.ui_utils.get_driver import get_driver


class TestLogin:
    @pytest.mark.parametrize("username, password, timeout", [
        ("19197051934", "@gxb04215", 30),
        # ("another_username", "another_password", 20),
        # ("yet_another_username", "yet_another_password", 10)
    ])
    def test_login1(self, allure_report, username, password, timeout):
        # 打开浏览器
        driver = get_driver('edge')
        login_and_assert(driver, username, password, timeout)
        base_page = BasePage(driver)
        base_page.get_screenshot("D:\\Web_Test_boxuegu\\output\\image\\screenshot.png")
        result = base_page.assert_text("个人中心", "个人中心")

        if result:
            logger = Logger(log_file='D:\\Web_Test_boxuegu\\output\\log\\test.log', log_level='INFO')
            logger.info('运行了test_login1')
            logger.debug('test_login1 debug')
