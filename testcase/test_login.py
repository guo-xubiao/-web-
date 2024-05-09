import pytest

from config import login_and_assert
from utils.logger_utils.loguru_log import Logger
from utils.ui_utils.get_driver import get_driver


class Test_Login():
    @pytest.mark.parametrize("username, password, timeout", [
        ("19197051934", "@gxb04215", 30),
        # ("another_username", "another_password", 20),
        # ("yet_another_username", "yet_another_password", 10)
    ])
    def test_login1(self, allure_report, username, password, timeout):
        # 打开浏览器
        driver = get_driver('edge')
        login_and_assert(driver, username, password, timeout)

        logger = Logger(log_file='D:\\Web_Test_boxuegu\\output\\log\\test.log', log_level='INFO')
        logger.info('test_login1')
        logger.debug('test_login1 debug')
