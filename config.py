from time import sleep

from selenium.webdriver.common.by import By

from utils.ui_utils.base_page import BasePage


def login_and_assert(driver, username, password, timeout):
    base_page = BasePage(driver)
    base_page.open_url("https://passport.boxuegu.com/user/login?refer=https%3A%2F%2Fwww.boxuegu.com%2F")
    base_page.click_element((By.CLASS_NAME, "check-submit"))
    base_page.click_element((By.CLASS_NAME, "empty"))
    base_page.input_text((By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]/form/div[1]/div/div/input'),
                         username, timeout)
    base_page.input_text((By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]/form/div[2]/div/div/input'),
                         password, timeout)
    base_page.click_element((By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[3]/div[2]/div[2]/button'))
    sleep(5)  # 可以适当增加等待时间
    base_page.assert_text("个人中心", "个人中心")
